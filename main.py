'''import calculator
print(calculator.add(5, 3))
print(calculator.multiply(5, 3))'''

'''from calculator import add
print(add(5, 3))'''


#Functions:Student Grade Calculator
'''import calculator
marks=float(input("Enter your marks:"))
print(calculator.calculate_grade(marks))'''

#List:Find Largest Number in List
'''numbers = [5, 10, 2, 8, 3]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print("The largest number is:", largest)'''

#calculate average marks
'''marks = [85, 98, 78, 92, 88]
average = sum(marks) / len(marks)
print("average mark:-", average)'''



#search an item in list
'''fruits = ["apple", "banana", "orange", "grape"]
search_item = input("Enter a fruit to search: ")
#print(search_item in fruits) true or false
if search_item in fruits:
    print(search_item, "is found in the list.")
else:
    print(search_item, "is not found in the list.")'''

#dictionaries:-
     #student information system
'''students={"name":"Eldhos","age":23,"cource":"Generative AI"}
#print(students.keys())
#print(students.values())
#print(students.items())'''

    #Dictionary search
'''students={
    1:"Eldhos",
    2:"Thasneem",
    3:"Ashiq",
    4:"Neena",
    5:"Ancy",
    6:"Sreelakshmi",
    7:"Adwaith",
    8:"Vaibhav"
}
search = int(input("Enter your Roll number: "))
if search in students:
    print(students[search])
else:
    print("Student not found.")'''

#Exception Handling:-
    #safe division program 
'''try:
    number=int(input("Enter a number:"))
    result=150/number
    print(result)
except ZeroDivisionError:
    print("cannot divide by zero.")
except ValueError:
    print("please enter a valid number.")'''

    #safe age validation
 
'''age = int(input("Enter your age: "))

if age<18:
    raise ValueError("Age must be 18 or older.Sorry, you are not eligible to vote.")
print("You are eligible to vote!")'''

#safe list access

'''numbers = [10, 20, 30, 40, 50]
try:
    num=int(input("Enter your number:"))
    print (numbers[num])
except IndexError:
    print("please enter a valid number.")'''

#Write Student Names to File
'''with open("student_names.txt", "w") as file:
     file.write("Eldhos"+"\n")
     file.write("Thasneem"+"\n")
     file.write("Ashiq"+"\n")

print("File saved successfully")'''

#read file contents
'''with open("student_names.txt", "r") as file:
    data=file.read()
    print(data)'''

#Append new student
'''name=["Ashiq","Thasneem","Eldhos"]
name.append("Neena")
print(name)'''

#search student in file












