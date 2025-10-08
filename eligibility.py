name=input("What is your name? ")
gpa=float(input("What is your GPA? "))
hours=int(input("Total credid hours: "))
if gpa>= 3.5 and hours>=12:
    print(f"Congratulations {name} ! You have made it to the Dean's list")
else:
    print(f"You need {(3.5- gpa):.1f} more points and {12-hours} more credit hours to make it to the Dean's list")
