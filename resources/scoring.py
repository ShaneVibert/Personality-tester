def calculate_results(answers):
    score = {"Programmer": 0, "Not-Programmer": 0}

    # Example scoring logic
    if answers[0] == "a=5":
        score["Programmer"] += 1
    else:
        score["Not-Programmer"] += 1

    if answers[1] == "_variable":
        score["Programmer"] += 1
    else:
        score["Not-Programmer"] += 1
    if answers[2] == "to repeat a block of code":
        score["Programmer"] += 1
    else:
        score["Not-Programmer"] += 1
    if answers[3] == "13":
        score["Programmer"] += 1
    else:
        score["Not-Programmer"] += 1

    if answers[4] == "bool":
        score["Programmer"] += 1
    else:
        score["Not-Programmer"] += 1
    if answers[5] == "if statement":
        score["Programmer"] += 1
    else:
        score["Not-Programmer"] += 1
    if answers[6] == "create and initialize":
        score["Programmer"] += 1
    else:
        score["Not-Programmer"] += 1

    if answers[7] == "add to end of list":
        score["Programmer"] += 1
    else:
        score["Not-Programmer"] += 1
    if answers[8] == "binary tree":
        score["Programmer"] += 1
    else:
        score["Not-Programmer"] += 1
    if answers[9] == "Go":
        score["Programmer"] += 1
    else:
        score["Not-Programmer"] += 1

    if answers[10] == "tkinter itself":
        score["Programmer"] += 1
    else:
        score["Not-Programmer"] += 1
    if answers[11] == "CS(computer science":
        score["Programmer"] += 1
    else:
        score["Not-Programmer"] += 1


    return score