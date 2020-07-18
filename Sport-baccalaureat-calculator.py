# First : Asking about scores in Exams!

print("Hello Friend,Now you can calculate your Result with Me!!") 

mysection = ["informative","sport","lettre","science","economy","technical","mathematics"]
print(mysection)
section = input("What's your section?,choose from list please.") 
if section == "sport" :
    Philosophy = float(input("How much do you get in philosophy?"))
    Arabic = float(input("How do you get in Arabic?"))
    English = float(input("How do you get in English?"))
    Mathematics = float(input("How do you get in Mathematics?"))
    French = float(input("How do you get in French?"))
    Physics = float(input("How do you get in physics"))
    Sport_specialization_Theoretical_Test = float(input("How do you get in Sport specialization (Theoretical Test)?"))
    Sport_specialization_Application_Test = float(input("How do you get in Sport specialization (Application Test)?")) 
    Sience = float(input("How do you get in Sience?"))
    sport = float(input("How do you get in sport?"))
    Optional = float(input("How do you get in Optional test?"))
   
    # Second : Printing Result!

    Result = (Philosophy * 1.5 + Arabic * 1.5 + English * 1.5 + Mathematics + French * 1.5 + Physics + (((Sport_specialization_Theoretical_Test + Sport_specialization_Application_Test)/2) * 3) + Sience * 3 + sport + Optional) / 16

    print("Your Result is" , Result , "!")

    # Finally : Check if the student has passed the test succefully!

    if Result >= 10  and Result < 13:
        print("Congratulations!!!You passed the test with a good Mark!")
    elif Result >= 13 :     
        print("Congratulations!!!You passed the test with an Excillent Mark!,you win an award!!!")
    else :
        print("Sorry, you did not get the required mark!")
else :
    print("Sorry,this is for Sport, you can go to another link!")

