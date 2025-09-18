import pytest 


def test_equal_or_not_equal():
    assert 1 == 1

def test_equal_or_not_equal():
    assert 1 == 1


class Student :
    def __init__(self, name, age, major, year):
        self.name = name
        self.age = age
        self.major = major
        self.year = year

@pytest.fixture
def default_student():
    return Student("John Doe", 20, "Mathematics", 3)

def test_student(default_student):
    assert default_student.name == "John Doe"
    assert default_student.age == 20, 'Age should be 20'