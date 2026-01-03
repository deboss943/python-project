def run_questionnaire():
    print("Welcome to the Questionnaire!\n")

    questions = [
        "What is your name? ",
        "How old are you? ",
        "What is your favorite programming language? ",
        "Do you have programming experience? (yes/no) ",
        "What country are you from? "
    ]

    answers = []

    for question in questions:
        answer = input(question)
        answers.append(answer)

    print("\n--- Questionnaire Summary ---")
    print(f"Name: {answers[0]}")
    print(f"Age: {answers[1]}")
    print(f"Favorite Programming Language: {answers[2]}")
    print(f"Programming Experience: {answers[3]}")
    print(f"Country: {answers[4]}")

    print("\nThank you for completing the questionnaire!")


# Run the questionnaire
run_questionnaire()

