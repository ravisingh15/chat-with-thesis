# Chat with my thesis
Here is the link to [streamlit app](https://chat-with-thesis.streamlit.app/)

![image](https://github.com/ravisingh15/chat-with-thesis/assets/60500638/a2d139f0-5dcb-4e7a-9bde-417804cc3608)
Here, I have built a conversational AI tool to interact with my thesis.

## Title of the thesis
Applications of Artificial Intelligence in the Discovery and Development of Therapeutics for the Treatment of Alzheimer's Disease.

This code is a Streamlit application that allows users to interact with a conversational AI assistant trained on a PDF thesis file using the LangChain library and the Claude-3-opus-20240229 language model from Anthropic.

Here's a breakdown of what the code does:

It imports the necessary libraries and defines functions to load PDF files, split the text into chunks, create embeddings using the VoyageEmbeddings model, and set up the conversational retrieval chain using the ChatAnthropic language model from Anthropic.
The get_pdf_text function extracts the text from a PDF file using the PyPDF2 library.
The get_text_chunk function splits the raw text into smaller chunks using the CharacterTextSplitter from LangChain.
The get_conversation_chain function sets up the conversational retrieval chain using the ConversationalRetrievalChain from LangChain. It initializes the ChatAnthropic language model with the specified API key and model name (claude-3-opus-20240229). This model is used to generate responses based on the user's input and the context retrieved from the vector store.
The handle_userinput function processes the user's question, generates a response using the conversational retrieval chain, and updates the chat history with the new messages.
The main function sets up the Streamlit app, loads the PDF text, creates the vector store, and initializes the conversational retrieval chain.
The Streamlit app displays a text input field where users can ask questions, and it renders the chat history with user messages and bot responses using HTML templates.
In this code, the claude-3-opus-20240229 model from Anthropic is used as the language model for the conversational AI assistant. This model is initialized with the specified API key and temperature (a value that controls the randomness of the generated responses). The assistant uses this model to generate responses based on the user's input and the context retrieved from the vector store, which contains the embeddings of the PDF thesis text.

