'''
1 for snake
-1 for water
0 for gun
'''
import random

computer=random.choice([-1,1,0])
youstr=input("Enter your choice:")
youdict={"s":1 , "w":-1 ,"g":0}
reverseDict={1:"snake",-1:"water",0:"gun"}
you=youdict[youstr]

print(f"You chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")
if(you==computer):
    print("Its a draw")

else:
    if(computer==1 and you==-1):#2
           print("You loose")

    elif(computer==1 and you==0):#1
            print('You win')

    elif(computer==-1 and you==1):#-2
            print('You win')

    elif(computer==-1 and you==0):#-1
            print('You loose')

    elif(computer==0 and you==1):#-1
            print('You loose')

    elif(computer==0 and you==-1):#1
            print('You win')

    else:
         print("Something went wrong")
                                    