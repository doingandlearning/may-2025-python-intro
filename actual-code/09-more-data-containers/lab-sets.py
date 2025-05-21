# Set up sets
exam = {'Andrew', 'Kirsty', 'Beth', 'Emily', 'Sue'}
project = {'Kirsty', 'Emily', 'Ian', 'Stuart'}

# Output the basic sets
print('exam:', exam)
print('project:', project)

"""
    Which students took both the exam and submitted a project?
    Which students only took the exam?
    Which students only submitted the project?
    List all students who took either (or both) of the exam and the project.
    List all students who took either (but not both) of the exam and the project.

"""

print(exam.intersection(project))
print(exam & project)

print(exam.difference(project))
print(exam - project)

print(project.difference(exam))
print(project - exam)

print(project.union(exam))
print(project | exam)

print(project.symmetric_difference(exam))
print(project ^ exam)




















