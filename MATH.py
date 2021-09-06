import operator
import random
import time
print("hi your in a quiz your goal is to get as much question right, ok ok start!")
score = 0
for i in range(0,10):
    time.sleep(0.71) 
    num1 = random.randint(0,10)
    num2 = random.randint(1,10)
    some ={"+":operator.add,"-":operator.sub,"*":operator.mul}
    w = random.choice(list(some.keys()))
    q = some.get(w)(num1,num2)
    a = input("what's {}{}{} ".format(num1,w,num2)
    )
    try:
        int(a)
    except:

        break
    if int(a) == q:
        score = score + 1
        if score != 10:
            print("right!")
        elif score == 10:
            print("congrats you have won")
        continue
    else:
        if score >= 5:
            time.sleep(0.51) 
            print("{}! impresive you should try harder next time".format(score))
            break
        elif score < 5:
            time.sleep(0.51) 
            print("{}! wow you should try harder next time".format(score))
        break
   

        