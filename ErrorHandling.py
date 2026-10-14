# print("Hello")
# if True:
#     print(1)

print(1)
print(2)
print(3)
print(4)
# # print(5 #error

# print("Done")

# print("Hello"+3)
# print(int("Hello"))
# print(9/0)
# print("Done")

# try:
#     print(1)
#     print(2)
#     print(4/0)
#     print(2+"Hello")
# except TypeError:
#     print("You cannot add int and str")
# except ZeroDivisionError:
#     print("Invalid Expresiion")


# print("Done")
try:
    n1=int(input("Enter Your Number1: "))
    n2=int(input("Enter Your Number2: "))
    print(n1/n2)
except ValueError:
    print("Invalid Inputs")
except ZeroDivisionError:
    print("The number cant be divided by 0")
finally:
    print("Over..!")