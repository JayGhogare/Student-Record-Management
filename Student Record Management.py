students = {}
while True:
    print("====== Student Record Management ======")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")
    Choice = input("Enter your Choice:")
    if Choice == "1":
        def add_student():
            student = input("Enter student name:")
            marks = int(input("Enter marks:"))
            students[student] = marks
            print("student added Succesfully!!")
        add_student() 
    elif Choice == "2":
        def view_student():
            if not students:
                print("Student not available")
            else:
                print("==== Student ====")
        view_student()
        for student in students:
            print(student, ":", students[student])
    elif Choice == "3":
        def search_student():
            search = input("Enter student name:")
            if search in students:
                print("✅ Student found" )
                print("marks:", students[search])
            else:
                print("❌ Student not found")           
        search_student()
    elif Choice == "4":
        def update_marks():
            student = input("Enter student name:")
            if student in students:
                new_marks = int(input("Enter new marks:"))
                students[student] = new_marks
                print("✅ Marks updated sucessfully!!")
            else:
                print("❌ Student not found")
        update_marks()
    elif Choice == "5":
        def delete_student():
            student = input("Search student name:")  
            if student in students:
                del students["student"]
                print("✅ Student deleted sucessfully!!")
            else:
                print("❌ Student not found") 
        delete_student()
    elif Choice == "6":
        print(" 🙏Thank you for using Student Record Management System!")
        break