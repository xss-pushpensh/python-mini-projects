
print("===== Student Grade Calculator =====")

name = input("Enter student name: ")
subjects = int(input("Enter number of subjects: "))

if subjects <= 0:
    print("Number of subjects must be positive.")
    raise SystemExit

total = 0
valid = True

for i in range(1, subjects + 1):
    marks = float(input(f"Enter marks for subject {i} (0-100): "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Enter a value from 0 to 100.")
        valid = False
        break

    total += marks

if valid:
    percentage = total / subjects

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    print("\n===== Result =====")
    print("Student:", name)
    print("Total Marks:", total, "/", subjects * 100)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
