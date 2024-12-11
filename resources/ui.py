import tkinter as tk
from tkinter import ttk

def create_ui(root, questions, on_submit):
    answers = {}  # Store the selected answer for each question

    # Set the background color of the root window to light grey
    root.configure(bg="#d3d3d3")  # Light grey background

    # Get screen width and height for dynamic window size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set up the scrollable frame
    canvas = tk.Canvas(root, bg="#d3d3d3")  # Set canvas background to light grey
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#d3d3d3")  # Set scrollable frame background to light grey

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Position the scrollable frame
    canvas.create_window((screen_width / 2.9, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Frame to hold questions and answers
    question_frame = tk.Frame(scrollable_frame, bg="#d3d3d3")  # Set question frame background to light grey
    question_frame.pack(padx=50, pady=10, expand=True)

    def on_answer(question_index, selected_answer, button):
        # If the user is changing their answer, reset the previous one
        if question_index in answers:
            previous_button = answers[question_index]['button']
            previous_button.config(bg="#800000", fg="#ffffff")  # Reset the previous button color

        # Update the answer for the current question
        answers[question_index] = {'answer': selected_answer, 'button': button}

        # Change the button's background to bright green after selection
        button.config(bg="#00FF00", fg="#000000")  # Bright green background and black text

    # Loop through all questions
    for idx, question in enumerate(questions):
        # Create question label with light grey background
        question_label = tk.Label(
            question_frame, text=question["question"], font=("Arial", 14), wraplength=600, justify="center", bg="#d3d3d3"
        )
        question_label.grid(row=idx * 2, column=0, pady=(10, 5), sticky="n", padx=10)

        # Create frame for answer buttons with light grey background
        answer_frame = tk.Frame(question_frame, bg="#d3d3d3")
        answer_frame.grid(row=idx * 2 + 1, column=0, pady=(0, 20), sticky="n")

        # Create answer buttons (slightly beveled style with maroon background)
        for answer in question["answers"]:
            button = tk.Button(
                answer_frame, text=answer, font=("Arial", 12),
                bg="#800000",  # Dark maroon background
                fg="#ffffff",  # White text
                borderwidth=3,  # Slightly thicker border for the beveled effect
                relief="raised",  # Raised relief to give a subtle 3D effect
                highlightthickness=0.5,  # Thin highlight border
                padx=20,  # Horizontal padding for the button's shape
                pady=10,  # Vertical padding for the button's shape
                activebackground="#660000",  # Darker maroon when pressed
                activeforeground="white",  # White text when pressed
            )
            # Bind the lambda with the button reference after it is created
            button.config(command=lambda q=idx, a=answer, b=button: on_answer(q, a, b))
            button.pack(side="left", padx=5)  # Pack buttons horizontally with padding

    # Submit button at the bottom, placed outside the loop
    submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=lambda: on_submit(answers))
    submit_button.pack(pady=20, anchor="center")
















