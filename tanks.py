import random
import time
x = random.randint(1,10)
y = random.randint(1,10)
z = random.randint(1,10)
c = random.randint(1,10)
b = random.randint(1,10)
a = random.randint(1,10)
qwerty = ''
asdf = ''
attack = ''
start = ''
while not start  == 'y':
    start=input("Ready to start? (y/n) ")
name = input("What is your name?")

print("Hello captain "+ name )
time.sleep(2)
print("The General wants to tell you someting")
time.sleep(2)
print("Hello, Captain " + name + ".This is the General. You must be the new Tank Driver .")
time.sleep(2)
if x <= 1:
   
    while not asdf  == 'y':
        asdf=input("Ready to go on a mission? (y/n) ")
    while not attack  == 'y':
        attack=input("Ready to Attack? (y/n) ")
    if a <= 4:
        print("You Won the battle")
    else:
        print("You Lost the battle")
    
   
else :
    print("You have been promoted to Commander" )
    
     
    while not asdf  == 'y':
        asdf=input("Ready to go on a mission? (y/n) ")
    while not attack  == 'y':
        attatck=input("Ready to Attack? (y/n) ")
    if a <= 4:
        print("You Won the battle")
    else:
        print("You Lost the battle")
    