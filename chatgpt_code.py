import pytest

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def printInfo(self):
        print("ID:", self.id)
        print("Name:", self.name)


class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title


class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill


# 테스트 코드
def test_person_creation():
    person = Person(1, "John")
    assert isinstance(person, Person)

def test_manager_creation():
    manager = Manager(2, "Alice", "Senior Manager")
    assert isinstance(manager, Manager)

def test_employee_creation():
    employee = Employee(3, "Bob", "Python")
    assert isinstance(employee, Employee)

def test_person_info():
    person = Person(1, "John")
    assert person.id == 1
    assert person.name == "John"

def test_manager_info():
    manager = Manager(2, "Alice", "Senior Manager")
    assert manager.id == 2
    assert manager.name == "Alice"
    assert manager.title == "Senior Manager"

def test_employee_info():
    employee = Employee(3, "Bob", "Python")
    assert employee.id == 3
    assert employee.name == "Bob"
    assert employee.skill == "Python"

@pytest.mark.parametrize("obj, expected_output", [
    (Person(1, "John"), "ID: 1\nName: John"),
    (Manager(2, "Alice", "Senior Manager"), "ID: 2\nName: Alice"),
    (Employee(3, "Bob", "Python"), "ID: 3\nName: Bob")
])

def test_print_info(capsys, obj, expected_output):
    obj.printInfo()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output.strip()
    
def test_print_info(capsys, obj, expected_output):
    obj.printInfo()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output.strip()

def test_person_print_info(capsys):
    person = Person(1, "John")
    person.printInfo()
    captured = capsys.readouterr()
    assert captured.out.strip() == "ID: 1\nName: John"

def test_manager_print_info(capsys):
    manager = Manager(2, "Alice", "Senior Manager")
    manager.printInfo()
    captured = capsys.readouterr()
    assert captured.out.strip() == "ID: 2\nName: Alice"

def test_employee_print_info(capsys):
    employee = Employee(3, "Bob", "Python")
    employee.printInfo()
    captured = capsys.readouterr()
    assert captured.out.strip() == "ID: 3\nName: Bob"


if __name__ == "__main__":
    test_person_creation()
    test_manager_creation()
    test_employee_creation()
    test_person_info()
    test_manager_info()
    test_employee_info()
    #test_person_print_info(capsys=)
    #test_manager_print_info()
    #test_employee_print_info()
