from tkinter import *
import time
currenttime = time.ctime()

# with open("F:\\python_everything\\Personal_Projects\\records.txt",'w') as record:
#     final = record.write()
approot = Tk()

# Width x height
approot.geometry("300x300")

# width,height
approot.minsize(300,300)
approot.maxsize(300,300)
approot.title("NVC-2021")
approot.configure(bg = '#FDFD96')
# Label(approot,text = 'hello').grid(row = 0,column = 0)
# Label(approot,text = "E L E C T I O N  2 0 2 1",bg = "black",fg = "yellow",padx = 7,font = ("bebasneue",20,"bold"),borderwidth = 5, relief = SUNKEN).grid(row = 0,column = 0)


def congress():
    # phone number part
    if len(phonenumberentry.get()) == 10:
        print("Your mobile number is: ","+",91,phonenumberentry.get())
    else:
        print("[ERRORx00]:Please Enter a Correct Indian Number")
        Label(approot,text = "[ERRORx00]:Please Enter a Correct Indian Number.",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)
        
    if usernameentry.get() == "":
        print("[ERRORx01]:Incorrect name entered!")
        Label(approot,text = "[ERRORx01]:Incorrect name entered!",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)
    

    if(int(voteridentry.get())>=2020 and int(ageentry.get())>=18 and (len(phonenumberentry.get()) == 10)  and (usernameentry.get() != "")):
        print("THANK YOU",usernameentry.get(),"\nYou Voted CONGRESS")
        with open("F:\\python_everything\\personal_data\\votingGUI\\records.txt",'a') as record:
            final = record.write("\n"+currenttime+": "+usernameentry.get()+" Voted CONGRESS.")
            
        
        Label(approot,text = "THANK YOU "+ usernameentry.get()+"\nYou Voted CONGRESS",fg = 'blue',bg = '#FDFD96').grid(row = 70,column = 0)
        time.sleep(1.0)
        
    if(int(ageentry.get())<17 and int(voteridentry.get())<2020):
        print("[ERRORx001]:INCORRECT ID and you are not eligible since you are not greater than 18 years.")
        Label(approot,text = "[ERRORx001]:INCORRECT ID and you are not eligible since you are not greater than 18 years.",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)
    elif(int(ageentry.get())<17):
        print("[ERRORx002]:You are not eligible.")
        Label(approot,text = "[ERRORx002]:You are not eligible.",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)
    elif (int(voteridentry.get())<2020):
        print("[ERRORx003]:INCORRECT ID!")
        Label(approot,text = "[ERRORx003]:INCORRECT ID!",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)
   


def bjp():
    # phone number part
    if len(phonenumberentry.get()) == 10:
        print("Your mobile number is: ","+",91,phonenumberentry.get())
    else:
        print("[ERRORx00]:Please Enter a Correct Indian Number")
        Label(approot,text = "[ERRORx00]:Please Enter a Correct Indian Number.",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)
    if usernameentry.get() == "":
        print("[ERRORx01]:Incorrect name entered!")
        Label(approot,text = "[ERRORx01]:Incorrect name entered!",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)
    

    if(int(voteridentry.get())>=2020 and int(ageentry.get())>=18 and (len(phonenumberentry.get()) == 10)  and (usernameentry.get() != "")):
        print("THANK YOU",usernameentry.get(),"\nYou Voted BJP")
        with open("F:\\python_everything\\personal_data\\votingGUI\\records.txt",'a') as record:
            final = record.write("\n"+currenttime+": "+usernameentry.get()+" Voted BJP.")
        time.sleep(1.0)
        
        Label(approot,text = "THANK YOU "+ usernameentry.get()+"\nYou Voted BJP",fg = 'blue',bg = '#FDFD96').grid(row = 70,column = 0)
        # exit()
    if(int(ageentry.get())<17 and int(voteridentry.get())<2020):
        print("[ERRORx001]:INCORRECT ID and you are not eligible since you are not greater than 18 years.")
        Label(approot,text = "[ERRORx001]:INCORRECT ID and you are not eligible since you are not greater than 18 years.",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)
    elif(int(ageentry.get())<17):
        print("[ERRORx002]:You are not eligible.")
        Label(approot,text = "[ERRORx002]:You are not eligible.",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)
    elif (int(voteridentry.get())<2020):
        print("[ERRORx003]:INCORRECT ID!")
        Label(approot,text = "[ERRORx003]:INCORRECT ID!",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)
   
