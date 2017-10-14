import tkinter
import random

#prime part

def pri(n):

    #sqrt
    def sqt(n):
        a,b=n,1.0

        for i in range (11):
            a=(a+b)/2.0
            b=n/a
        return b

    def pr(n):

     #exceptions
        if n in [2,3]:
            print ("yes\n\n")
            

        elif (n%2==0):
            print ("no\n\n")
            


        else:
            m=int(sqt(n)) + 2
            for i in range (3,m,2):
                print ("count: ",i)
                if (n%i==0.0):
                    print (n/i,"here")
                    print ("no\n\n")
                    break
                    
                elif (i==m-1) or (i==m-2):
                    print ("yes\n\n")
                    break
                
    pr(n)
                    



#create a new window

win = tkinter.Tk()

win.title('prime')
win.geometry('250x85')
lab=tkinter.Label(win,text='click and enter number above',bg='#0099ff', font = '11')

#text entry and pack to window

ent=tkinter.Entry(win)
ent.pack()

#defining button command

def butpr():
    a=int(ent.get())
    pri(a)

but=tkinter.Button(win,text='check', font = '11', command = butpr,fg='#a1dbcf',bg='#383a39')

#packing all

lab.pack()
ent.pack()
but.pack()

#background
win.configure(background='#a1bdcd')


win.mainloop()





