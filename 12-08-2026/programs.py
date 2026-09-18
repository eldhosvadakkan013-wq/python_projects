#file handling in python
    

     #*reading file/(traditional approach)

'''file = open("C:/Users/ELDHOS VADAKKAN/OneDrive/Documents/file handling.txt","r")
content=file.read()
print(content)
file.close()'''

     #*reading file/(Recommended approach)
    
'''with open("message.txt","r") as file:
    data=file.read()
    print(data)'''
    
    #Reading line by line

'''file = open("C:/Users/ELDHOS VADAKKAN/OneDrive/Documents/file handling.txt","r")
line=file.readlines()
print(line)
file.close()'''

     #Reading using a loop

'''file=open("C:/Users/ELDHOS VADAKKAN/OneDrive/Documents/file handling.txt","r")
for line in file:
    print(line.strip())
file.close()'''

    #writing to file

'''file=open("message.txt","w")
file.write("Welcome to python!")
file.close()'''

#writing user input to a file
name=input("Enter your name:")
with open("message.txt","a") as file:
    file.write(name +"\n")
print("student saved successfully!")
