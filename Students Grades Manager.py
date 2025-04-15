def menu():
    print("\n1. Add a student")
    print("2. View all students and grades")
    print("3. View each student average grade")
    print("4. Show all students with an average grade higher than 14")
    print("5. Quit")

def add():
    name = input("Student's name: ")
    grades = input("Student's grades separated by commas (ex.: 15, 17, 14): ") 
    with open("grades.txt", "a") as f:
        f.write(f"{name}: {grades}\n")
        print("Student added sucessfully")

def view_all():
    try:
        with open("grades.txt", "r") as f:
            print("\nStudent's list:")
            print (f.read())

    except FileNotFoundError:
        print("You have not registered any students yet") 

def view_average():
    try:
        with open("grades.txt", "r") as f:
            for line in f:
                name, grades = line.strip().split(":")
                grades_list = [int(n) for n in grades.split(",")]  
                average = sum(grades_list) / len(grades_list) 
                print(f"{name.strip()} - Average: {average:.2f}")  

    except:
        print("Error")    


def higher_than_14():
    try:
        with open("grades.txt", "r") as f:
            print ("Students who have an average grade higher than 14: ")
            for line in f:
                name, grades = line.strip().split(":")
                grades_list = [int(n) for n in grades.split(",")]  
                average = sum(grades_list) / len(grades_list) 
                if average > 14:
                    print(f"{name.strip()} - Average: {average:.2f}")
    except:
        print("Error")

while True:
    menu()
    option = input("Choose an option: ") 

    if option == "1":
        add()
    
    elif option == "2":  
        view_all()
    
    elif option == "3":   
        view_average()
    
    elif option == "4": 
        higher_than_14()
    elif option == "5":
        break 
    else:
        print("Invalid option.") 
                       
              
        