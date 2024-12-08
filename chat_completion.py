import os
import openai
from openai import AzureOpenAI
import json

# Custom wrapper class for AzureOpenAI
class AzureOpenAI:
    def __init__(self, api_version, azure_endpoint, api_key):
        self.api_version = api_version
        self.azure_endpoint = azure_endpoint
        self.api_key = api_key
        self.configure_client()

    def configure_client(self):
        openai.api_type = "azure"
        openai.api_base = self.azure_endpoint
        openai.api_key = self.api_key
        openai.api_version = self.api_version

    def create_chat_completion(self, engine, messages):
        try:
            response = openai.ChatCompletion.create(
                engine=engine,
                messages=messages
            )
            return response
        except Exception as e:
            print(f"Error creating chat completion: {e}")
            return None
        
client = AzureOpenAI(
    api_version="2024-05-01-preview",
    azure_endpoint="https://newchatbot.openai.azure.com/",
    api_key="EhlNXF7DZOUmr2RGlQwQ3MdQB2Gc3gL7TmHqdV7wkIBf535p2yrKJQQJ99AKACYeBjFXJ3w3AAABACOG5DMA"
)

completion = client.chat.completions.create(
    model="Newbot",
    messages=[
        {
            "role": "user",
            "content": "Hi",
        }
    ]
)
      
print(completion.to_json())
