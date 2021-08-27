# req is input fun for 4 type

def archana_calculator():
    secondChoice="y"
    while(secondChoice=="y"):
     Userchoice =input("Hey user, Please choose one of the below \n plus for addition, minus for substraction , mult for multiplication, Div for division" )
     if Userchoice=="plus":
        x=int (input("x"))
        y=int (input("y"))
        print (x+y)

     elif Userchoice=="minus":
          x=int (input ("x"))
          y=int (input ("y"))
          print (x-y)

     elif Userchoice=="mult":
          x=int (input ("x"))
          y=int (input ("y"))
          print (x*y)
     secondChoice=input("Do you want to continue=y")

     
archana_calculator()



    
 
