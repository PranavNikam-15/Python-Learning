# Write a grading program: 
# marks >= 90 (Grade A), >= 75 (Grade B), >= 50 (Grade C), else (Fail).


marks = int(input("Enter student marks (0-100): "))

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")
    
else:
    print("Fail")