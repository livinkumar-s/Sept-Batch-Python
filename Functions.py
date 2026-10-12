# def printSteps():
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     print("-------")


# a=printSteps() #caller #None
# print(a)
# printSteps()
# printSteps()

# def addNum(a,b): #4,5
#     print(a+b)

# addNum(4,5)
# addNum(40,50)



# def addNum(a,b,c=10): #4,5
#     print(a)
#     print(b)
#     print(c)
#     print(a+b+c)

# addNum(9,5)
# addNum(c=10,a=20,b=30)
# addNum(34,43,15)

# def findSum(*a): #Tuple
#     print(a)

# findSum(3,4,3,213,234,234,234) 


# def getDetails(**a): #Dict
#     print(a)

# getDetails(name="Ken",age=42,role="VIP")

# def isEven(n):
#     if n%2==0:
#         return True
#     return False

# print(isEven(9))

# def findMul(a,b):
#     return a*b

# print(findMul(3,findMul(3,findMul(2,findMul(4,2)))))

# a=input("Enter Name: ")

# print(4,5,6,7)


# Scopes 

# a=10

# def showNum():
#     # a=10
#     print(a)

# showNum()
# print(a)

# a=10

# def showNum():
#     a=20
#     print(a) #10, 20

# def inc():
#     global a
#     # a+=1
#     # print(a)
#     a+=1 # global scopped var

# # showNum()
# inc()
# inc()
# inc()
# print(a) 

# def parent():
#     a=10
#     def child():
#         def grandchild():
#             nonlocal a
#             a-=1 #local scoped var
#         grandchild()
#         grandchild()
#         grandchild()
#     child()
#     print(a) #7


# parent()


# def greet():
#     print("Hello")

# b=12


print()
input()
