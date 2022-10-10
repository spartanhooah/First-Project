END_STRING = "\end"
QUESTION_WORDS = ("who", "what", "where", "when", "why", "how"]

input_list = []

while True:
    user_input = input("Say something: ")

    if user_input == END_STRING:
        break
    else:
        if user_input.startswith(QUESTION_WORDS):
            user_input = user_input + "?"
        else:
            user_input = user_input + "."

        user_input = user_input.capitalize()
        input_list.append(user_input)

print(" ".join(input_list))