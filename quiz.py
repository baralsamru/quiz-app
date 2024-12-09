import tkinter as tk
from tkinter import messagebox

# Quiz questions and answers
questions = [
    ("What does CPU stand for?", "central processing unit"),
    ("What does AWS stand for?", "amazon web services"),
    ("Which data structure uses LIFO (Last In, First Out) principle?", "stack"),
    ("What does GPU stand for?", "graphics processing unit"),
    ("What does GUI stand for?", "Graphical user interface"),
]

# Initialize score and question index
score = 0
current_question_index = 0
# Function to check the answer
def check_answer():
    global score, current_question_index
    user_answer = answer_entry.get().strip().lower()
    correct_answer = questions[current_question_index][1]
    
    if user_answer == correct_answer:
        score += 1
        messagebox.showinfo("Result", "Correct!", icon='info')
    else:
        messagebox.showinfo("Result", "Incorrect! The correct answer was: " + correct_answer, icon='warning')

    current_question_index += 1
    answer_entry.delete(0, tk.END)

    if current_question_index < len(questions):
        show_question()
    else:
        show_score()

# Function to display the current question
def show_question():
    question_label.config(text=questions[current_question_index][0])
    answer_entry.focus()

# Function to display the score at the end
def show_score():
    messagebox.showinfo("Quiz Over", f"You got {score} out of {len(questions)} questions correct!", icon='info')
    reset_quiz()

# Function to reset the quiz
def reset_quiz():
    global score, current_question_index
    score = 0
    current_question_index = 0
    show_question()

# Create the main window
root = tk.Tk()
root.title("Computer Quiz")
root.geometry("400x400")
root.configure(bg="#f0f8ff")  # Light background color
root.resizable(False, False)

# Create a frame for the quiz content
quiz_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
quiz_frame.pack(pady=20)

# Create UI elements with improved styling
question_label = tk.Label(quiz_frame, text="", wraplength=300, font=("Helvetica", 14, "bold"), bg="#ffffff")
question_label.pack(pady=10)

answer_entry = tk.Entry(quiz_frame, font=("Helvetica", 14), bd=2, relief=tk.SUNKEN)
answer_entry.pack(pady=10, padx=10, fill=tk.X)

submit_button = tk.Button(quiz_frame, text="Submit", command=check_answer, font=("Helvetica", 12), bg="#4CAF50", fg="white", relief=tk.RAISED)
submit_button.pack(pady=20)

# Start the quiz
show_question()

# Run the application
root.mainloop()
