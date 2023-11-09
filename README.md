
Spencer Lafferty 

2378112

lafferty@chapman.edu

CPSC 408-01

Assignment 1

Notes:
- Query by GPA assumes a 4.0 GPA scale
- In order to import the students.csv file, uncomment line 73 of Main.py

Known Errors/Oversights:
- When Querying, if the query value is recognized as valid but there is no result, nothing will show. This isn't a bug, just a missing feature.
- All user prompts recognize numbers as characters, even when they shouldn't be
- The imported data has some inconsistencies, such as phone number formats differ wildly
- There are inconsistencies in how AddStudent and QueryStudent checks input strings. 99% of the time this won't be apparent, but it allows the user to add absurdly long strings as values in AddStudent. Please don't :)