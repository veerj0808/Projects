# Simple Chatbot in Python
# Author: Veer Jain's AI Mentor :)

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How are you today?"
    elif "your name" in user_input:
        return "I'm PyBot, your friendly chatbot!"
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm doing great! 😄"
    elif "bye" in user_input:
        return "Goodbye! Have a great day ahead!"
    else:
        return "Sorry, I didn’t understand that. Can you rephrase?"

print("PyBot: Hello! I’m your chatbot. Type 'bye' to exit.")

while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("PyBot: Goodbye!")
        break
    print("PyBot:", chatbot_response(user))