import random
computer = random.choice([1,0,-1])

youstr = input("Enter your choice below \n"
               "(s = snake)\n"
               "(w = water)\n"
               "(g = gun): ")
youdict = {"s":1,"w":-1,"g":0}
reversedict = {1:"snake",-1:"water",0:"gun"}

you = youdict[youstr]
print(f"Computer choose {reversedict[computer]}\nYou choose {reversedict[you]}")

if computer == you:
    print("it is draw")
    
else:
    if(computer ==1 and you==-1):
        print("you lose")
    elif(computer ==1 and you==0):
        print("you win")
    elif(computer ==0 and you==-1):
        print("you win")
    elif(computer ==0 and you==1):
        print("you lose")
    elif(computer ==-1 and you==1):
        print("you win")
    elif(computer ==-1 and you==0):
        print("you lose")
    else:
        print("something went wrong")
        