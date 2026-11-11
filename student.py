def display_student():
    name = "Sanjay"
    roll_no = 9
    print("student Name:",name)
    print("Roll Number:",roll_no)
display_student()
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"
display_student()
print("Grade:",calculate_grade(int(input("enter marks\t"))))

