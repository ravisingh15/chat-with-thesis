import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_anthropic import ChatAnthropic
from langchain_community.embeddings import VoyageEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from html_template import css, bot_template, user_template



load_dotenv()

# Get the API key from the environment variable
HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')
VOYAGE_API_KEY = os.getenv('VOYAGE_API_KEY')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

# load pdf files and get text
def get_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

# Define embedding model
embeddings = VoyageEmbeddings(voyage_api_key=VOYAGE_API_KEY, model="voyage-2")

# get text chunks
def get_text_chunk(raw_text):
    text_splitter = CharacterTextSplitter(
        separator='\n', chunk_size=500, chunk_overlap=50, length_function=len, is_separator_regex=False
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks

def get_conversation_chain(vector_store):
    llm = ChatAnthropic(temperature=0.5, anthropic_api_key=ANTHROPIC_API_KEY, model_name="claude-3-opus-20240229")
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vector_store.as_retriever(),memory=memory)
    return conversation_chain

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    new_messages = response['chat_history'][-2:]  # Get the last two messages (user question and bot response)
    st.session_state.chat_history.extend(new_messages)  # Append the new messages to the existing chat history
    for message in st.session_state.chat_history:
        if message.type == "human":
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

# loading the pdf
#text = get_pdf_text('thesis.pdf')
#chunks = get_text_chunk(text)
vector_store = FAISS.load_local("faiss_index_mythesis", embeddings, allow_dangerous_deserialization=True)

def main():
    #load_dotenv()
    st.set_page_config(page_title="Chat with my Thesis", page_icon=':books:')
    st.write(css, unsafe_allow_html=True)
    if "conversation" not in st.session_state:
        st.session_state.conversation = []
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    st.header("Chat with my Thesis")
    user_question = st.text_input("Ask me anything")
    if user_question:
        handle_userinput(user_question)
    st.write(user_template.replace("{{MSG}}", "Hello, Bot!"), unsafe_allow_html=True)
    st.write(bot_template.replace("{{MSG}}", "Hello, I am your thesis. Ask me anything"), unsafe_allow_html=True)
    

    st.session_state.conversation = get_conversation_chain(vector_store)

if __name__ == "__main__":
    main()