from openai import AzureOpenAI

# The URL of the load balancer
load_balancer_url = "https://cloudcherry-openai-service.azurewebsites.net"
# The model to use
model_name = "cloudcherry-gpt35t-default"
# The defualt question to ask the model
question = "What is the the meaning of life, the universe, and everything?"

# Function to ask a question
def ask_question(question, load_balancer_url, model_name):
    # Create a OpenAI client
    client = AzureOpenAI(
        azure_endpoint=load_balancer_url,
        api_key="whatever-your-api-key-is-here",
        api_version="2023-12-01-preview"
    )
    # Ask the question
    response = client.chat.completions.create(
        model= model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant expert in the movie called The Hitchhiker's Guide to the Galaxy, responding just with one sentence"},
            {"role": "user", "content": question}
        ]
    )
    # Return the first response
    return response.choices[0].message.content

print(f"Question: {question}")
print(f"Answer: {ask_question(question, load_balancer_url, model_name)}")
