import sys
import time
import random

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1/10)
def slowprint2(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.1/10)

slowprint("Greetings! I'm an advanced AI chatbot designed to engage in fascinating discussions.")

def chatbot():
    name = input("Chatbot: What's your name? ")
    slowprint("Chatbot: Nice to meet you, " + name + "! You have a wonderful name.")

    questions = [
        "What are your hobbies?",
        "Tell me about an interesting trip or adventure you had.",
        "Do you have any hidden talents or skills?",
        "If you could have any superpower, what would it be and why?",
        "What's the most memorable book you've read recently?",
        "Share a funny or exciting incident from your life.",
        "What's something you've always wanted to learn or try?",
    ]

    answers = []

    for question in questions:
        slowprint("Chatbot: " + question)
        response = input("User: ")
        answers.append(response)

        responses = [
            "That sounds fascinating!",
            "Wow, I'd love to hear more about it!",
            "Impressive!",
            "I can see why that interests you.",
            "That must have been quite an experience.",
            "Nice! It's always good to have a passion.",
            "I hope you get the chance to explore that further."
        ]

        random_response = random.choice(responses)
        slowprint("Chatbot: " + random_response)

    while True:
        response = input("Chatbot: Did you enjoy answering those questions? (yes/no) ")

        if response.lower() == "yes":
            slowprint("Chatbot: I'm glad you enjoyed it!")
            break
        elif response.lower() == "no":
            slowprint("Chatbot: I'm sorry if the questions weren't to your liking. I'll improve next time.")
            break
        else:
            slowprint("Chatbot: I'm sorry, I didn't understand. Please answer with 'yes' or 'no'.")

    slowprint("Chatbot: Here's a summary of your answers:")
    for i in range(len(questions)):
        slowprint2("Q: " + questions[i])
        slowprint2("A: " + answers[i])
        print()

    slowprint("Chatbot: Thank you for chatting, " + name + "! Have a wonderful day.")

chatbot()
