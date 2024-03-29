import os
from dotenv import load_dotenv


load_dotenv()

# Get the API key from the environment variable
HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')
VOYAGE_API_KEY = os.getenv('VOYAGE_API_KEY')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

print(HUGGINGFACEHUB_API_TOKEN)
