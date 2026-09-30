#1. Check whether a number is even or odd.
'''number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is a even number.")
else:
    print(number, "is an odd number.")'''


#2.Find the largest of three numbers.
'''num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))
if num1 >=num2 and num1 >= num3:
    print(num1,"is the largest number.")
elif num2 >=num1 and num2 >=num3:
    print(num2,"is the largest number.")
else:
    print(num3,"is the largest number.")'''

#3.Calculate factorial of a number
'''num=int(input("Enter the number:"))
fact = 1
for e in range(1,num+1):  
    fact=fact*e
print("The factorial of",num,"is",fact)'''

#Check whether a number is prime
'''num=int(input("Enter a number:"))
if num<=1:
    print(num,"Not prime number")
else:
    prime=True
    for i in range(2,num):
        if num%i==0:
            prime=False
            break
    if prime:
        print(num,"is a prime number.")
    else:
        print(num,"is not a prime number.")'''

#Reverse a string
'''string=input("Enter a string:")
reverse=string[::-1]
print("Reversed string is :",reverse)'''

#Count vowels in a string.
'''word= input("Enter a word: ")
count =0
for i in word:
    if i in 'aeiouAEIOU':
         count +=1
print("Number of vowels in the word is:",count)'''

#Find the largest element in a list.
'''num=[10, 20, 4, 45, 99]
largest=num[0]
for i in num:
    if i>largest:
        largest=i
print("Largest element is:",largest)'''

#Remove duplicate values from a list
'''numbers = [1, 2, 3, 2, 4, 1, 5]
number = []
for n in numbers:
    if n not in number:
        number.append(n)
print("orderd number of list is:", number)'''

#Read data from a text file
'''file=open("message.txt","r")
data=file.read()
print(data)'''

#Create a Python function to calculate the average of a list
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers) 
    return average

numbers = [10, 20, 30, 40, 50]
result = calculate_average(numbers)
print("Average:",result)