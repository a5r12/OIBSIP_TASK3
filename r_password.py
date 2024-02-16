import random
import string
from tkinter import *


main = Tk()
main.title("Password Generator")
main.geometry("350x350")
main.configure(background= 'black') 

latter_len = IntVar()
digit_len = IntVar()
symbol_len = IntVar()
password_ = StringVar()


def random_password():
    char_l=  string.ascii_letters       # all the upercase and lowercase letters
    char_d = string.digits              # all the digits
    char_s= string.punctuation          # all the punctuation characters

    password = ""       # empty string

    for i in range(0,latter_len.get()):
        password = password + random.choice(char_l)    # it takes given num of latter randomly and add into empty password string

    for i in range(0,digit_len.get()):
        password = password + random.choice(char_d)    # it takes given num of digits randomly and add into empty password string

    for i in range(0,symbol_len.get()):
        password = password + random.choice(char_s)    #it takes given num of punctuation randomly and add into empty password string

    p= list(password) # temporary list to suffle the password

    random.shuffle(p) # functon shuffle the list p randomly

    password_.set(''.join(p)) # we want the string type password , so we use '.join' to modify the list p as final output


        
# labbel for num of latters
Label(main,text=" Enter num of latters you want :", fg='silver', bg='black').pack(padx=5,pady=5)
Entry(main,textvariable= latter_len, fg='blue', font='bold').pack()

# labbel for num of digits
Label(main,text="  Enter num of Digits you want :", fg='silver', bg='black').pack(padx=5,pady=5)
Entry(main,textvariable= digit_len, fg='blue', font='bold').pack()

# labbel for num of punctuation
Label(main,text="  Enter num of punctuations you want :", fg='silver', bg='black').pack(padx=5,pady=5)
Entry(main,textvariable= symbol_len, fg='blue', font='bold').pack()

# button for 'Generate Password'
Button(main,text='Generate Password',command=random_password,bg='silver', fg='black').pack(pady=15,ipadx=2,ipady=2)

# output box 
Entry(main,textvariable=password_, bg='white',fg='blue',font='bold').pack(ipadx=5,ipady=5)


main.mainloop()