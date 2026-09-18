#eyword arguement

'''def student(name,age):
    print("Name:",name)
    print("age:",age)
student(age=20,name="Eldhos")''' 

#variable-length arguments - *args

'''def add_numbers(*numbers):
    total=0
    for number in numbers:
        total+=number
    return total
print(add_numbers(10,20))
print(add_numbers(10,20,30,40))'''

#variable-length keyword argument - **kwargs

'''def st_info(**details):
    for key,value in details.items():
        print(key,":",value)

st_info(
    name="Eldhos",
    age=23,
    course="Python"
)'''



#Scope of variable

#Lambda functions

'''square = lambda x:x*x
print(square(5))'''

#zero divison error
'''num=int(input("Enter a number:"))
print(100/num)
print("Program completed")'''

#try-Except
'''try:
    number=int(input("Enter a number:"))
    print(100/number)
except:
    print("something went wrong")'''


#handling a specific exception
'''try:
    num=int(input("Enter a number:"))
    result=100/num
    print(result)

except ZeroDivisionError:
    print("cannot divide by zero.")

except ValueError:
    print("Enter a value number.")'''

#the else block:- the else block executes only when no no exception occcurs
'''try:
    num=int(input("Enter a number:"))
    result=100/num
except ZeroDivisionError:
    print("cannot divide by zero.")
    
except ValueError:
    print("Enter a value number.")

else:
    print("Result:",result)'''

#the finally block:-the finally block executes whether an exception occurs or not
'''try:
    num=int(input("Enter a number:"))
    result=100/num
except ZeroDivisionError:
    print("cannot divide by zero.")
    
except ValueError:
    print("Enter a value number.")

else:
    print("Result:",result)

finally:
    print("Program finished")'''

#raise statement
age=int(input("Enter your age:"))

if age<18:
    raise ValueError("Age must be 18 or above")
print("Eligible")

#custom exception
'''class AgeError(Exception):
    pass
age=int(input("Enter your age:"))
if age<18:
    raise AgeError("Age must be 18 or above")
print("Eligible")'''