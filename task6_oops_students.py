#OOP based program of class student with attribute like name , roll no  and marks with 2 methods to input and display

students=[]

class student :
    def _init_(self):
        self.name=""
        self.roll=0
        self.marks=0.0

    def input_data(self):
        print("\nEnter A information of Student :")
        self.name=input("Enter a Name of Student : ")
        self.roll=int(input("Enter a Roll no. of Student :"))
        self.marks=float(input("Enter a Marks of Student :"))
        print("Student Data Stored Successfully .\n")

    def display_data(self):
        print("Student Information :")
        print(f"Name : {self.name}")
        print(f"Roll no. : {self.roll}")
        print(f"Marks : {self.marks}\n")

def main():
    student1 = student()
    while True :
        print("Choose a Option : ")
        print("1. Input Student Information ")
        print("2. Display Student Information")
        print("3. Exit")
        choice=int(input("Enter Your choice (1-3 ) :"))

        if choice==1:
            student1.input_data()
            students.append(student1)

        elif choice ==2:
            for data in students:
                data.display_data()
        
        elif choice ==3:
            print("Exiting..")
            break
        else:
            print("Invalid option , Try Again")

main()