'''
1.Conditional 
2.Looping 
3.Jumping
'''
def checkAge(age):
    if(age > 18):
       print("Age is greater than 18")
    else:
        print("Age is not greater than 18")
checkAge(18)

#WAP to display Child if age is below 18, display 'Adult' is age is above 18
#display Senior citizen if age is above 65

def checkTheAge(age):
    if(age < 18):
        print("Child")
    elif(age > 18 and age < 65):
          print("Adult")
    else:
        print("Senior Citizen")
checkTheAge(45)

