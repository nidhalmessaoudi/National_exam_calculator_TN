# First : Asking about scores in Exams!

print("Hello Friend,Now you can calculate your Result with Me!!") 

mysection = ["informative","sport","lettre","science","economy","technical","mathematics"]
print(mysection)
section = input("What's your section?,choose from list please.") 
if section == "technical" :
    Philosophy = float(input("How much do you get in philosophy?"))
    Arabic = float(input("How do you get in Arabic?"))
    English = float(input("How do you get in English?"))
    Mathematics = float(input("How do you get in Mathematics?"))
    French = float(input("How do you get in French?"))
    Physics = float(input("How do you get in physics"))
    Technical_writen_test = float(input("How do you get in Technical Test (Written)"))
    Technical_application_test = float(input("How do you get in Technical Test (Application)"))
    Informative_written_test = float(input("How do you get in Informative (Written Test)?"))
    Informative_application_test = float(input("How do you get in Informative (Application Test)?")) 
    Sience = float(input("How do you get in Sience?"))
    sport = float(input("How do you get in sport?"))
    Optional = float(input("How do you get in Optional test?"))
   
    # Second : Printing Result!

    Result = (Philosophy * 1 + Arabic * 1 + English * 1 + Mathematics * 3 + French * 1 + Physics * 3 + (Informative_written_test + Informative_application_test/2) + ((Technical_writen_test + Technical_application_test) / 2 ) * 4 + Sience * 1 + sport + Optional) / 17

    print("Your Result is" , Result , "!")

    # Finally : Check if the student has passed the test succefully!

    if Result >= 10  and Result < 13:
        print("Congratulations!!!You passed the test with a good Mark!")
    elif Result >= 13 :     
        print("Congratulations!!!You passed the test with an Excillent Mark!,you win an award!!!")
    else :
        print("Sorry, you did not get the required mark!")
else :
    print("Sorry,this is for Technical, you can go to another link!")