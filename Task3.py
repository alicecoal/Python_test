class_ = {}

def add_student(class_, name, subject):
    # Добавляем предмет для ученика
    if name in class_:
        class_[name] += subject
    else:
        class_[name] = subject

def show_all():
    sorted_students = dict(sorted(class_.items(), key=lambda item: item[0], reverse=True))
    for name, subjects in sorted_students.items():
        print(f"{name}: {subjects}")

def student_for_sub(name):
    subjects_of_student = class_.get(name, [])
    if subjects_of_student:
        print(subjects_of_student) 
    else:
        print("There are no students with this name. ")

def sub_for_students(subject):
    students_with_subject = [name for name, subjects in class_.items() if subject in subjects]
    if students_with_subject:
        print(students_with_subject)
    else:
         print("There are no matching students. ")



num_students = int(input("Write number of students: "))

# Заполняем информацию о учениках
for i in range(num_students):
    name = input(f'Name of {i+1} student: ')
    subjects = input(f'Subjects of {i+1} student: ').split()
    add_student(class_, name, subjects)

show_all()
student_for_sub("Jane")
student_for_sub("Jack")
sub_for_students("math")
sub_for_students("astronomy")
sub_for_students("biology")