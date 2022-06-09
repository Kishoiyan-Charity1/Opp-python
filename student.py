class Student:
    # name="kanini"
    # age=20
    # country="kenya"
    # school="akirachix"
    school="akirachix"
    def __init__(self,first_name,second_name,age,country):
        self.first_name= first_name
        self.second_name= second_name
        self.age= age
        self.country= country


    def greet(self):
         return f'hello {self.name} from {self.country} welcome to {self.school}'

    def full_name(self):
        y= f"{self.first_name} {self.second_name}"
        return y

    def year_of_birth(self):
        year_of_birth= 2000-self.age

        return year_of_birth

    def initials(self):
        x= f'{self.first_name[0]}{self.second_name[0]}'
        t=x.upper()
        return t

