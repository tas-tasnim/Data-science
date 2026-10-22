import math
def Decimal_to_Any(Decimal_number, Base_Number):
    if(Decimal_number != 0 and Decimal_number > 0):
        i = []
        while(Decimal_number > 0):
            a = int(Decimal_number/Base_Number)
            print(f"{Decimal_number}/{Base_Number} = {a} --> {Decimal_number%Base_Number}")
            i.append(Decimal_number % Base_Number)
            Decimal_number = a
        t = ''.join(map(str,i[::-1]))
        print(f"\nLSD -- > MSD")
        print("the result is : " , t)
    else:
        print("Wrong!!")
'''
t , a = map(int, input().split())
Decimal_to_Any(t, a)
'''
def Any_to_Decimal(Any_number, Base_Number):
    if(Any_number != 0 and Any_number > 0):
        Number_in_list = [int(x) for x in str(Any_number)]
        print(Number_in_list)
        Power = len(Number_in_list)-1
        Decimal_number = 0
        print(f"= ")
        for i in Number_in_list:
            Decimal_number += i * Base_Number**(Power)
            print(f"{i} * {Base_Number}**{(Number_in_list.index(i))}")
            Power -= 1
            if Number_in_list.index(i) == len(Number_in_list) - 1:
               break
            print("+")

        print(f"= {Decimal_number}")

while True:
    Initial_number, Base_1, Base_2 = map(int, input("Please enter your number, base and base of converted number (ex: 15 10 8): ").split())
    if (Base_1 == 10):
        Decimal_to_Any(Initial_number, Base_2)
    else:
        Any_to_Decimal(Initial_number, Base_1)


















