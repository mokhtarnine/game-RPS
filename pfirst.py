print("Hello guys let's go to play game ohhhh!!!")
import  random
P = random.randint(1,3)
W = 0
E = 0 
L = 0 
S = 1
TR = 0

while S != 0 :
    print("let's go to play rock paper scissors ")
    print("Pour play you should to choise R=1,P=2 or S=3 ")
    U =int(input("choise :"))
    if U == P :
        E = E + 1 
        print("you tied!!!!!")
    #****************************
    elif  U == 1 and P == 2 :
        L = L + 1
        print("you choise rock and pc choise paper .")
        print("you lost !!!!!")
    elif  U == 2 and P == 3 :
        L = L + 1
        print("you choise paper and pc choise scissors .")
        print("you lost !!!!!")
    elif  U == 3 and P == 1 :
        L = L + 1
        print("you choise scissors and pc choise rock. ")
        print("you lost !!!!!")
    #******************************
    elif  U == 2 and P == 1 :
        W = W + 1
        print("you choise paper and pc choise rock .")
        print("you win !!!!!")
    elif  U == 3 and P == 2 :
        W = W + 1
        print("you choise scissors and pc choise paper")
        print("you win !!!!!")
    elif  U == 1 and P == 3 :
        W = W + 1
        print("you choise rock and pc choise scissors")
        print("you win !!!!!")
    else :
        print("error 404 , use correct one ")
    TR += 1 
    if TR == 3 :
           S = int(input("choise 1 for contine or 0 for stop play :"))
           TR = 0 

print("you tied ",E,"time")
print("you lost ",L,"time")
print("you win ",W,"time")
  


