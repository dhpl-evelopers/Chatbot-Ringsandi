import os
import requests
from openai import AzureOpenAI

def main():
    client = AzureOpenAI(
    api_version="2024-05-01-preview",
    azure_endpoint="https://newchatbot.openai.azure.com/",
    api_key="EhlNXF7DZOUmr2RGlQwQ3MdQB2Gc3gL7TmHqdV7wkIBf535p2yrKJQQJ99AKACYeBjFXJ3w3AAABACOG5DMA"
)
    completion= client.chat.completions.create(
        model="Newbot",
        messages=[
            {"role":"system","content": "You are an AI ring expert that helps people find information."},
            {"role":"user","content": "Hi"}
        ]
    )
    print(completion.to_json())
    
if __name__=='__main__': 
    main()