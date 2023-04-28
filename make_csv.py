import csv
import random

# Get number of entries to generate from user
num_entries = int(input('How many entries would you like to generate? '))

# Get the grade levels from user
lowest_grade = int(input('What is the lowest grade level? '))
highest_grade = int(input('What is the highest grade level? '))

# List of first names and last names
first_names = []
last_names = []

# Read in first names from file
with open('first_names.txt', 'r') as f:
    for line in f:
        names = line.split(',')
        for name in names:
            first_names.append(name.strip())

# Read in last names from file
with open('last_names.txt', 'r') as f:
    for line in f:
        names = line.split(',')
        for name in names:
            last_names.append(name.strip())

# Open a new CSV file and write headers
with open('students.csv', 'w', newline='') as csvfile:
    fieldnames = ['last name', 'first name', 'student ID', 'email', 'grade level']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Generate random data and write to the CSV file
    for i in range(num_entries):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        student_id = 'S' + str(i).zfill(4)
        email = first_name.lower() + '.' + last_name.lower() + '@anytownschools.org'
        grade_level = random.randint(lowest_grade, highest_grade)
        writer.writerow({'last name': last_name, 'first name': first_name, 'student ID': student_id, 'email': email, 'grade level': grade_level})
