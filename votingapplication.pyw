import tkinter
import time
from drawscreen import create_app
currenttime = time.ctime()

#config 
approot = tkinter.Tk()

# Width x height
approot.geometry("300x300")

# width,height,set title
approot.minsize(300,300)
approot.maxsize(300,300)
approot.title("NVC-2021")
approot.configure(bg = '#FDFD96')

#draws the screen
create_app(approot)

#created main loop 
approot.mainloop()