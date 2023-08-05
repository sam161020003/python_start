class run:
    #to pass data inside the class we use constructor
    def __init__(self,phome_number,email_id,student_id): # inbuilt function used to pass data with in class 
        self.phone_number1=phome_number
        self.email_id1=email_id
        self.student_id1=student_id # LHS vsls pata hai system ka
    def return_student_id(self):
        return self.phone_number1,self.email_id1,self.student_id1
    # agar hm values pass kr rhe hain class ke saath to hmesh () iske andar pehla word self hi aayega
    
sam=run(9464945684,'samarthsinghadhikari03@gmail.com',102203303)# creating object and passing values to quesi
print(sam.return_student_id())
print(sam.email_id1)
print(sam.phone_number1)