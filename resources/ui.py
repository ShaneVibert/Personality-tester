import tkinter as tk

def create_ui(root, questions):
    question_index = 0
    answers = []

    def on_answer(selected_answer):
        nonlocal question_index
        answers.append(selected_answer)

        question_index += 1
        if question_index < len(questions):
            update_question()
        else:
            show_results()

    def update_question():
        question = questions[question_index]
        question_label.config(text=question["question"])

        for i, answer in enumerate(question["answers"]):
            answer_buttons[i].config(text=answer)

    def show_results():
        from scoring import calculate_results
        results = calculate_results(answers)
        result_text = f"Your personality type is: {max(results, key=results.get)}"
        result_label.config(text=result_text)


    question_label = tk.Label(root, text="")
    question_label.pack()

    answer_buttons = []
    for i in range(4):
        button = tk.Button(root, text="", command=lambda i=i: on_answer(questions[question_index]["answers"][i]))
        button.pack()
        answer_buttons.append(button)

    result_label = tk.Label(root, text="")
    result_label.pack()

    update_question()


