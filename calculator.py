'''def add(a,b):
    return a+b
def multiply(a,b):
    return a*b'''

def calculate_grade(marks):
    if marks >= 90:
        return "Grade A+"
    elif marks >= 85:
        return "Grade A"
    elif marks >= 80:
        return "Grade B+"
    elif marks >= 75:
        return "Grade B"
    elif marks >= 70:
        return "Grade C+"
    elif marks >= 65:
        return "Grade C"
    elif marks >= 55:
        return "Grade D+"
    else:
        return "You Failed"

