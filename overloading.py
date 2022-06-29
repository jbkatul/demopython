class Book:

    def __init__(self,nm,pg):
        self.name = nm
        self.pages = pg

    def __add__(self,other):
        return self.name + other.name

    def __add__(self,other,anyother):
        return self.name + other.name , self.pages + other.pages


    def __sub__(self,other):
        return self.pages - other.pages



B1 = Book('Basics of Python', 200)
B2 = Book('Advance Python', 500)
B3 = Book('Advance Python', 200)
print(B1 + B2 + B3)


'''print(B1 - B2)
print(B1 * B2)
print(B1 / B2)
print(B1 >= B2)
print(B1 <= B2)
print(B1 == B2)'''
