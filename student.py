import csv

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)
#
#
# def get_name(student):
#     return student["name"]
#
#
# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")

# students = []
#


# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)
#
#
# for student in sorted(students, key=lambda student: student["house"]):
#     print(f"{student["name"]} is in {student["house"]}")

# TODO: Print student name and home using csv Reader
# students = []
#
# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         student = {"name": name, "home": home}
#         students.append(student)
#
# for student in sorted(students, key=lambda student: student["home"]):
#     print(f"{student["name"]} is from {student["home"]}")


# TODO: Print students name and home using csv DictReader
# students = []
#
# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         student = {"name": row["name"], "home": row["home"]}
#         students.append(student)
#
# for student in sorted(students, key=lambda student: student["home"]):
#     print(f"{student['name']} is from {student['home']}")

# TODO: Write students name and home in students.csv using csv writer

name = input("What's your name?: ")
home = input("What's your house?: ")
#
# with open("students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

# TODO: Write students name and home in students.csv using csv DictWriter

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
