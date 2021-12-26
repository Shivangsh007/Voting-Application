import tkinter
import time

def vote_party(approot,current_time,party,phonenumberentry,usernameentry,ageentry,voteridentry):
    #phone number verification
    if len(phonenumberentry.get()) == 10:
        print("Your mobile number is: ","+",91,phonenumberentry.get())
    else:
        print("[ERRORx00]:Please Enter a Correct Indian Number")
        tkinter.Label(approot,text = "[ERRORx00]:Please Enter a Correct Indian Number.",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)

    #username verification 
    if usernameentry.get() == "":
        print("[ERRORx01]:Incorrect name entered!")
        tkinter.Label(approot,text = "[ERRORx01]:Incorrect name entered!",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)

    #successful voting 
    if(int(voteridentry.get())>=2020 and int(ageentry.get())>=18 and (len(phonenumberentry.get()) == 10)  and (usernameentry.get() != "")):
        print("THANK YOU",usernameentry.get(),"\nYou Voted", party)
        with open("records.txt",'a') as record:
            final = record.write("\n"+current_time+": "+usernameentry.get()+" Voted "+ party)
        tkinter.Label(approot,text = "THANK YOU "+ usernameentry.get()+"\nYou Voted " + party,fg = 'blue',bg = '#FDFD96').grid(row = 70,column = 0)
        time.sleep(1.0)

    #id and age verification
    if(int(ageentry.get())<17 and int(voteridentry.get())<2020):
        print("[ERRORx001]:INCORRECT ID and you are not eligible since you are not greater than 18 years.")
        tkinter.Label(approot,text = "[ERRORx001]:INCORRECT ID and you are not eligible since you are not greater than 18 years.",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)
    elif(int(ageentry.get())<17):
        print("[ERRORx002]:You are not eligible.")
        tkinter.Label(approot,text = "[ERRORx002]:You are not eligible.",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)
    elif (int(voteridentry.get())<2020):
        print("[ERRORx003]:INCORRECT ID!")
        tkinter.Label(approot,text = "[ERRORx003]:INCORRECT ID!",fg = 'red',bg = '#FDFD96').grid(row = 70,column = 0)