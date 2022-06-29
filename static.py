class Demo:
     
     @staticmethod
     def add_two(a,b):
        print(a+b)


d = Demo()
print(id(d))
print(type(d))

'''
d.add_two(10,20)
Demo.add_two(32,11)'''