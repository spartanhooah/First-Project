END_STRING = "\end"
QUESTION_WORDS = ["who", "what", "where", "when", "why", "how"]

input_list = []

while True:
    user_input = input("Say something:")

    if user_input == END_STRING:
        break
    else:
        if QUESTION_WORDS.contains(user_input.split()[0]):
            user_input = user_input + "?"
        else:
            user_input = user_input + "."

        user_input = user_input.capitalize()
        input_list.append

print