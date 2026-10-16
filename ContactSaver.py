from mysql import connector

connectionObj=connector.connect(host="localhost",user="root",password="12345",database="septbatch1")

cursor=connectionObj.cursor()

# cursor.execute("CREATE TABLE contact (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(40) NOT NULL, PHONE CHAR(10) NOT NULL UNIQUE)")

# print("Table Created!")

# cursor.execute("INSERT INTO contact (name,phone) VALUE (%s,%s)",("Ben","7787878788"))
# cursor.execute("UPDATE contact SET name=%s where id=%s",("Benjamin",5))
# connectionObj.commit()

# cursor.execute("SELECT * FROM contact")

# print(cursor.fetchall())
# print(cursor.fetchone())
# print(cursor.fetchmany(2))

# print("Retrived!")

def viewAllContact():
    cursor.execute("SELECT * FROM contact")
    allRecords=cursor.fetchall()
    for id,name,phone in allRecords:
        print(f"Name: {name} Phone: {phone}")
    

def addContact():
    try:
        name=input("Enter the name: ")
        phone=input("Enter the phone: ")
        if len(phone) != 10:
            print("Enter Valid Phone Number")
            return
        cursor.execute("INSERT INTO contact (name,phone) VALUE (%s,%s)",(name,phone))
        connectionObj.commit()
        print("Contact Added")
    except connector.errors.IntegrityError:
        print("Invalid Contact Details")
    except Exception:
        print("Something went Wrong")

    

while True:
    inp=int(input("0 --> Exit\n1 --> Add Contact\n2 --> See All Contact\n3 --> Update a Contact\n4 --> Delete a Contact\n\nChoose an Option: "))

    if inp==0:
        break
    elif inp==1:
        addContact()
    elif inp==2:
        viewAllContact()
    elif inp==3:
        #id 
        pass
    elif inp==4:
        pass
    else:
        print("Please select an appropriate option...!")

# Django

#Client --->API---> server() --> MySQL servr