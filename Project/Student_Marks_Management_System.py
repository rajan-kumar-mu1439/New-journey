
def calculate_result():
    s_name = input("Enter Student Name: ")

    p_mark = int(input("Python Mark: "))
    j_mark = int(input("Java Mark: "))
    m_mark = int(input("Math Mark: "))
    e_mark = int(input("English Mark: "))
    s_mark = int(input("Science Mark: "))

    # Store student details
    s_details = {
        "Name": s_name,
        "Python": p_mark,
        "Java": j_mark,
        "Math": m_mark,
        "English": e_mark,
        "Science": s_mark
    }

    # Store subject marks in a list
    marks = [
        s_details["Python"],
        s_details["Java"],
        s_details["Math"],
        s_details["English"],
        s_details["Science"]
    ]

    # Calculate total and percentage
    total = sum(marks)
    percentage = (total / 500) * 100

    # Assign grade
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
        grade = "Fail"

    # Display student result
    print("\n===== STUDENT RESULT =====")
    print("Student Name:", s_details["Name"])

    for subject in ["Python", "Java", "Math", "English", "Science"]:
        print(f"{subject}: {s_details[subject]}")

    print("Total Marks:", total, "/ 500")
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", grade)
    print("==========================")

calculate_result()
