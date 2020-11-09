from tkinter import *
from random import randint#RANDOMIZE
root=Tk()
root.title("Random Winner Generator")
root.geometry('400x400')

def pick():
    entries=['Hrithik','Roshan','Google India','Saad','as','sdkhjhfgsd','sd;ljkfknhsd','sldjfjgb','ewpihad','dskjfugewu','sdjfjhsd','sdljfhho','dslkfjgaedu','sadsdoluf','eufgj','s;dfjd','as;dja','kesoifh','sdljf','.ljfbhsh','dsfwerg','dsfsd','swrewf','dsfert','ffgsrg','sdf',]
    #converting to set to remove the duplicate names & then converting back to list
    #SETS DO NOT HAVE INDEX NUMBERS
    entries_set=set(entries)
    unique_entries=list(entries_set)

    #creating a randomnumber before zero and 25

    rando=randint(0,25)

    winlabel=Label(root,text=unique_entries[rando],font=("Helvetica",20))
    winlabel.pack(pady=20)


toplabel=Label(root,text='Win-O-Rama',font=("Helvetica",20))
toplabel.pack(pady=20)

winbtn=Button(root,text="Pick A Winner",font=("Helvetica",20),command=pick)
winbtn.pack(pady=20)


root.mainloop()