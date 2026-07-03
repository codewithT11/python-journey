# Student Record System

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
favorite_language = input("Enter your favorite language: ")
student_record = { "Name":name, "Age":age, "City":city, "Favorite Language":favorite_language}
line = "-" * 6
print(line, "Student Record", line)
for key, value in student_record.items():
    print(f"{key}:{value}")
print("-" * 28)