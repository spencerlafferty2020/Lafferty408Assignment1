# Spencer Lafferty
# 2378112
# lafferty@chapman.edu
# CPSC 408-01
# Assignment 1

import sqlite3
import csv

def displayStudents(conn):
    mycursor = conn.cursor()
    mycursor.execute ("SELECT * FROM Students WHERE isDeleted = 0")
    result = mycursor.fetchall()
    for x in result:
        print(x)

    mycursor.close()

def addStudent(conn):
    mycursor = conn.cursor()

    # Prompt user for student information
    while True:
        firstName = input("Enter the student's first name: ")
        if firstName.isalpha() and len(firstName) > 0:
            break
        else:
            print("Invalid input. Please enter a valid first name.\n")
    while True:
        lastName = input("Enter the student's last name: ")
        if lastName.isalpha() and len(lastName) > 0:
            break
        else:
            print("Invalid input. Please enter a valid last name.")
    while True:
        try:
            gpa = float(input("Enter the student GPA: "))
            if 0.0 <= gpa <= 4.0:
                break
            else:
                print("Invalid input. GPA must be between 0.0 and 4.0.")
        except ValueError:
            print("Invalid input. GPA must be a numeric value.")
    while True:
        major = input("Enter the student's major: ")
        if len(major) > 0:
            break
        else:
            print("Invalid input. Please enter a valid major.")
    while True:
        facultyAdvisor = input("Enter the student's faculty advisor: ")
        if len(facultyAdvisor) > 0:
            break
        else:
            print("Invalid input. Please enter a valid faculty advisor.")
    while True:
        address = input("Enter the student's address: ")
        if len(address) > 0:
            break
        else:
            print("Invalid input. Please enter a valid address.")
    while True:
        city = input("Enter the student's city: ")
        if len(city) > 0:
            break
        else:
            print("Invalid input. Please enter a valid city.")
    while True:
        state = input("Enter the student's state: ")
        if len(state) > 0 and state.isalpha():
            break
        else:
            print("Invalid input. Please enter a valid state.")
    while True:
        zipCode = input("Enter the student's zip code: ")
        if zipCode.isnumeric() and len(zipCode) == 5:
            break
        else:
            print("Invalid input. Zip code must be a 5-digit numeric value.")
    while True:
        mobilePhoneNumber = input("Enter the student's mobile phone number: ")
        if mobilePhoneNumber.isnumeric() and len(mobilePhoneNumber) == 10:
            break
        else:
            print("Invalid input. Mobile phone number must be a 10-digit numeric value.")

    sql = ("INSERT INTO Students (FirstName, LastName, GPA, Major, FacultyAdvisor, "
           "Address, City, State, ZipCode, MobilePhoneNumber, isDeleted) "
           "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
    val = (firstName,
        lastName,
        gpa,
        major,
        facultyAdvisor,
        address,
        city,
        state,
        zipCode,
        mobilePhoneNumber,
        0)
    mycursor.execute(sql, val)
    conn.commit()

    print("Student added successfully")
    mycursor.close()

def updateStudent(conn):
    mycursor = conn.cursor()
    while True:
        try:
            studentID = int(input("Enter the student ID: "))
            break
        except ValueError:
            print("Bad input. Please enter a valid student ID")
    mycursor.execute("SELECT * FROM Students WHERE StudentID = ? AND isDeleted = 0", (studentID,))
    myresult = mycursor.fetchone()
    if myresult:
        # The student exists, so update their information
        while True:
            major = input("Enter the student's major: ")
            if len(major) > 0:
                break
            else:
                print("Invalid input. Please enter a valid major.")

        while True:
            facultyAdvisor = input("Enter the student's faculty advisor: ")
            if len(facultyAdvisor) > 0:
                break
            else:
                print("Invalid input. Please enter a valid faculty advisor.")

        while True:
            phoneNumber = input("Enter the student's mobile phone number: ")
            if phoneNumber.isnumeric() and len(phoneNumber) == 10:
                break
            else:
                print("Invalid input. Mobile phone number must be a 10-digit numeric value.")

        # Update the student's information in the database
        sql = "UPDATE Students SET Major = ?, FacultyAdvisor = ?, MobilePhoneNumber = ? WHERE StudentID = ?"
        val = (major, facultyAdvisor, phoneNumber, studentID)
        mycursor.execute(sql, val)
        conn.commit()
        print("Student successfully updated")
    else:
        print("That student does not exist")
    mycursor.close()

def deleteStudent(conn):
    mycursor = conn.cursor()
    while True:
        try:
            studentID = int(input("Enter the student ID: "))
            break
        except ValueError:
            print("Bad input. Please enter a valid student ID")
    mycursor.execute("SELECT * FROM Students WHERE StudentID = ? AND isDeleted = 0", (studentID,))
    myresult = mycursor.fetchone()
    if myresult:
        mycursor.execute("UPDATE Students SET isDeleted = 1 WHERE StudentID = ?", (studentID,))
        conn.commit()
        print("Student deleted successfully.")
    else:
        print("Student not found.")
    mycursor.close()

def queryByMajor(conn, maj):
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM Students WHERE Major = ? AND isDeleted = 0", (maj,))
    result = mycursor.fetchall()
    for x in result:
        print(x)
    mycursor.close()

def queryByMinGPA(conn, gpa):
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM Students WHERE GPA >= ? AND isDeleted = 0", (gpa,))
    result = mycursor.fetchall()
    for x in result:
        print(x)
    mycursor.close()

def queryByCity(conn, city):
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM Students WHERE City = ? AND isDeleted = 0", (city,))
    result = mycursor.fetchall()
    for x in result:
        print(x)
    mycursor.close()

def queryByState(conn, state):
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM Students WHERE State = ? AND isDeleted = 0", (state,))
    result = mycursor.fetchall()
    for x in result:
        print(x)
    mycursor.close()

def queryByAdvisor(conn, adv):
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM Students WHERE FacultyAdvisor = ? AND isDeleted = 0", (adv,))
    result = mycursor.fetchall()
    for x in result:
        print(x)
    mycursor.close()

def exit():
    raise SystemExit