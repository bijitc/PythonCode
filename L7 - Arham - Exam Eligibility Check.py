# Take input for the student that he can attend the exam or not
medical_cause = input("Did you have a medical cause? (Y/N): ").strip().upper()

# outer if
if medical_cause == 'Y':   # Condition 1
    print("You are allowed")
else:
    # Take input of the attendance
    attendance = int(input("Enter the attendance of the student: "))

    if attendance >= 75: # nested/inner if 
        print("Allowed")
    else:
        print("Not allowed")
