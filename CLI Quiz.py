# Console-based Quiz Program

def quiz_game():
    
    questions = [
        "1. Who painted the Mona Lisa?",
        "2. How many days are there in a week?",
        "3. What is 5 * 6?",
        "4. Who developed the theory of relativity?",
        "5. Which planet is known as the Red Planet?"
    ]
    
    options = [
        ["A. Pablo Picasso", "B. Leanardo da Vinci", "C. Michelangelo", "D. Vincent Van Gogh"],
        ["A. 12", "B. 6", "C. 7", "D. 30"],
        ["A. 30", "B. 56", "C. 60", "D. 26"],
        ["A. Newton", "B. Einstein", "C. Galileo", "D. Tesla"],
        ["A. Venus", "B. Jupiter", "C. Mars", "D. Saturn"]
    ]
    
    answers = ["B", "C", "A", "B", "C"]  # Correct answers
    
    score = 0
    
    # Loop through questions
    for i in range(len(questions)):
        print("\n" + questions[i])
        for option in options[i]:
            print(option)
        
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if user_answer == answers[i]:
            print(" Correct!")
            score += 1
        else:
            print(f" Wrong! The correct answer was {answers[i]}.")
    
    # Final score
    print("\n Quiz Finished!")
    print(f"Your final score is: {score} / {len(questions)}")


# Run the quiz
if __name__ == "__main__":
    quiz_game()
