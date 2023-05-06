from cryptography.fernet import Fernet


def generate_key ():
    key = Fernet.generate_key()
    with open ("key.key","wb")as key_file :
        key_file.write(key)

def local_key() :
    file= open("key.key" , "rb") 
    key = file.read()
    file.close()
    return key


key = local_key() 
fer =Fernet(key)

def view():
    with open('password.txts', 'r')as file :
        for line in file.readlines():
            data =line.rstrip()
            user,passc = data.split("|")
            print("User acc :" , user , " | password :" ,
                  (fer.decrypt(passc.encode())).decode())
            


def add():
    name = input('Account name: ')
    password =input('Password :')

    with open ('password.txts', 'a')as file:
        file.write(name + "|" + (fer.encrypt(password.encode())).decode()  + "\n")
        
while True :
        
    ask =(input('would to like to add new password or view existing ones? [add or view] or q to quit  :')).lower()

    if ask =='q' :
        break

    if ask == 'add' :
        add()

    elif ask == 'view':
        view()

    else :
        print('Invlid Input...Try again')
        print ()
        continue