import matplotlib.pyplot as plt  # Importing for graph plotting

# Function to display a single question and its options
def display_question(question, options):
    print("\n" + question)  # Print the question
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")  # Display options with numbers

# Function to plot the performance graph
def plot_performance(correct, incorrect, unanswered):
    labels = ['Correct', 'Incorrect', 'Unanswered']
    counts = [correct, incorrect, unanswered]
    colors = ['green', 'red', 'gray']

    # Plot a bar graph
    plt.figure(figsize=(8, 6))
    plt.bar(labels, counts, color=colors)
    plt.title("MCQ Examination Performance")
    plt.ylabel("Number of Questions")
    plt.show()

# Main program logic starts here
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "Madrid", "Rome"],
        "answer": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": 2
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["Charles Dickens", "William Shakespeare", "J.K. Rowling", "Mark Twain"],
        "answer": 2
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": 4
    },
    {
        "question": "What is the speed of light?",
        "options": ["3 × 10^8 m/s", "3 × 10^6 m/s", "3 × 10^5 m/s", "3 × 10^4 m/s"],
        "answer": 1
    }
]

# Initialize variables
score = 0
correct = 0
incorrect = 0
unanswered = 0

print("Welcome to the MCQ Examination Portal!\n")  # Welcome message

# Loop through each question
for i, q in enumerate(questions, start=1):
    display_question(q["question"], q["options"])  # Show the question and options
    try:
        user_answer = input("Enter your choice (1-4 or press Enter to skip): ").strip()
        if user_answer == "":  # User skipped the question
            unanswered += 1
            print("You skipped this question.")
        elif int(user_answer) == q["answer"]:  # Correct answer
            score += 1
            correct += 1
            print("Correct!")
        else:  # Incorrect answer
            incorrect += 1
            print("Incorrect!")
    except ValueError:  # Handle invalid inputs
        unanswered += 1
        print("Invalid input. Skipping this question.")

# Results calculation
total_questions = len(questions)
percentage = (score / total_questions) * 100

# Display results
print("\nExamination Complete!")
print(f"Total Questions: {total_questions}")
print(f"Correct Answers: {correct}")
print(f"Incorrect Answers: {incorrect}")
print(f"Unanswered Questions: {unanswered}")
print(f"Your Score: {score}/{total_questions} ({percentage:.2f}%)")

# Ask if the user wants to see the graph
plot = input("Do you want to see your performance graph? (yes/no): ").strip().lower()
if plot == "yes":
    plot_performance(correct, incorrect, unanswered)
