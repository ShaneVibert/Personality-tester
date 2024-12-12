import tkinter as tk
from tkinter import ttk

def create_ui(root, questions, on_submit):
    answers = {}


    root.configure(bg="#d3d3d3")


    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()


    canvas = tk.Canvas(root, bg="#d3d3d3")  # Set canvas background to light grey
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#d3d3d3")  # Set scrollable frame background to light grey

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    def on_mousewheel(event):
        canvas.yview_scroll(-1 * int(event.delta / 120), "units")
    canvas.bind_all("<MouseWheel>", on_mousewheel)

    canvas.create_window((screen_width / 3.4, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")


    question_frame = tk.Frame(scrollable_frame, bg="#d3d3d3")  # Set question frame background to light grey
    question_frame.pack(padx=50, pady=10, expand=True)

    def on_answer(question_index, selected_answer, button):
        if question_index in answers:
            previous_button = answers[question_index]['button']
            previous_button.config(bg="#800000", fg="#ffffff")  # Reset the previous button color

        answers[question_index] = {'answer': selected_answer, 'button': button}

        button.config(bg="#00FF00", fg="#000000")
    for idx, question in enumerate(questions):
        question_label = tk.Label(
            question_frame, text=question["question"], font=("Arial", 14), wraplength=600, justify="center", bg="#d3d3d3"
        )
        question_label.grid(row=idx * 2, column=0, pady=(10, 5), sticky="n", padx=10)


        answer_frame = tk.Frame(question_frame, bg="#d3d3d3")
        answer_frame.grid(row=idx * 2 + 1, column=0, pady=(0, 20), sticky="n")


        for answer in question["answers"]:
            button = tk.Button(
                answer_frame, text=answer, font=("Arial", 12),
                bg="#800000",
                fg="#ffffff",
                borderwidth=3,
                relief="raised",
                highlightthickness=0.5,
                padx=20,
                pady=10,
                activebackground="#660000",
                activeforeground="white",
            )

            button.config(command=lambda q=idx, a=answer, b=button: on_answer(q, a, b))
            button.pack(side="left", padx=5)


    submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=lambda: on_submit(answers))
    submit_button.pack(pady=20, anchor="center")
















