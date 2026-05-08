import numpy as np

def calculate_result(math, science, english):

    marks = np.array([math, science, english])

    total = np.sum(marks)
    average = np.mean(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    else:
        grade = "C"

    return total, round(average, 2), grade