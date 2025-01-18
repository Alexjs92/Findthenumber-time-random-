number = 30
control = 0
attempts = 1
import random 
import time
y = random.randint(0,1000)

while(control==0):
    print("Ingress the number here")
    num = int(input())
    if(num==number):
        print("congratulations you find the number with", attempts,"attempts")
        print("now, you can close this page")
        control=1

    elif(num > number):
        print("INCORRECT")
        attempts+=1
        print("you have", attempts,"attempts")
        print("try again!")

    elif(num < number):
        print("INCORRECT")
        attempts+=1
        print("you have", attempts,"attempts")
        print("try again!")

#- The best part here----
    if(num==77):
        print("console????")
        control= 1
        time.sleep(3)
        print("INGRESS THE -77")
        time.sleep(3)
        control= 0
    
    if(num==-77):
        print("INGRESS -9997 to change the number to 77")
        time.sleep(2)
        print("INGRESS -9998 to generate randoms numbers")
        time.sleep(2)
        print("you can continue")
    
    if(num==-9997):
        number = 77
        print("THE NUMBER IS CHANGED")
        print("you can continue")

    if(num==-9998):
        print(y)            #-Only can generate 1 number random