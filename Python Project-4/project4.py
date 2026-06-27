questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["A. Karachi", "B. Lahore", "C. Islamabad", "D. Peshawar"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Elon Musk"],
        "answer": "C"
    },
    {
        "question": "How many continents are there?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "Which is the largest ocean?",
        "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
        "answer": "C"
    }
]


def start_quiz():
    score = 0

    print("\n===== General Knowledge Quiz =====")

    for index, q in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {q['question']}")

        for option in q["options"]:
            print(option)

        while True:
            answer = input("Enter your answer (A/B/C/D): ").upper()

            if answer in ["A", "B", "C", "D"]:
                break

            print("Invalid input! Please enter A, B, C or D.")

        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer is {q['answer']}.")

    print("\n===== Quiz Finished =====")
    print(f"Your Score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("Excellent!")
    elif percentage >= 60:
        print("Good Job!")
    elif percentage >= 40:
        print("Keep Practicing!")
    else:
        print("Better Luck Next Time!")


def main():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Start Quiz")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            start_quiz()

        elif choice == "2":
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()