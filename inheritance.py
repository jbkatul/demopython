# Hybrid Inheritance Example

class A:
	def m1(self):
		print('This is method m1 of class A')

class B(A):
	def m2(self):
		print('This is method m2 of class B')

class C(A):
	def m3(self):
		print('This is method m3 of class C')

class D:
	def m4(self):
		print('This is method m4 of class D')

class E(C,D):
	def m5(self):
		print('This is method m5 of class E')

class F(B):
	def m6(self):
		print('This is method m6 of class F')


f1 = F()
f1.m6()
f1.m2()
f1.m1()
#f1.m5()

e1 = E()