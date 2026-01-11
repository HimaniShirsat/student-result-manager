# student result manager
# Created by: Himani Shirsat 
# Description: A beginner project to calculate student grades. 

print("Welcome to student Result Manager")

Name = input("Enter student Name ?")
print(Name)
mark1 = float(input("mark 1:"))
print(mark1)
mark2 = float(input("mark 2:"))
print(mark2)
mark3 = float(input("mark 3"))
print(mark3)

total = mark1 + mark2 + mark3 
print(total)
average = total / 3
print(average)

if average >= 70:
    print("grade Distinction")
elif average >= 60:
    print("grade Merit")
elif average >= 50:
    print("grade pass")
else:
    print("grade fail")
    