
list = [1,2,3,4,5,6,7,8,9,10,0]
print("Sorted List: ", sorted(list))
print("Original List: ", list)
list.sort()
print("Sorted List with .sort: ", list)
print("Reversed List: ", sorted(list, reverse=True))

map = { "a": 1, "b": 2, "zzz": 3, "d": 4, "e": 5}
print("Sort map by key: ", sorted(map, key=lambda x: x))
print("Sort map by value: ", sorted(map, key=lambda x: map[x]))

print("Sort strings: ", sorted("This is a test string from Andrew"))

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print("Sort tuples: ", sorted(student_tuples, key=lambda student: student[2]))

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print("Sort objects: ", sorted(student_objects, key=lambda student: student.age)) 