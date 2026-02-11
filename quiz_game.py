print("Welcome to the Quiz Game!")
score = 0

playing = (input("Do you want to play? (Yes/No): ").strip().lower() == "yes")
if not playing:
    print("Maybe next time!")
    exit()
else:
    print("Great! Let's start the quiz.")

questions = [
    {
        "question": "What is the capital of Bangladesh?",
        "options": ["Berlin", "Madrid", "Dhaka", "Rome"],
        "answer": "Dhaka"
    },
    {
        "question": "What is 0 + 0 in boolean?",
        "options": [True, False],
        "answer": False
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    }
]

for q in questions:
    # print(q) # just to show the structure of the question dictionary
    print("\n" + q["question"]) # print the question
    for i, option in enumerate(q["options"], 1): # enumerate the options starting from 1. the enumerate function gives us both the index (i) and the option itself. we start from 1 to make it more user-friendly
        print(f"{i}. {option}") # print the options with numbers
    
# ask until we get a valid option number
    while True: # we want to keep asking until we get a valid answer
        try: # we want to catch the case where the user enters something that is not an integer. try is used to catch exceptions. if the user enters something that cannot be converted to an integer, it will raise a ValueError, and we can handle that in the except block.
            answer = int(input("Enter the number of your answer: ")) # declare a variable answer and assign it the integer value of the user's input. we use int() to convert the input string to an integer. if the user enters something that cannot be converted to an integer, it will raise a ValueError, which we will catch in the except block.
            if 1 <= answer <= len(q["options"]): # check if the answer is a valid option number. we check if the answer is greater than or equal to 1 and less than or equal to the number of options. if it is valid, we
                break # out of the loop. if it is not valid, we print an error message and ask again.
            print(f"Please enter a number between 1 and {len(q['options'])}.") # if the answer is not a valid option number, we print an error message and ask again.
        except ValueError:
            print("Please enter a valid integer.")

    # now check
    if q["options"][answer - 1] == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {q['answer']}")

print(f"\nYour final score is: {score}/{len(questions)}")