# f1=open("text1.txt","w")
# print(f1.read())
# f1.seek(16)
# content=f1.read(2)
# content=f1.read(10)
# content=f1.readlines()[2]
# content=f1.readline()
# print(content)
# print(f1.tell())
# print(f1.readable())
# f1.close()


# f1=open("text.txt","w")

# # print(f1.writable())
# f1.write("Hi\nHello\nWelcome..!")

# f1.close()

# f1=open("text.txt","a")

# f1.write("\nHi\nHello\nWelcome..!")

# f1.close()

# f1=open("text1.txt","x")


# f1=open("files/text.txt")
# print(f1.read())
# f1.close()

with open("files/text.txt") as f:
    print(f.read())
