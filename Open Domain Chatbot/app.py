import openai

# Replace 'YOUR_API_KEY' with your actual API key
openai.api_key = 'YOUR_API_KEY'

def chat_with_bot(prompt):
    response = openai.Completion.create(
        engine="davinci",  # You can choose a different GPT-3 engine
        prompt=prompt,
        max_tokens=50  # Adjust the response length as needed
    )
    return response.choices[0].text

# Example conversation
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    bot_response = chat_with_bot(f"You: {user_input}\nBot:")
    print(f"Bot: {bot_response}")
