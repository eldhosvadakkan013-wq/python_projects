age=int(input("Enter age:"))
citizen=input("Are you an indian citizen?(yes/no):")

if age>=18:

    if citizen.lower()=="yes":
        print("Eligible to Vote")
    else:
        print("Not Eligible to Vote")

else:print("Not Eligible")