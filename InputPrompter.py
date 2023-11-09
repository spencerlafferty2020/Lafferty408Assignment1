# Spencer Lafferty
# 2378112
# lafferty@chapman.edu
# CPSC 408-01
# Assignment 1
import DatabaseInterfacer

menuPromptString = '''
Please enter a number (don't include the colon): 
1: Display all Students in students.csv
2: Add a new Student
3: Update a Student
4: Delete a Student
5: Search through Students
6: Exit
'''

queryPromptString = '''
What field would you like to search by (don't include the colon): 
1: Search by Major
2: Search by minimum GPA
3: Search by City
4: Search by State
5: Search by Advisor
6: Go back
'''

def MenuPrompt (conn):
    while True:
        try:
            userInput = int(input(menuPromptString))
            if userInput == 1:
                displayStudents(conn)
            elif userInput == 2:
                addStudent(conn)
            elif userInput == 3:
                updateStudent(conn)
            elif userInput == 4:
                deleteStudent(conn)
            elif userInput == 5:
                queryStudents(conn)
            elif userInput == 6:
                exitProgram()
            else:
                print ("Invalid input. Please enter a number between 1 and 6.")
        except ValueError:
            print ("Invalid input. Please enter a number between 1 and 6.")



def displayStudents(conn):
    DatabaseInterfacer.displayStudents(conn)

def addStudent(conn):
    DatabaseInterfacer.addStudent(conn)

def updateStudent(conn):
    DatabaseInterfacer.updateStudent(conn)

def deleteStudent(conn):
    DatabaseInterfacer.deleteStudent(conn)

def queryStudents(conn):
    while True:
        try:
            userInput = int(input(queryPromptString))
            if userInput == 1:
                queryByMajor(conn)
            elif userInput == 2:
                queryByMinGPA(conn)
            elif userInput == 3:
                queryByCity(conn)
            elif userInput == 4:
                queryByState(conn)
            elif userInput == 5:
                queryByAdvisor(conn)
            elif userInput == 6:
                print("Returning to menu")
                break
            else:
                print("Invalid input. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

# Query Functions
# Query by major won't accept a string longer than 24 characters
def queryByMajor(conn):
    prompt = "Please enter the target major: "
    while True:
        major = input(prompt)
        if 0 < len(major) < 25:
            break
        else:
            print("Invalid Input. Please enter a valid major")
    DatabaseInterfacer.queryByMajor(conn, major)

# Query by minimum GPA won't accept an input that is not a number between 0 and 4
def queryByMinGPA(conn):
    prompt = "Please enter the minimum GPA: "
    while True:
        try:
            gpa = float(input(prompt))
            if 0.0 <= gpa <= 4.0:
                break
            else:
                print("Invalid input. GPA must be between 0.0 and 4.0.")
        except ValueError:
            print("Invalid input. GPA must be a numeric value.")
    DatabaseInterfacer.queryByMinGPA(conn, gpa)

# Query by city won't accept a string longer than 24 characters
def queryByCity(conn):
    prompt = "Please enter the target city: "
    while True:
        city = input(prompt)
        if 0 < len(city) < 25:
            break
        else:
            print("Invalid Input. Please enter a valid city")
    DatabaseInterfacer.queryByCity(conn, city)

# Query by state won't accept a string longer than 24 characters
def queryByState(conn):
    prompt = "Please enter the target state: "
    while True:
        state = input(prompt)
        if 0 < len(state) < 25:
            break
        else:
            print("Invalid Input. Please enter a valid state")
    DatabaseInterfacer.queryByState(conn, state)

# Query by Advisor won't accept strings longer than 24 characters
def queryByAdvisor(conn):
    prompt = "Please enter the target advisor: "
    while True:
        advisor = input(prompt)
        if 0 < len(advisor) < 25:
            break
        else:
            print("Invalid Input. Please enter a valid advisor")
    DatabaseInterfacer.queryByAdvisor(conn, advisor)

def exitProgram():
    DatabaseInterfacer.exit()