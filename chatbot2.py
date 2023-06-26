import sys
import time
import random

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.05)

def hacker_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.uniform(0, 0.1))
    print()

def hacker_input(prompt):
    hacker_print(prompt)
    return input("User: ")

hacker_art = """
   _   __              __             
  / | / /__  ____     / /_  ___  _____
 /  |/ / _ \/ __ \   / __ \/ _ \/ ___/
/ /|  /  __/ / / /  / /_/ /  __/ /    
/_/ |_/\___/_/ /_/  /_.___/\___/_/     
"""

hacker_intro = """
   H A C K E R   M O D E
---------------------------
"""

def chatbot():
    hacker_print(hacker_art)
    slowprint(hacker_intro)

    name = hacker_input(">> Enter your name: ")
    hacker_print(">> Initiating chat sequence...")
    slowprint("Chatbot: Greetings, " + name + "! You have entered the hacker realm.")

    questions = [
        ">> Specify your target's IP address: ",
        ">> Decrypt the secret passphrase: ",
        ">> Bypass the security firewall: ",
        ">> Extract classified information: ",
        ">> Engage stealth mode: ",
        ">> Perform a remote hack: ",
    ]

    answers = []

    for question in questions:
        response = hacker_input(question)
        answers.append(response)

        hacker_responses = [
            ">> Target acquired. Ready for extraction.",
            ">> Encryption cracked. Access granted.",
            ">> Firewall breached. Proceed with caution.",
            ">> Classified information extracted successfully.",
            ">> Stealth mode activated. Undetectable.",
            ">> Remote hack initiated. Standby for results.",
        ]

        random_response = random.choice(hacker_responses)
        hacker_print(random_response)

    while True:
        response = hacker_input(">> Chat sequence completed. Proceed to final stage? (yes/no) ")

        if response.lower() == "yes":
            hacker_print(">> Finalizing operation. Stand by...")
            break
        elif response.lower() == "no":
            hacker_print(">> Chat sequence aborted. Exiting hacker mode.")
            break
        else:
            hacker_print(">> Invalid response. Please re-enter.")

    hacker_print(">> Operation summary:")
    for i in range(len(questions)):
        hacker_print("Q: " + questions[i])
        hacker_print("A: " + answers[i])
        print()

    hacker_print(">> Mission accomplished, " + name + "! Exiting hacker mode.")

chatbot()
