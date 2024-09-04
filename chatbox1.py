def chatbot_response(user_input):
    # Convert input to lowercase to handle case insensitivity
    user_input = user_input.lower()

    # Define responses based on user input
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I am a simple chatbot created to assist you."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"


# Main loop to keep the chatbot running
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)

    # Exit condition
    if "bye" in user_input:
        break