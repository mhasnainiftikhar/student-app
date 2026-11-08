from app import get_students, count_students, add_student

def test_get_students():
    assert get_students() == ["Alice", "Bob", "Charlie"]

def test_count_students():
    assert count_students() == 3

def test_add_student():
    result = add_student("David")
    assert result == ["Alice", "Bob", "Charlie", "David"]
