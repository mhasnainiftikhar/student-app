def get_students():
    return ["Alice", "Bob", "Charlie"]

def count_students():
    return len(get_students())

if __name__ == "__main__":
    print("Student Management System")
    print("Total students:", count_students())
