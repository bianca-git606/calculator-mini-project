import math
from time import sleep
class calculator: 
    def __init__(self):
        
        print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        sleep(0.5)
        print ("+                                                                                    AA        TTTTTTTTTT    OOOOOOOO      RRRRRRR     +")
        sleep(0.5)
        print ("+    CCCCCCC          AA        LL            CCCCCCCC  UU     UU  LL               A  A           TT        OO    OO      RR    RR    +")
        sleep(0.5)
        print ("+    CC              AAAA       LL            CC        UU     UU  LL              AA  AA          TT        OO    OO      RR   RR     +")
        sleep(0.5)
        print ("+    Cc             AAAAAA      LL            CC        UU     UU  LL             AA    AA         TT        OO    OO      RRRRRRR     +")
        sleep(0.5)
        print ("+    Cc            AAAAAAAA     LL            CC        UU     UU  LL            AAAAAAAAAA        TT        OO    OO      RR   RR     +")
        sleep(0.5)
        print ("+    Cc          AAA      AAA   LL            CC        UU     UU  LL          AAA        AAA      TT        OO    OO      RR    RR    +")
        print ("+    CCCCCCC   AAAAAA    AAAAA  LLLLLLLLLLL   CCCCCCCC  UUUUUUUUU  LLLLLLLLL  AAAAAA    AAAAAA     TT        OOOOOOOO      RR     RR   +")
        sleep(0.5)
        print ("+                                                                                                                                      +")
        print ("+                                                                                                                                      +")
        sleep(0.5)
        print ("+                                                                                                                                      +")
        print ("+       type  areacircle  to calculate area of the circle                                                                              +")
        sleep(0.5)
        print ("+       type  rect to calculate area of rectangle                                                                                      +")
        print ("+       type  efficiencycalc to calculate efficiency                                                                                   +")
        sleep(0.5)
        print ("+                                                                                                                                      +")
        sleep(0.5)
        print ("+                                                                                                                                      +")
        sleep(0.5)
        print ("+                                                                                                                                      +")
        print ("+                                                                                                                                      +")
        print ("+                                                                                                                                      +")
        sleep(0.5)
        print ("+                                                                                                                                      +")
        print ("+                                                                                                                                      +")
        print ("+                                                                                                                                      +")
        print ("+                                                                                                                                      +")
        sleep(0.5)
        print ("+                                                                                                                                      +")
        print ("+                                                                                                                                      +")
        print ("+                                                                                                                                      +")
        print ("+                                                                                                                                      +")
        print ("+                                                                                                                                      +")
        print ("+                                                                                                                                      +")
        print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        self.string123 = n1=(input("enter your input"))
        
        if self.string123 =="areacircle":
                radius = float(input("enter the radius"))
                r1= radius*radius
                area = math.pi * r1
                print("the area of the circle is ",area)
        elif self.string123 == "rect":
            
                length = float(input("enter the length"))
                breath = float(input("enter the breath"))
                area = length * breath
                print("the area pf the rectange is ",area)
        elif self.string123 == "efficiencycalc":
                inputelement = float(input("enter outputelement"))
                outputelement = float(input("enter the inputelement"))
                if inputelement==0:
                    print("Invalid input element ")
                elif outputelement==0:
                    print("Invalid ouput element ")
                else:
                    e1 = (inputelement/outputelement)*100
                    print("the efficiency of this element is ",e1,"%")
     

print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
sleep(0.25)
print ("+                                                                                    AA        TTTTTTTTTT    OOOOOOOO      RRRRRRR     +")
sleep(0.25)
print ("+    CCCCCCC          AA        LL            CCCCCCCC  UU     UU  LL               A  A           TT        OO    OO      RR    RR    +")
sleep(0.25)
print ("+    CC              AAAA       LL            CC        UU     UU  LL              AA  AA          TT        OO    OO      RR   RR     +")
sleep(0.25)
print ("+    Cc             AAAAAA      LL            CC        UU     UU  LL             AA    AA         TT        OO    OO      RRRRRRR     +")
sleep(0.25)
print ("+    Cc            AAAAAAAA     LL            CC        UU     UU  LL            AAAAAAAAAA        TT        OO    OO      RR   RR     +")
sleep(0.25)
print ("+    Cc          AAA      AAA   LL            CC        UU     UU  LL          AAA        AAA      TT        OO    OO      RR    RR    +")
print ("+    CCCCCCC   AAAAAA    AAAAA  LLLLLLLLLLL   CCCCCCCC  UUUUUUUUU  LLLLLLLLL  AAAAAA    AAAAAA     TT        OOOOOOOO      RR     RR   +")
print ("+                                                                                                                                      +")
sleep(0.25)
print ("+                                                                                                                                      +")
print ("+                                                                                                                                      +")
sleep(0.25)
print ("+       press 1  to add                                                                                                                +")
print ("+       press 2  to subtract                                                                                                           +")
sleep(0.25)
print ("+       press 3  to multiply                                                                                                           +")
sleep(0.25)
print ("+       press 4  to divide                                                                                                             +")
sleep(0.25)
print ("+       press 5  for more options                                                                                                      +")
print ("+                                                                                                                                      +")
sleep(0.25)
print ("+                                                                                                                                      +")
sleep(0.25)
print ("+                                                                                                                                      +")
print ("+                                                                                                                                      +")
sleep(0.5)
print ("+                                                                                                                                      +")
print ("+                                                                                                                                      +")
print ("+                                                                                                                                      +")
sleep(0.5)
print ("+                                                                                                                                      +")
print ("+                                                                                                                                      +")
print ("+                                                                                                                                      +")
sleep(0.25)
print ("+                                                                                                                                      +")
print ("+                                                                                                                                      +")
print ("+                                                                                                                                      +")
print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

P1=int(input("Please select the input"))

if P1==1:
    n1=float(input("enter the first  no"))
    n2=float(input("enter the second no"))
    n3 = n1+n2
    print ("the sum of two numbers", n1,"and",n2, "is:-", n3)

elif P1==2:
    n1=float(input("enter the first  no"))
    n2=float(input("enter the second no"))
    n3 = subtract (n1,n2)
    print ("the difference of two numbers", n1,"and",n2, "is:-", n3)

elif P1==3:
    n1=float(input("enter the first  no"))
    n2=float(input("enter the second no"))
    n3 = n1 - n2
    print ("the product of two numbers", n1,"and",n2, "is:-", n3)

elif P1==4:
    n1=float(input("enter the first  no"))
    n2=float(input("enter the second no"))
    if n1==0:
        print("Division by ZERO")
    elif n2==0:
        print("infinity")
    else:
        n3 = n1 / n2
        n4 = n1%n2
        print ("the division of two numbers", n1,"and",n2, "is:-", n3)
        sleep(0.5)
        print ("the reminder of two numbers", n1,"and",n2, "is:-", n4)

else:
    calculator()


    
                
                
