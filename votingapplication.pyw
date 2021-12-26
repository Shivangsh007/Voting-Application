import tkinter
import time
from drawscreen import create_app
from util import vote_party
current_time = time.ctime()

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
create_app(approot,current_time,vote_party)

#created main loop 
approot.mainloop()