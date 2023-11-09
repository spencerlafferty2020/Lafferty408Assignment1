# Spencer Lafferty
# 2378112
# lafferty@chapman.edu
# CPSC 408-01
# Assignment 1

import sqlite3
import csv
import InputPrompter
import random
from sqlite3 import Error

# Create a daatabase called StudentDB and a table called Student
conn = sqlite3.connect('./StudentDB.db')
mycursor = conn.cursor()

# Check if Students already exists as a table
mycursor.execute ("SELECT name FROM sqlite_master WHERE type = 'table' and name = 'Students'")
tableExists = mycursor.fetchone()

# Advisor List
advisors = ["Advisor 1", "Advisor 2", "Advisor 3", "Advisor 4"]

if not tableExists:
    try:
        mycursor.execute("""CREATE TABLE IF NOT EXISTS
            Students (
                StudentId INTEGER PRIMARY KEY,
                FirstName TEXT,
                LastName TEXT,
                GPA REAL,
                Major TEXT,
                FacultyAdvisor TEXT,
                Address TEXT,
                City TEXT,
                State TEXT,
                ZipCode TEXT,
                MobilePhoneNumber TEXT,
                isDeleted INTEGER NOT NULL DEFAULT 0
        );""")
    except Error as e:
        print(e)
    conn.commit()
    print("Students table created")
else:
    print ("Students already exists")

# Function to import data into database
def importFile():
    with (open('students.csv', 'r') as impFile):
        reader = csv.DictReader(impFile)
        for row in reader:
            sqlString = ("INSERT INTO Students (FirstName, LastName, GPA, "
                         "Major, FacultyAdvisor, Address, City, State, ZipCode, "
                         "MobilePhoneNumber, isDeleted) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
            vals = (row["FirstName"],
                row["LastName"],
                row["GPA"],
                row["Major"],
                random.choice(advisors),
                row["Address"],
                row["City"],
                row["State"],
                row["ZipCode"],
                row["MobilePhoneNumber"],
                0
            )
            mycursor.execute(sqlString, vals)
            conn.commit()

    print('data import complete')

# importFile()
InputPrompter.MenuPrompt(conn)
