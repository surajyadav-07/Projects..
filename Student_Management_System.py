class Student:
    count = 0

    def __init__(self,name,roll_no,marks):
        self.name = name 
        self.roll_no = roll_no
        self.marks = marks
        Student.count +=1

    def display(self):
        print("name:=" ,self.name)
        print("roll_no:=" ,self.roll_no)
        print("Marks:=",self.marks)
        print()


    def check_result(self):
        if self.marks>=40:
            print("pass")
        else:
            print("fail")


    def update_marks(self,new_marks):
        self.marks = new_marks
        print()
        print("Mark updated")

   
    def grade(self):
        if  90<=self.marks<=100:
            print("Grade A")
        elif  70<=self.marks<=89:
            print("Grade B")
        elif  50<=self.marks<=69:
            print("Grade C")
        elif  30<=self.marks<=49:
            print("Grade D")
        else:
            print("Grade F")

    def is_topper(self):
        if self.marks>=90:
            print("Topper")
        else:
            print("Not Topper")\


    def percentage(self):
        print("Percentage =",self.marks,"%")

    def total_students(self):
        print()
        print("Total Students=",Student.count)

    def search(self,roll):
        if self.roll_no == roll:
            print("Found")
            self.display()
        else:
            print("Not Found")

s1 = Student("suraj",128,95)
s2 = Student("vikash",138,85)
s3 = Student("prince",86,55)


students =[]

students.append(s1)
students.append(s2)
students.append(s3)

while True:
    print("\n--- Student management system---")
    print("1. Add student")
    print("2. Search Student")
    print("3. display all student")
    print("4. update marks")
    print("5. show_topper")
    print("6. Delete_student")
    print("7. exit")

    choice = int(input("Enter Your Choice "))

    if choice == 1:
        name = (input("Enter name "))
        roll = int(input("Enter roll_no" ))
        marks = int(input("Enter marks"))
        duplicate = False
        for i in students:
            if i.roll_no == roll:
                duplicate =True
                break
        if duplicate :
            print("Roll no already Exist")
        else:          
            new_student = Student(name,roll,marks)
            students.append(new_student)
            print(" Student added succesfuliy")

    elif choice == 2:
        Search_roll = int(input("Enter roll_no"))
        found = False
        for i in students:
            if i.roll_no == Search_roll:
                print("Student Found")
                i.display()
                found = True
            if not found:
               print("Not found")

    elif choice == 3:
        for i in students:
            i.display()

    elif choice == 4:
        roll = int(input("Enter roll_no"))
        new_marks = int(input("Enter Marks"))
        for i in students:
            if i.roll_no == roll:
               i.update_marks(new_marks)
               print("Marks Updated")
               break
            else:
               print("student not found")


    elif choice == 5:
        topper = students[0]
        for i in students:
           if i.marks>topper.marks:
            topper = i

           print("topper name =:",topper.name)
           print("topper marks =:",topper.marks)
           break


    elif choice == 6:
           roll = int(input("Enter roll_no"))

           found = False
        
           for i in students:
               if i.roll_no == roll:
                   students.remove(i)
                   found = True
                   print("student deleted ")
                
               if found == False:
                   print("student not found")
                   break

               
    elif choice == 7:
            print("Exiting...")
            break
           

    else:
        print("Invalid choice Try again")
        
