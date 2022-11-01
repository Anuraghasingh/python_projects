
print("enter the number and operator in any order")
a=input()
b=input()
c=input()
m=None
num1=None
sign=None
num2=None 
count=0


def check():
    r=None
    for x in range(3):
        global count
        global m
        global sign
      
       
        if x==0:
            m=a
        elif x==1:
            m=b
        elif x==2:
            m=c
        if m=="*" or m=="/"or m=="+" or m=="-":
            count=count+1
            if x==0:
                r=0
            elif x==1:
                r=1
            elif x==2:
                r=2
            sign=m
    return r





def check2():
    final=False
    x=check()
    i=0
    global num1
    global num2
    while(count==1 and i<3):
        
        if x==0:
                num1=int(b)
                num2=int(c)
                final=True
        elif x==1:
               num1=int(a)
               num2=int(c)
               final=True
        elif x==2:
               num1=int(a)
               num2=int(b)
               final=True
        i=i+1
    return final



checker=check2()
if checker==True :
   
    if sign=="*":
        print("product of",num1,"and" ,num2, "is",num1*num2)
    elif sign=="+":
        print("addition of",num1,"and" ,num2, "is",num1+num2)
    elif sign=="-":
        print("subtraction of",num1,"and" ,num2, "is",num1-num2)
    elif sign=="/":
        print("subtraction of",num1,"and" ,num2, "is",num1/num2)
else:
    print("you are entering a wrong input")


