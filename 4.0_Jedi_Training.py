# 4.0 Jedi Training (40pts)  Name:________________
#Below each program list the mistakes found in comments.

  #1. Make the following program work. (3 mistakes)  (3pts)
     
     midichlorians = float(input("Enter midichlorian count: ")
     if midichlorians > 10000
         print("You have serious Jedi potential")
     elif:
         print("Jedi, you will never be.")
#line 6 and 9 no indentation needed while 7 and 10 only need one
#missing : on line 7
#line 9 elif statment should include elif midichlorians < 1000:

 # 2. Make the following program work. (3 mistakes)  (3pts)
     
     x = input("Enter a number: ")
     if x = 3
         print("You entered 3")


  # 3. Make the following program work. (4 mistakes)  (4pts)
     
     answer = input("What is the name of Poe Dameron's Droid? ")
     if a = "BB8":
         print("Correct!")
         else
         print("Incorrect! It is BB8.")


  # 4. Make the following program work. (4 mistakes) (4pts)
     
     x = input("Name one of the top 3 greatest Jedi.")
     if jedi == Yoda or Luke Skywalker or Obi-Wan Kenobi:
         print "That is correct!"
# when defining yoda luke skywalker or obi-wan kenobi include "" between the names
# if statement deos not work because jedi was never defined change x to jedi.
# when printing text needs to include ()

 # 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
 #    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.  (6pts)
     
     print("Welcome to the Jedi Academy!")

     print("A. Jedi Master")
     print("B. Sith Lord")
     print("C. Droid")

     user_input = input("Choose a character?")

     if user_input = A:
         sensitivity = 1000
     else if user_input = B:
         sensitivity = 900
     else if user_input = C:
         sensitivity = 0

     print("Sensitivity: ",Sensitivity)




'''
6. NUMBER ANALYSIS PROGRAM  (10pts)
-----------------------
Create a program that asks the user for a number and then analyzes it to determine if it is:
1.) odd or even
2.) positive, negative or zero
3.) inclusively between -100 and +100

A small report will then be printed. Use the following to test your program:

In: 32  
Out:  Test 1: Even
      Test 2: Positive
      Test 3: Inclusive

In: -123  
Out:  Test 1: Odd
      Test 2: Negative
      Test 3: Exclusive
'''





'''
GRADING 2.0    (10pts)
-------------------
Copy your Grading 1.0 program below and then modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''
semester_grade = float(input("Enter your semester grade:"))
final_exam = float(input("Enter you exam grade:"))
final_worth = float(input("Enter the final exam worth:"))

fworth=final_worth/100
sgworth = 1-fworth
og = fworth*final_exam+sgworth*semester_grade
if og >= 90:
    print("A")
if og >= 80:
    print("B")
if og >= 70:
    print("C")
if og >= 60:
    print("D")
if og >= 50:
    print("Transfer to Johnston!")

