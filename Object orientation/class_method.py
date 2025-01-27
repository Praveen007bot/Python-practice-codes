class Student:
    coll_name = "Kodnest"

    def get_info(self):
        print(f'College name: {Student.coll_name}')

    @classmethod
    def change_name(cls, new_name):
        cls.coll_name = new_name


s = Student()
s.get_info()
Student.change_name("Code")
s.get_info()