students = [
    {"name": "Sam", "score": 90},
    {"name": "Maya", "score": 72},
    {"name": "Leo", "score": 85},
    {"name": "Ava", "score": 58},
    {"name": "Noah", "score": 85},
]

def print_names(students):
    for student in students:
        print(student["name"])


def print_grades(students):
    for student in students:
        print(student["score"])

def print_names_grades(students):
    for student in students:
            print(student["name"])
            print(student["score"])

def passing(students):
    names = []
    for student in students:
          if student["score"] >= 60:
               names.append(student["name"])
    return names

def avg_score(students):
    total = 0
    number = 0
    if not students:
                 return None
    for student in students:
        total += student["score"]
        number += 1
    return total/number


def top_student(students):
    if not students:
          return None
    best = students[0]
    for student in students:
         if student["score"] > best["score"]:
              best = student
    return best["name"]

def add_student(students,name,score):
     students.append({"name": name, "score": score})

def summary(students):
     return {
          "average": avg_score(students),
          "top": top_student(students),
          "passing_count": len(passing(students)),
     }

print(summary(students))