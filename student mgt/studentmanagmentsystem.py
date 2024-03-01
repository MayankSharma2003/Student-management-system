import mysql.connector
import pandas as pd

dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="",
  database = "studentmanagmentsystem"
)

cursor = dataBase.cursor()

class  Student:
    def setDetails(self, name, id):
        self.name=name
        self.id=id

    def printDetails(self):
        print(self.name, self.id)

    def access(self):
         print("\n1. BSc")
         print("2. BCom ")
         print("3. BBA ")
         print("4. BCA")
         print("5. Exit")
         choice = int(input("Choose the new course : "))
         val=None
         match choice:
            case 1:
                val="BSc"       
            case 2:
                val="BCom"
            case 3:
                val="BBA"
            case 4:
                val="BCA"
            case 5:
                 return
            case default:
                 print("Invalid Choice")
                 self.access()
         query = "UPDATE STUDENT SET Course=%s where stud=%s"
         value = (val,self.id)
         cursor.execute(query,value)
         dataBase.commit()
         print("Course updated succesfully")

             
    def viewGrades(self):
        query = f"SELECT * FROM STUDENT where stud = {self.id}"
        cursor.execute(query)
        myresult = cursor.fetchall()  
        # df  = pd.DataFrame(columns=myresult)
        print(myresult)

    def updateContactInfo(self):
        print("\n1. Update Phone Number")
        print("2. Update email")
        print("3. Exit")
        choice = int(input("Choose the feild : "))
        val=None
        match choice:
            case 1:
                val=int(input("Enter New phone number : "))
            case 2:
                val=input("Enter new email : ")
            case 3:
                 return
            case default:
                print("Invalid choice")
                self.updateContactInfo()
        if type(val)==type(123456) and len(str(val))==10:
            query = "UPDATE STUDENT SET contactnumber=%s where stud=%s"
        else:
            query = "UPDATE STUDENT SET email=%s where stud=%s"
        value = (val,self.id)
        cursor.execute(query,value)
        dataBase.commit()
        if type(val)==type(123456) and len(str(val))==10:
            print("Phone number has been changed successfully.")
        else:
            print("Email has been changed successfully.")

name = input("Enter your name : ")
id = input ("Enter your id :") 

student = Student()
student.setDetails(name,id)
student.printDetails()


while(1):
    print("\n1. Change your course ")
    print("2. View your grades ")
    print("3. Update your contact information ")
    print("4. Exit")
    choice = int(input("Enter the choice : "))
    match choice:
        case 1:
            student.access()
        case 2:
            student.viewGrades()
        case 3:
            student.updateContactInfo()
        case 4:
            exit()
        case default:
            print("Invalid Choice")
    