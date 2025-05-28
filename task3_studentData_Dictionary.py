#write a program to enter  a student data and store it in a dictionary 
#and also provide a menu to add , search and display student
students={}
#function to add student
def add_student():
    print("\n")
    roll = int(input("Enter a Roll no. : "))
    if roll in students :
        print("Roll no. Already Exist ")

    else:
        name = input("Enter a name : ")
        marks = input("Enter a marks : ")
        contact = input("Enter a Contact number : ")

        students[roll]={
            'name':name,
            'marks':marks,
            'contact':contact
        }
        print("Student Data Added Successfully ")
        print("\n")

#function to search student based on roll no.
def search_student():
    print("\n")
    roll = int(input("Enter Roll no :"))
    if roll in students :
        print(f"Roll no : {roll}")
        print(f"Name : {students[roll]['name']}")
        print(f"Name : {students[roll]['marks']}")
        print(f"Name : {students[roll]['contact']}")
    else:
        print("Student Doesn't Exist")
        
    print("\n")

#function to display Student Record
def display_students():
    print("\n")
    if not students:
        print("No student data available.\n")
    else:
        print("\nAll Students:")
        for roll, info in students.items():
            print(f"Roll Number: {roll}")
            print(f"Name   : {info['name']}")
            print(f"Age    : {info['marks']}")
            print(f"Course : {info['contact']}")
        print("\n")

def main():

    while True:
    
        print("=== Student Management Menu ===")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            display_students()
        elif choice == '4':
             print("Exiting program. Goodbye!")
             break
        else:
            print("Invalid choice! Please try again.\n")
        

#calling main method
main()

 

