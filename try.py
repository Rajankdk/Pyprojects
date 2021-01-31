
from tkinter import *
from functools import partial
from babandar import process

def value(ip,port,pan, terminal, Mti, acquirer, currency, source, destination):
    ip=ip.get()
    port=port.get()
    pan = pan.get()
    terminal = terminal.get()
    Mti = Mti.get()
    acquirer = acquirer.get()
    currency = currency.get()
    source = source.get()
    destination = destination.get()

    prcs = process()
    for i in range(0, 5):
        prcs.isomaking(ip,port,pan, terminal, Mti, acquirer, currency, source, destination,'350000') #400000
    for i in range(0, 5):
        prcs.isomaking(ip,port,pan, terminal, Mti, acquirer, currency, source, destination,'400000')
    for i in range(0, 5):
        prcs.isomaking(ip,port,pan, terminal, Mti, acquirer, currency, source, destination,'301000')



def valuepass(pan, terminal, Mti, acquirer, currency, source, destination):
    print(pan, terminal, Mti, acquirer, currency, source, destination)

    '''print("username entered :", username.get())
	#print("password entered :", password.get())
	#return'''


# window
tkWindow = Tk()
tkWindow.geometry('400x400')
# tkWindow.configure(background="white");
tkWindow.title('MG Simulator')

# username label and text entry box
iplbl = Label(tkWindow, text="-").grid(row=8, column=8)
ip = StringVar()
IpEntry = Entry(tkWindow, textvariable=ip).grid(row=8, column=3)

portlbl = Label(tkWindow, text="T").grid(row=9, column=3)
port = StringVar()
portEntry = Entry(tkWindow, textvariable=port).grid(row=9, column=3)

panlbl = Label(tkWindow, text="enter pan no").grid(row=0, column=0)
pan = StringVar()
panEntry = Entry(tkWindow, textvariable=pan).grid(row=0, column=1)

Mtilbl = Label(tkWindow, text="Mti").grid(row=1, column=0)
Mti = StringVar()
MtiEntry = Entry(tkWindow, textvariable=Mti).grid(row=1, column=1)

acquirerLbl = Label(tkWindow, text="enter acquirerid:").grid(row=2, column=0)
acquirer = StringVar()
acquirerEntry = Entry(tkWindow, textvariable=acquirer).grid(row=2, column=1)

terminalLbl = Label(tkWindow, text="enter Terminalid:").grid(row=3, column=0)
terminal = StringVar()
terminalEntry = Entry(tkWindow, textvariable=terminal).grid(row=3, column=1)

currencyLbl = Label(tkWindow, text="enter currency code:").grid(row=4, column=0)
currency = StringVar()
currencyEntry = Entry(tkWindow, textvariable=currency).grid(row=4, column=1)

sourceLbl = Label(tkWindow, text="enter source account:").grid(row=5, column=0)
source = StringVar()
sourceEntry = Entry(tkWindow, textvariable=source).grid(row=5, column=1)

DestinationLbl = Label(tkWindow, text="Destination account:").grid(row=6, column=0)
destination = StringVar()
destinationEntry = Entry(tkWindow, textvariable=destination).grid(row=6, column=1)
# password label and password entry box
# passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)
# password = StringVar()
# passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

value = partial(value,ip, port, pan, terminal, Mti, acquirer, currency, source, destination)

# login button

loginButton = Button(tkWindow, text="SEND", command=value).grid(row=9, column=7)


tkWindow.mainloop()



