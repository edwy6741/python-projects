students = [
    {"name": "Alex", "grades": [90, 85, 92]},
    {"name": "Sarah", "grades": [78, 88, 84]},
    {"name": "James", "grades": [95, 91, 89]},
    {"name": "Emily", "grades": [72, 80, 75]},
    {"name": "Daniel", "grades": [88, 94, 90]}
]

def class_average(students):
    if not students:
        return None
    total = 0
    number = 0
    for average in students:
        total += sum(average["grades"])
        number += len(average["grades"])
    return total / number

def student_avg(student):
    total = 0
    number = 0
    if not student:
        return None
    total += sum(student['grades'])
    number += len(student['grades'])
    average = total/number
    return average

students1 = [
    {"name": "Alex", "grades": [90, 85]},
    {"name": "James", "grades": [95, 91]}
]

def individual(students):
    for student in students:

        if student['name'] == 'James':
            return student

def top_student(students):
    highest_average = students[0]
    for high in students:

        highest_average = high['grades']
        if high['grades'] > highest_average:
            high['grades'] = highest_average
    return highest_average

print(top_student(students))