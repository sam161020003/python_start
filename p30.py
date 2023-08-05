#Polymorphism Example
class ds:
    def syl(self):
        print("this is my syllabus for data science masters")

class webdev:
    def syl(self):
        print("this is my syllabus for web dev")

def class_parcer(class_obj):
        for i in class_obj:
          i.syl()

ds1=ds()
wd1=webdev()

class_obj=[ds1,wd1]

print(class_parcer(class_obj))