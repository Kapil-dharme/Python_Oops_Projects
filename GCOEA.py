class Student:
    def __init__(self,name,CET_Score,branch):
        self.name=name
        self.CET_Score=CET_Score
        self.branch=branch
        self.Seat_available=True
    def __str__(self):
        status="Seat available" if self.Seat_available else "Seat booked"
        return f"{status} for {self.name} in {self.branch} branch."
class Admission:
    def __init__(self,student,year_of_admission):
        self.student=student
        self.year_of_admission=year_of_admission
    def confirm_admission(self):
        if not self.student.Seat_available:
            print(f"{self.student.name} score is below cutoff .")
        else:
            self.student.Seat_available=False
            print(f"{self.student.name} seat is confirmed .")
    def graduate_student(self):
        if not self.student.Seat_available:
            self.student.Seat_available=True
            print(f"{self.student.name} has completed his graduation in {self.year_of_admission+4}")
        else:
            print("The admission is unavailable.")
class College:
    def __init__(self,name):
        self.name=name
        self.admissions=[]
        self.students=[]
    def add_students(self,name,CET_Score,branch):
        student=Student(name,CET_Score,branch)
        self.students.append(student)
    def show_students(self):
        for college_students in self.students:
            print(college_students)
    def book_admission(self,student_name,Percentile,type,year_of_admission):
        for students in self.students:
            if students.CET_Score==Percentile:
                admissions=Admission(students,year_of_admission)
                admissions.confirm_admission()
                self.admissions.append(admissions)
                return
        print(f"{student_name} score is below cutoff for {type} branch.")
    def graduate_students(self,nam,year):
        for admissions in self.admissions:
            if admissions.student.name==nam and not admissions.student.Seat_available:
                admissions.graduate_student()
                self.admissions.remove(admissions)
                return
        print("Admission was not found.")

college=College("GCOEA")
college.add_students('Kapil',98.41,'Electrical engineering')
college.add_students('pranav',98.50,'computer science and engineering')
college.add_students('aniket',98.63,'mechanical engineering')
college.add_students('mohit',94.88,'computer science and engineering')
college.show_students()
college.book_admission('Kapil',98.41,'Electrical engineering',2024)
college.book_admission('mohit',94.88,'computer science and engineering',2025)
college.book_admission('pranav',98.50,'computer science and engineering',2024)
college.show_students()
college.graduate_students('Kapil',2024)
college.graduate_students('mohit',2025)
college.show_students()