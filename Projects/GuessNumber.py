import random

n = random.randint(1,100)
count = 0
yrnum = -1
print("welcome...")

while(yrnum != n):
    
    yrnum = int(input("Guess the number: "))
    if(yrnum > n):
        print("Enter the smaller number...")
    else:
        print("Enter the higher numbere...")
        
    count+=1
        
print(f"You have guessed number {n} successfully in {count} attempts")