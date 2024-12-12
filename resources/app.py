import tkinter as tk
from tkinter import messagebox
from questions import load_questions
from ui import create_ui
from scoring import calculate_results

def main():
    questions = load_questions()

    def handle_submit(answers):
        if len(answers) < len(questions):
            messagebox.showwarning("Incomplete", "Please answer all the questions before submitting!")
            return

        results = calculate_results(list(answers.values()))
        result_text = f"The answer is: {max(results, key=results.get)}"
        result_label.config(text=result_text)


    root = tk.Tk()
    root.title("Are you a programmer")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width}x{screen_height}+0+0")

    create_ui(root, questions, handle_submit)

    global result_label
    result_label = tk.Label(root, text="", font=("Arial", 14), fg="green", wraplength=600, justify="center")
    result_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()