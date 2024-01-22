'''
QUIZ MASTER PROJECT  (4pts)
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
total_questions =0
total = 0
correct = ("Correct")
incorrect = ("Incorrect")

question1 = input("where is Adventure land located? ")
total_questions += 1
if question1 == "Iowa" or question1 == "IOWA" or question1 == "IA" or question1 == "iowa":
    print(correct)
    total += 1
else:
    print(incorrect)
    total += 0

question2 = input("What is the name of Adventure land's mascot ")
total_questions += 1
if question2 == "Bernie" or question2 == "bernie" or question2 == "Bernie Bernard" or question2 == "bernie bernard":
    print(correct)
    total += 1
else:
    print(incorrect)
    total += 0

question3 = input("how tall is the Storm Chaser in feet? ")
total_questions += 1
if question3 == "260" or question3 == "260 feet" or question3 == "260ft":
    print(correct)
    total += 1
else:
    print(incorrect)
    total += 0

question4 = input("What year did Adventure land introduce there newest event Phantom Fall Fest ")
total_questions += 1
if question4 == "2022":
    print(correct)
    total += 1
else:
    print(incorrect)
    total += 0

question5 = input("What new roller coaster was built this year at Adventure land? ")
total_questions += 1
if question5 == "flying viking" or question5 == "Flying Viking" or question5 == "Flying viking":
    print(correct)
    total += 1
else:
    print(incorrect)
    total += 0

question6 = input("What year was the Monster roller coaster first open to the public? ")
total_questions += 1
if question6 == "2016":
    print(correct)
    total += 1
else:
    print(incorrect)
    total += 0

question7 = input("What year did Adventureland open? \n A: 1973 \n B: 1974 \n C: 1975 \n D: I dont know \n Enter an answer:")
total_questions += 1
if question7 == "B" or question7 == "b":
    print(correct)
    total += 1
elif question7:
    print(incorrect)
    total += 0


grade = total/total_questions * 100
if grade >= 90:
    print(grade)
    print("You got a A")
elif grade >= 80:
    print(grade)
    print("You got a B")
elif grade >= 70:
    print(grade)
    print("You got a C")
elif grade >= 60:
    print(grade)
    print("You got a D")
elif grade >= 50 or grade <= 0:
    print(grade)
    print("You got a F")




