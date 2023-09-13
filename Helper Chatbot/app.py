import openai

# Replace with your OpenAI API key
api_key = "YOUR_API_KEY"


# Function to interact with GPT-3 and get responses
def chatbot_response(question, api_key):
    openai.api_key = api_key

    # Prompt the model with the user's question
    prompt = f"Question: {question}\nAnswer:"

    # Generate a response from GPT-3
    response = openai.Completion.create(
        engine="davinci",  # GPT-3's most capable engine
        prompt=prompt,
        max_tokens=100  # Adjust the response length as needed
    )

    return response.choices[0].text


# Example usage
while True:
    user_question = input("Ask a question (or type 'exit' to quit): ")
    if user_question.lower() == "exit":
        break
    response = chatbot_response(user_question, api_key)
    print(response)
