# # Bottle class
# class Bottle:
    #Attribute Defenition
    # brand="Aqua" #Beta
    # def __init__(self,c,h,r): #self=b2,
    #     self.color=c
    #     self.height=h
    #     self.radius=r
    #     print("Hello Guys")

    # def printVolume(self,a,b): #self=b1
    #     print((22/7)*(self.radius)*(self.radius)*(self.height))
    #     print(a+b)

    # @classmethod
    # def printBrandName(cls): 
    #     print(cls.brand)

    # @staticmethod
    # def greet():
    #     print("Good Morning")

# Bottle.printVolume()

# print(Bottle.color)

# b1=Bottle("Blue",56,5) #Bottle.__init__(b1,"Blue",56,5)
# b2=Bottle("Black",12,2)#Bottle.__init__(b2,"Blue",56,5)

# b1.printVolume(5,5)
# b1.printVolume(10,15) #Bottle.printVolume(b1,10,15)

# b1.printBrandName() #Bottle.printBrand(Bottle)

# b1.greet() #Bottle.greet()
# b1=Bottle() #object1 3 attr 0 method brand="beta"
# b2=Bottle() #object2 3 attr 0 method brand="beta"

# b1.printVolume()
# b1.printBrandName()
# Bottle.printBrandName()
# b1.greet()
# Bottle.greet()

# # Bottle.brand="Beta"
# b3=Bottle() #object2 3 attr 0 method brand="beta"

# print(b1.brand)
# print(b2.brand)
# print(b3.brand)
# b1.color="Blue"
# b1.cap="steel"

# print(b1.color)
# print(b1.cap)
# print(b2.color)

# b1.brand="AquaFill"


# print(Bottle.brand)

# print(Bottle.height)
# 3 attr, 0 meth

# print(Bottle.brand)
# Bottle.brand="AquaFill" #
# print(Bottle.color)

# b1.brand="Beta"
# b1.color="Black"
# b2.color="Blue"
# b1.brand="AquaFill"
# print(b2.color)
# print(b1.color)
# print(b1.height)
# print(b2.radius)
# print(b1.brand)
# print(b2.brand)

# print(Bottle.height)


# a=10 
# b="Hello"
# c=[1,2,3]
# b1=Bottle("Grey",23,3)

# # print(type(a)) #<class "int">
# print(type(b1)) #<class "__main__.Bottle">

# print("Hello"-"World")



# def add(a,b):
#     print(a+b)

# def add(a,b,c=0):
#     print(a+b+c)

# add(2,3)
# add(12,3,3)

# class User:
#     def __init__(self,u,p,m):
#         self.username=u #normal
#         self.__password=p #private
#         self._mail=m #protected

#     def checkPass(self,password):
#         return self.__password==password

    

# u1=User("Leo","12345","Leo123@gmail.com")

# print(u1.username)
# print(u1._mail) #accessible
# print(u1.__password) #not accessible

# passw=input("Password: ")

# if passw==u1.__password:
# if u1.checkPass(passw):
#     print("User Auth Done")
# else:
#     print("Wrong Credentials").

