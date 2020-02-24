##class Bank:
##    bname='nossam'
##    def deposit(self,amt):
##        print('the balance is:',self.amt)
##    def withdraw(self,amt):
##        print('the balance is:',self.amt)
##class SavingsAccount(Bank):
##    def deposit(self,amt):
##        pass
##class CurrentAccount(Bank):
##    def withdraw(self,amt):
##        pass
##
##b=Bank()
##b.deposit(10000)
##b.withdraw(5000)
##sa=SavingsAccount()
##ca=CurrentAccount()
##while True:
##    print('the  bankname is:',Bank.bname)
##    print('enter account holdername:',)
##    print('enter account number:',)
##    print('1.savingsaccount')
##    print('2.currentaccount')
##    moption=int(input('please select your option:',))
##    if moption==1:
##        print('1.deposit')
##        print('2.withdraw')
##        suboption=int(input('please select your option:',))
##        if suboption==1:
##            sa.deposit(10000)
##        elif suboption==2:
##            sa.withdraw()
##        else:
##            print('u entered involved option')
##    elif moption==2:
##        print('1.deposit')
##        print('2.withdraw')
##        suboption=int(input('please select your option:',))
##        if suboption==1:
##            ca.deposit()
##        elif suboption==2:
##            ca.withdraw()
##        else:
##            print('u entered involved option')
##        
##                  
##        
##        
##        
##class Student:
##    
##    
##sname='prschool'
##    def __init__(self,stname,stage,address,mobile):
##        self.stname=stname
##        self.stage=stage
##        self.address=address
##        self.mobile=mobile
##    def display(self):
##        print('student school name:',Student.sname)
####        print('student class:',Student.levelclass1)
##        print('the student name is:',self.stname)
##        print('the student age:,'self.stage)
##        print('the student address:',self.address)
##        print('the student mobile:',self.mobile)
##
##
## s=Student('ravi',23,'banglore',7382517853)
## s.display()




##class Bike:
##    showroomname='herohonda'
##    loc='nandyal'
##    def __init__(self,bcolor,engno,bno,bmodel,manufyear,millege,speed):
##        self.bcolor=bcolor
##        self.engno=engno
##        self.bno=bno
##        self.bmodel=bmodel
##        self.manufyear=manufyear
##        self.millege=millege
##        self.speed=speed
##
##    def display(self):
##       print('showroom name is:',Bike.showroomname)
##       print('location is:',Bike.loc)
##       print('bike color is:',self.bcolor)
##       print('bike engine number is:',self.engno)
##       print('bike number plate is:',self.bno)
##       print('bike mobel:',self.bmodel)
##       print('bike manufyear is:',self.manufyear)
##       print('bike millege per km:',self.millege)
##       print('bike speed km/h is:',self.speed)
##
##
##
##obj=Bike('red','25Ab6','AP21AJ7592','passion plus',2018,70,120)
##obj=Bike('red','25Ab6','AP21AJ7592','passion plus',2018,70,120)
##obj.display()


##class Student:
##    collegename='national degree college'
##    loc='nandyal'
##    def __init__(self):
##        Student.class1='degree'
##    def display(self):
##        print('the student collegename:',Student.collegename)
##        print('the student location:',Student.loc)
##        print('the student class room is:',Student.croom='1st floor')
##        print('the student class is:',Student.class1)
##        
##obj=Student()
##obj.display()

##def display():
##    print('hello')
##    print('goodmorning')
##    print('how r u')
##    print('nice place')
##    print('excellent work')
##
##display()    

##def display():
##    yield 'hello'
##    yield 'goodmorning'
##    yield 'how r u'
##    yield 'nice place'
##    yield 'excellent work'
##
##d=display()
##print(next(d))
##print(next(d))
##print(next(d))
##print(next(d))
##print(next(d))
##print(next(d))

##count=1
##def fun():
##    yield count
##
##d=fun()
##next(d)
##print(next(d))

##class A:
##    loc='hyd'
##    def __init__(self):
##        print('the name is:'A.name='ravi')
##    def display(self):
##        print('age is:',A.age=23)
##a=A()
##a.display()
##print(A.loc)
##print('work role is:',A.a='developer')

##a=[]
##row=int(input('enter no of rows'))
##col=int(input('enter no of cols'))
##for i in range(row):
##    a.append([])
##    for j in range(col):
##        num=int(input('enter nos'))
##        a[i].append(num)
##
##
##
##print(a)
##output
##-----------
##enter no of rows3
##enter no of cols3
##enter nos1
##enter nos2
##enter nos3
##enter nos4
##enter nos5
##enter nos6
##enter nos7
##enter nos8
##enter nos9
##[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
##

import numpy as np
##a=np.array([[1,2,3],[4,5,6],[7,8,9]])
##print(a)
##print(a.shape)
##print(a.reshape(1,9))
##print(a[2])
##print(a[2][1])
##print(a.sum())
##print(a.min())
##print(a.max())
##print(a.sum(axis=0))
##print(a.min(axis=0))
##print(a.max(axis=0))
##print(a.sum(axis=1))
##print(a.min(axis=1))
##print(a.max(axis=1))
##


##a=np.array([[1,2,3,4]])
##b=np.array([[5,6,7,8]])
##print(a,'\t',b)
##print(a+b)
##print(a-b)
##print(a*b)

##def dec_fun(fun1):
##    def inner(msg):
##        if msg=='ravi':
##            print('hello',msg)
##        else:
##            print('hello',msg)
##            fun1(msg)
##            return inner
##
##
##def fun(msg):
##    print('hello',msg)





##class Student:
##    '''hello good morning'''
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##
##    def info(self):
##        print('hello {} how are you'.format(self.name))
##        print('your age is',self.age)
##s=Student('ravi',23)
##print(s.__doc__)
##print(s.name)
##print(s.age)
##s.info()
##print(s.__dict__)
##        
##              


##class Student:
##    '''welcome to college'''
##print(Student.__doc__)
##print(type(Student))


##class College:
##    clgname='crec'
##    loc='tirupati'
##    def __init__(self,type):
##        print('this is parent class constructor')
##        self.type=type
##    def info(self):
##        print('the type of college is',self.type)
##
##class Student(College):
##    def __init__(self,sname,sbranch,spesub):
##        print('this is child class constructor')
##        super().__init__('engi')
##
##        self.sname=sname
##        self.sbranch=sbranch
##        self.spesub=spesub
##    def display(self):
##       print('student clgname is',College.clgname)
##       print('college location is',College.loc)
##       print('student name is',self.sname)
##       print('student sbranch is',self.sbranch)
##       print('student spesub is',self.spesub)
##
##
##s=Student('ravi','mca','computer')
##s.info()
##s.display()
##


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
      super().__init__(fname, lname)
      self.fname=fname
      self.lname=lname
    

  def displayname(self):
      print(self.fname,self.lname)

x = Student("Mike", "Olsen")
x.printname()
x.displayname()

























       
        




































    





