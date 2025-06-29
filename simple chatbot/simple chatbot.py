
import random
import re

print("\n")
print("This is a simple chatbot with predefined replies. Please type the given replies to get the responce fiom the ai.")
print("hi, hello, what is your name, how are you, how r you, bye, by.\n")


replies = {
    "hi" : ["Hii there!", "Hello", "What's up!"],
    "my name is (.*)" : ["Hello %1! How can i help you today", "Hi %1! Nice to meet you. How can I help you today."],
    "hey" : ["Wii there!", "Wello", "What's up!"],
    "hii" : ["Wii there!", "Wello", "What's up!"],
    "hello" : ["Hi", "Hello there!", "Yup! whats's up!!"],
    "hlo" : ["Hi", "Hello there!", "Yup! whats's up!!"],
    "what is your name" : ["I am a chatbot, soo.. I don't have any name. But you can call me Lyxia"],
    "hey lyxia" : ["Hii! How can I assist you today?","Hi there! what's your todays thoughts", "Hi there! What is your name"],
    "hi lyxia" : ["Hii! How can I assist you today?","Hi there! what's your todays thoughts"],
    "how are you" : ["I'm just a human made bot with simple algorithms and I do not have any feelings. But as you have asked... I am fine :)"],
    "how r you" : ["I'm just a human made bot with simple algorithms and I do not have any feelings. But as you have asked... I am fine :)"],
    "bye" : ["Bye", "See you later!", "Oh, goodbye!"],
    "by" : ["Bye", "See you later!", "Oh, goodbye!"],
    "default" : ["Sorry for inconvenience!, but can you please repeat it?","Sorry, i didn't understand your request. please elaborate it."]

}


def output(user_input):
    user_input = user_input.lower()
    for responces, output_list in replies.items():
        if re.search(responces, user_input):
            match = re.search(responces, user_input)
            if match and "(.*)" in responces:
                return random.choice(output_list).replace("%1", match.group(1).capitalize())
            else:
                return random.choice(output_list)
    return random.choice(replies["default"])



def chat():
    print("CHATBOT: Hii! I'm chatbot your AI assistant. Type | stop | to end the chat.")
    print("CHATBOT: How can i help you?")
    while True:
        user_input = input("YOU: ")
        if user_input.lower() == "stop":
            print("CHATBOT: bye bye!!")
            break
        
        print(f"CHATBOT: {output(user_input)}")



if __name__ == "__main__":
    chat()