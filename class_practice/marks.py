class Marks:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    
    def avarage_calculate(self):
        sum = 0
        for value in self.marks:
            sum +=value
            avg = sum/len(self.marks)
        print("Your Avarage Score is ",avg)



student = Marks("khadija",[88,9,7,9])
print(student.avarage_calculate())