import tkinter as tk 

def create_app(approot,current_time,vote):
    #draws label to add details
    user = tk.Label(approot,text = "       Full Name:    ",bg = '#AEC6CF',fg = 'white',padx = 1.5)
    phno = tk.Label(approot,text = " Phone Number: ",bg = '#AEC6CF',fg = 'white',padx = 2)
    voteno = tk.Label(approot,text = "VoterID Number: ",bg = '#AEC6CF',fg = 'white')
    age = tk.Label(approot,text = "Age:  ",bg = '#AEC6CF',fg = 'white',padx = 32)
    user.grid()
    phno.grid()
    voteno.grid()
    age.grid()
    username = tk.StringVar()
    phonenumber = tk.StringVar()
    voterid = tk.IntVar()
    age = tk.IntVar()

    #Takes input
    usernameentry = tk.Entry(approot,textvariable = username,bg = '#C8A2C8',fg = 'white')
    phonenumberentry = tk.Entry(approot,textvariable = phonenumber,bg = '#C8A2C8',fg = 'white')
    voteridentry = tk.Entry(approot,textvariable = voterid,bg = '#C8A2C8',fg = 'white')
    ageentry = tk.Entry(approot,textvariable = age,bg = '#C8A2C8',fg = 'white')
    usernameentry.grid(column = 1,row = 0)
    phonenumberentry.grid(column = 1,row = 1)
    voteridentry.grid(column = 1,row = 2)
    ageentry.grid(column = 1,row = 3)

    #draws label to select party
    votelabel = tk.Label(approot,text = 'Select the political party: ',bg = '#242B2E',fg = 'white')
    votelabel.grid(column = 0,row = 10)

    bjpvariable = tk.StringVar()
    bjpbutton = tk.Button(approot, textvariable = bjpvariable,bg = '#FFB347',fg = 'white',padx = 22, command=lambda : vote(approot,current_time,"bjp",phonenumberentry,usernameentry,ageentry,voteridentry))
    bjpvariable.set("BJP")
    bjpbutton.grid(column = 0,row = 32)

    aapvariable = tk.StringVar()
    aapbutton = tk.Button(approot, textvariable = aapvariable,bg = 'darkgrey',fg = 'white',padx = 19,command=lambda : vote(approot,current_time,"aap",phonenumberentry,usernameentry,ageentry,voteridentry))
    aapvariable.set("AAP")
    aapbutton.grid(column = 0 ,row = 12)

    congvariable = tk.StringVar()
    congbutton = tk.Button(approot, textvariable = congvariable,bg = "lightgreen",fg = 'white',padx = 1,command=lambda : vote(approot,current_time,"congress",phonenumberentry,usernameentry,ageentry,voteridentry))
    congvariable.set("CONGRESS")
    congbutton.grid(column = 0,row = 42)