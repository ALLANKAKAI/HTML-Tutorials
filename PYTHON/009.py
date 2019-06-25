class College:
    def __init__(self, college_name):
        self.__college_name = college_name

    def get_college(self):
        return self.__college_name


class Student(College):
    def __init__(self, student_name, reg_num):
        self.student_name = student_name
        self.reg_num = reg_num
        super(). __init__("Rongo")

    def get_bio(self):
        return self.student_name, self.reg_num


kefa = Student("Wekesa", 321)

print(kefa)
print(kefa.get_college())
