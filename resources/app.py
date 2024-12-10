import tkinter as tk
from ui import create_ui
from questions import load_questions
from scoring import calculate_results

def main():
    root = tk.Tk()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width}x{screen_height}+0+0")

    root.title("Personality Tester")

    label = tk.Label(root, text="Welcome to the Personality Test!")
    label.pack(pady = 20)

    create_ui(root, )



    root.mainloop()
if __name__=="__main__":
    main()