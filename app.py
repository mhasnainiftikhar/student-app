def add_student(name):
    students = get_students()
    students.append(name)
    return students

def get_students():
    return ["Alice", "Bob", "Charlie"]

def count_students():
    return 100

if __name__ == "__main__":

    print("Student Management Platform")
    print("Total students:", count_students())
