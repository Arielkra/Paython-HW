'''ilan tal
312201619
work 1 py'''
print ("Q1")
''' get 5 digit number and print the sum of even and not even digit
enter 5 diget number:12345
not even: 9
even: 6
enter 5 diget number:98789
not even: 25
even: 16
enter 5 diget number: 35464
not even: 8
even: 14
'''
x=int(input("enter 5 diget number:"))
d1=x%10
d2=x%100//10 
d3=x%1000//100
d4=x%10000//1000 
d5=x//10000
sum1=int(0)
sum2=int(0)
'''if digit even add to sum2 else add to sum1'''
if x>9999 and x<100000:
    if d1%2==0:
        sum2+=d1
    else:
        sum1+=d1
    if d2%2==0:
        sum2+=d2
    else:
        sum1+=d2
    if d3%2==0:
        sum2+=d3
    else:
        sum1+=d3
    if d4%2==0:
        sum2+=d4
    else:
        sum1+=d4
    if d5%2==0:
        sum2+=d5
    else:
        sum1+=d5
    print ("not even:",sum1)
    print ("even:",sum2)
else:
    print ("not 5 digit number!!!")


print ("Q2")
''' get 4 numbers and print the max number
enter number 1:12
enter number 2:0.1
enter number 3:-1
enter number 4:4
max: 12.0
enter number 1:0.0
enter number 2:-9
enter number 3:-0.1
enter number 4:-6
max: 0.0
enter number 1:-1
enter number 2:-2
enter number 3:-3
enter number 4:-4
max: -1.0
'''
num1=float(input("enter number 1:"))
num2=float(input("enter number 2:"))
num3=float(input("enter number 3:"))
num4=float(input("enter number 4:"))
max2=float(num1)
'''if any number is bigger then sum the number is max'''
if (max2<num2):
    max2=num2
if (max2<num3):
    max2=num3
if (max2<num4):
    max2=num4
print("max:",max2)

print ("Q3")
'''get 4 digin number and chack the requerments
enter password number:0123
not 4 digit number!
not pass
enter password number:12345
not 4 digit number!
not pass
enter password number:4321
pass
enter password number:2239
same digits in the pass!
not pass
enter password number:9753
all digits are uneven!
not pass
enter password number:8642
all digits are even!
not pass
enter password number:3542
pass
'''
password=int(input("enter password number:"))
if password>999 and password<10000:
    d1=password%10
    d2=password%100//10
    d3=password%1000//100
    d4=password//1000
    sum1=d1+d2+d3+d4
    if sum1>9:
        if d1!=d2 and d1!=d3 and d1!=d4 and d2!=d3 and d2!=d4 and d3!=d4:
            if d1%2==1 or d2%2==1 or d3%2==1 or d4%2==1:
                if d1%2==0 or d2%2==0 or d3%2==0 or d4%2==0:
                    print ("pass")
                else:
                    print("all digits are uneven!\nnot pass")
            else:
                print("all digits are even!\nnot pass")
        else:
            print("same digits in the pass!\nnot pass")

    else:
        print("sum its not 2 digit number!\nnot pass")
else:
    print("not 4 digit number!\nnot pass")

print("Q4")
'''
get a grade and add points
enter grade:100
100 0 100
enter grade:96
96 4 100
enter grade:105
not a grade!
enter grade:-1
not a grade!
enter grade:0
faied no faktor
enter grade:55
55 6 61
enter grade:85
85 6 91
enter grade:86
86 4 90
enter grade:95
95 4 99
enter grade:54
faied no faktor
'''
grade=int(input("enter grade:"))
if grade>-1 and grade<101:
    if grade>95:
        print(grade,100-grade,"100")
    elif grade>85 and grade<96:
        print (grade,"4",grade+4)
    elif grade>54 and grade<86:
        print (grade,"6",grade+6)
    elif grade<55:
        print ("faied no faktor")
else:
    print("not a grade!")

print ("Q5")
'''
cheack bmi and print the bmi state
'''
height=float(input("enter height:"))
weight=float(input("enter weight:"))
bmi=weight/height**2
print ("bmi:",bmi)
if bmi>=17 and bmi<25:
    print ("תת משקל")
if bmi>=25 and bmi<30:
    print ("משקל בריא")
if bmi>=30 and bmi<35:
    print ("השמנה")
if bmi>=35 and bmi<44:
    print ("השמנת יתר")
if bmi>44:
    print ("חמורה השמנת יתר")
