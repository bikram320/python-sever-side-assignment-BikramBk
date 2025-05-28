#Program to take a list of student names and stores them in file
#then read and display the contents

noOfStudent= int(input("\nEnter a number of Student : "))

studentNames = []

for student in range( noOfStudent):
    studentName = input("Enter a Name of Student : ")
    studentNames.append(studentName)

with open("student.txt","w") as file :
    file.write("{:<15}\n".format("Student Name"))
    for name in studentNames:
        file.write("{:<15}\n".format(name))
    print("Successfully Written into file")

with open("student.txt","r") as file :
    content = file.read()
    print("\n"+content)
    print("Successfully Read from file")

