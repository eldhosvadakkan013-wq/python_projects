#Dictionaries:key value pairs

'''person={"name":"Eldhos","age":30}
print(person)
print(person["name"])'''

#keys:-keys mathram varaan

'''person={"name":"Eldhos","age":30}
print(person.keys())'''

#values:-values mathram varaan

'''person={"name":"Eldhos","age":30}
print(person.values())'''

#items:-ella keysum valuesum varan

'''person={"name":"Eldhos","age":30}
print(person.items())'''

#get
'''person={"name":"Eldhos","age":23}
print(person.get("name"))
print(person.get("city"))
print(person.get("city","not found"))'''

#pop:-key kalanjit athinte values mathram edukan
'''person={"name":"Eldhos","age":30}
age=person.pop("age")
print(age)
print(person)'''

#update:-values update aakan.2 dictionary venam ivade

'''person={"name":"Eldhos","age":23}
person.update({"city":"delhi","age":18})
print(person)'''





#sets:Unique items only
numbers={1,2,3,2,4}
#print(numbers)
'''print(numbers.add(50)) #add cheyaan
print(numbers)'''

#update
'''s={1,3}
s.update([2,3,4])
print(s)

#remove
s.remove(3)
print(s)

#discard
s.discard(3)
print(s)

#clear
s.clear()
print(s)'''

#Union
'''a={1,2,3}
b={3,4,5}
print(a|b)'''

#intersection
'''a={1,2,3}
b={3,4,5}
print(a&b)'''

#difference
'''a={1,2,3}
b={3,4,5}
print(a-b)'''

#symmetric_difference
'''a={1,2,3}
b={2,3,4}
print(a.symmetric_difference(b))'''




#functions
'''def greet():
    print("Hello,Welcome to python")
greet()'''

#function with parameters
'''def greet(name):
    print("Hello",name) #name is parameters

greet("Eldhos")'''

#multiple parameters
'''def add(a,b):
    print(a+b)
add(10,20)'''

'''def student_info(name,age,course):
    print("Name:",name)
    print("Age:",age)
    print("course:",course)

student_info("Eldhos",20,"Python")'''

#return statement
'''def add(a,b):
    return a+b
result=add(10,20)
print(result)'''
