import threading
from colorama import Fore, Style
from openai import AzureOpenAI

# The URL of the load balancer
load_balancer_url = "https://cloudcherry-openai-service.azurewebsites.net"
# The model to use
model_name = "cloudcherry-gpt35t-default"
# The default question to ask the model
question = "What I could gift to Marta for the International Women's Day?"
# Number of iterations
num_iterations = 6
# Number of threads
num_threads = 1

# Function to ask a question
def ask_question(question, load_balancer_url, model_name):
    # Create a OpenAI client
    client = AzureOpenAI(
        azure_endpoint=load_balancer_url,
        api_key="whatever-your-api-key-is-here",
        api_version="2023-12-01-preview"
    )
    # Ask the question
    response = client.chat.completions.with_raw_response.create(
        model= model_name,
        messages=[
            {"role": "system", "content": "You are a helpful shop assistant expert women shopping, responding just with one short sentence"},
            {"role": "user", "content": question}
        ]
    )
    
    region = response.headers.get("x-ms-region")
    response = response.parse()

    # Print the response
    print(f"Question: {question}")
    if region != "UK South":
        print(f"Answer ({Fore.MAGENTA}{region}{Style.RESET_ALL}): {response.choices[0].message.content}")
    else:
        print(f"Answer ({Fore.YELLOW}{region}{Style.RESET_ALL}): {response.choices[0].message.content}")
    
    # Return the first response
    return 0

# prepare the itaration loop
for i in range(num_iterations):
    # prepare and start threads in the iteration
    threads = []
    for j in range(num_threads):
        t = threading.Thread(target=ask_question, args=(question, load_balancer_url, model_name))
        threads.append(t)
        t.start()
    # Wait for all threads to finish
    for t in threads:
        t.join()

    
