def calculate_results(answers):
    # Basic example of scoring logic
    score = {"Introvert": 0, "Extrovert": 0}

    # Example scoring logic
    if answers[0] == "Reading":
        score["Introvert"] += 1
    else:
        score["Extrovert"] += 1

    if answers[1] == "Solo":
        score["Introvert"] += 1
    else:
        score["Extrovert"] += 1
    if answers[2] == "yes":
        score["Introvert"] += 1
    else:
        score["Extrovert"] += 1

    return score