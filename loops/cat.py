# i = 0

# while i < 5 :
#     print("meow")
#     i += 1

# for _ in range(3):
#     print("meow")

# while True:
#     n = int(input("Enter value of n: "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")

# def main():
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         n = int(input("Enter value of n: "))
#         if n > 0:
#             break
#     return n

# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()

# students = ["abaa", "dabba", "jabba"]

# for student in students:
#     print(student)

# students = ["abaa", "dabba", "jabba"]

# for i in range(len(students)):
#     print(i + 1, students[i])

# students = {
#     "shiva": "God",
#     "Vishnu": "God",
#     "Brahma": "God",
#     "Tadkasur": "Devil"
# }

# for student in students:
#     print(student, students[student], sep=", ")

students = [
    { "name": "shiva", "house":"God", "weapon":"trishul"},
    { "name": "vishnu", "house":"God", "weapon":"chakra"},
    { "name": "brahma", "house":"God", "weapon":"fourbrains"},
    { "name": "tadkasur", "house":"Devil", "weapon":None },
]

for student in students:
    print(student["name"], student["house"], student["weapon"], sep=", ")