def aap():
    # phone number part
    if len(phonenumberentry.get()) == 10:
        print("Your mobile number is: ","+",91,phonenumberentry.get())
    else:
        print("[ERRORx00]:Please Enter a Correct Indian Number.")
        Label(approot,text = "[ERRORx00]:Please Enter a Correct Indian Number",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)
        # exit()
    if usernameentry.get() == "":
        print("[ERRORx01]:Incorrect name entered!")
        Label(approot,text = "[ERRORx01]:Incorrect name entered!",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)
    

    if(int(voteridentry.get())>=2020 and int(ageentry.get())>=18 and (len(phonenumberentry.get()) == 10)  and (usernameentry.get() != "")):
        print("THANK YOU",usernameentry.get(),"\nYou Voted AAP")
        with open("F:\\python_everything\\personal_data\\votingGUI\\records.txt",'a') as record:
            final = record.write("\n"+currenttime+": "+usernameentry.get()+" Voted AAP.")
        Label(approot,text = "THANK YOU "+ usernameentry.get()+"\nYou Voted AAP",fg = 'blue',bg = '#FDFD96').grid(row = 70,column = 0)
        time.sleep(1.0)
        
    if(int(ageentry.get())<17 and int(voteridentry.get())<2020):
        print("[ERRORx001]:INCORRECT ID and you are not eligible since you are not greater than 18 years.")
        Label(approot,text = "[ERRORx001]:INCORRECT ID and you are not eligible since you are not greater than 18 years.",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)
        
    elif(int(ageentry.get())<17):
        print("[ERRORx002]:You are not eligible.")
        Label(approot,text = "[ERRORx002]:You are not eligible.",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)
    elif (int(voteridentry.get())<2020):
        print("[ERRORx003]:INCORRECT ID!")
        Label(approot,text = "[ERRORx003]:INCORRECT ID!",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)
   

user = Label(approot,text = "       Full Name:    ",bg = '#AEC6CF',fg = 'white',padx = 1.5)
phno = Label(approot,text = " Phone Number: ",bg = '#AEC6CF',fg = 'white',padx = 2)
voteno = Label(approot,text = "VoterID Number: ",bg = '#AEC6CF',fg = 'white')
age = Label(approot,text = "Age:  ",bg = '#AEC6CF',fg = 'white',padx = 32)
user.grid()
phno.grid()
voteno.grid()
age.grid()
username = StringVar()
phonenumber = StringVar()
voterid = IntVar()
age = IntVar()
usernameentry = Entry(approot,textvariable = username,bg = '#C8A2C8',fg = 'white')
phonenumberentry = Entry(approot,textvariable = phonenumber,bg = '#C8A2C8',fg = 'white')
voteridentry = Entry(approot,textvariable = voterid,bg = '#C8A2C8',fg = 'white')
ageentry = Entry(approot,textvariable = age,bg = '#C8A2C8',fg = 'white')
usernameentry.grid(column = 1,row = 0)
phonenumberentry.grid(column = 1,row = 1)
voteridentry.grid(column = 1,row = 2)
ageentry.grid(column = 1,row = 3)

votelabel = Label(approot,text = 'Select the political party: ',bg = '#242B2E',fg = 'white')
votelabel.grid(column = 0,row = 10)

bjpvariable = StringVar()
bjpbutton = Button(approot, textvariable = bjpvariable,bg = '#FFB347',fg = 'white',padx = 22,command = lambda:bjp())
bjpvariable.set("BJP")
bjpbutton.grid(column = 0,row = 32)

aapvariable = StringVar()
aapbutton = Button(approot, textvariable = aapvariable,bg = 'darkgrey',fg = 'white',padx = 19,command = lambda:aap())
aapvariable.set("AAP")
aapbutton.grid(column = 0 ,row = 12)

congvariable = StringVar()
congbutton = Button(approot, textvariable = congvariable,bg = "lightgreen",fg = 'white',padx = 1,command = lambda:congress())
congvariable.set("CONGRESS")
congbutton.grid(column = 0,row = 42)

approot.mainloop()
