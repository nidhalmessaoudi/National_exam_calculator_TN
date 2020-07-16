# First : Asking about scores in Exams!

print("Hello Friend,Now you can calculate your Result with Me!!")

Sience = float(input("How much do you get in Sience?"))
Arabic = float(input("How do you get in Arabic?"))
English = float(input("How do you get in English?"))
Mathematics = float(input("How do you get in Mathematics?"))
French = float(input("How do you get in French?"))

# Second : Printing Result!

Result = (Sience + Arabic + English + Mathematics + French)/5

print("Your Result is" , Result , "!!!")

# Finally : Check if the student has passed the test succefully!

if Result >= 15  and Result < 17:
    print("Congratulations!!!You passed the test with a good Mark!")
elif Result >= 18 :     
    print("Congratulations!!!You passed the test with an Excillent Mark!,you win an award!!!")
else :
    print("Sorry, you did not get the required mark!")



