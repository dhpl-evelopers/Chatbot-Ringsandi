import os
from openai import AzureOpenAI

endpoint = os.getenv("ENDPOINT_URL", "https://newchatbot.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "Newbot")
search_endpoint = os.getenv("SEARCH_ENDPOINT", "https://newchatbot.search.windows.net")
search_key = os.getenv("SEARCH_KEY", "3YcQ5nEkiEdpeZUrLcaMUfh4U9DDloY4ilvp50thqZAzSeBtSoTC")
search_index = os.getenv("SEARCH_INDEX_NAME", "newchatbot1")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "EhlNXF7DZOUmr2RGlQwQ3MdQB2Gc3gL7TmHqdV7wkIBf535p2yrKJQQJ99AKACYeBjFXJ3w3AAABACOG5DMA")

# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
    azure_endpoint = endpoint,
    api_key = subscription_key,
    api_version = "2024-05-01-preview",
)

completion = client.chat.completions.create(
    model=deployment,
    messages= [
    {
        "role": "system",
        "content": "You are an AI ring expert that helps people find information."
    },
    {
        "role": "user",
        "content": "hi"
    },
    {
        "role": "assistant",
        "content": "Hello! How can I assist you today?"
    },
    {
        "role": "user",
        "content": "what is ringsandi"
    },
    {
        "role": "assistant",
        "content": "RINGS & I is a personalized diamond ring studio that offers made-to-order diamond rings. They provide a unique experience where customers can try on 1200 design prototypes in person, choose their preferred design, size, metal tone, metal finish, and even engrave their rings. Customers can also select from nine different price options based on their preferences and budget [doc2].\n\nThe studio is currently located in Pune, India, with plans to expand to Mumbai, Bengaluru, and Delhi. They also offer virtual appointments for customers who are not in these locations [doc2]."
    }
],
    past_messages=10,
    max_tokens=800,
    temperature=0,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
,
    extra_body={
      "data_sources": [{
          "type": "azure_search",
          "parameters": {
            "endpoint": f"{search_endpoint}",
            "index_name": "newchatbot1",
            "semantic_configuration": "default",
            "query_type": "simple",
            "fields_mapping": {},
            "in_scope": True,
            "role_information": "You are an AI ring expert that helps people find information.",
            "filter": None,
            "strictness": 3,
            "top_n_documents": 5,
            "authentication": {
              "type": "api_key",
              "key": f"{search_key}"
            }
          }
        }]
    })

print(completion.to_json())