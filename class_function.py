class Individual:
    def __init__(self, name):
        self.name = name
        

    def get_name(self):
        return self.name

    def add_birthday(self, birthday):
        self.birthday = birthday

    def get_age(self,age):
        self.age=age


    def __str__(self):
        return f"{self.name}"


class AU_Employee(Individual):
    new=1
    def __init__(self, name):
        super().__init__(name)
        

    def get_unique_id(self):
        self.unique_id = AU_Employee.new
        AU_Employee.new+=1
        return self.unique_id

class Faculty(AU_Employee):
    pass


class EN_Faculty(Faculty):
    def __init__(self, name,  classroom_year):
        super().__init__(name)
        self.classroom_year = classroom_year

    def assign_class(self, classroom_year):
        self.classroom_year = classroom_year
        return self.classroom_year


class Roster_AU():
    def __init__(self):
        self.faculties = []
        self.courses = {}

    def add_faculty(self, faculty):
        if faculty not in self.faculties:
            self.faculties.append(faculty)
            self.courses[faculty.get_name()] = []

    def add_course(self, course, faculty):
        if faculty.get_name() in self.courses:
            self.courses[faculty.get_name()].append(course)
        else:
            raise ValueError("Faculty not found")

    def get_courses(self, faculty):
        if faculty.get_name() in self.courses:
            return self.courses[faculty.get_name()]
        else:
            raise ValueError("Faculty not found")

    def sort_faculty(self, faculty):
        return faculty.get_name()

    def get_sorted_faculties(self):
        return sorted(self.faculties, key=self.sort_faculty)



Rushikesh_Pawar = EN_Faculty("Rushikesh sir ",  "2024")
Rahul_Thakur = EN_Faculty("Rahul sir", "2024")
c=AU_Employee("Rushikesh")
print(Rushikesh_Pawar.get_unique_id)

d=AU_Employee("Rahul")

roster = Roster_AU()

roster.add_faculty(Rushikesh_Pawar)
roster.add_faculty(Rahul_Thakur)

roster.add_course("Creative and Critical Thinking", Rushikesh_Pawar)
roster.add_course("Engineering Physics", Rahul_Thakur)
roster.add_course("Engineering Mathematics", Rahul_Thakur)
roster.add_course("introduction to computing",Rushikesh_Pawar)

for faculty in roster.get_sorted_faculties():
    courses = roster.get_courses(faculty)
    print(f"{faculty}: {courses}")
