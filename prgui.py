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
            lab.configure(text='yes\n')
            

        elif (n%2==0):
            print ("no\n\n")
            lab.configure(text='no\n')
            


        else:
            m=int(sqt(n)) + 2
            for i in range (3,m,2):
                print ("count: ",i)
                if (n%i==0.0):
                    print (n/i,"here")
                    print ("no\n\n")
                    lab.configure(text='no\n')
                    break
                    
                elif (i==m-1) or (i==m-2):
                    print ("yes\n\n")
                    lab.configure(text='yes\n')
                    break
                
    pr(n)
                    



#create a new window

win = tkinter.Tk()

win.title('prime')
win.geometry('250x170')
lab=tkinter.Label(win,text='enter number above to check \n if number is prime',bg='#ffffff', font = ('Helvetica', 13), justify = 'center')

 
#text entry and pack to window

ent=tkinter.Entry(win, font=('DejaVu Sans',15), justify = 'right', bg='#ffffff')


#defining button command

def butpr():
    a=int(ent.get())
    pri(a)

but1=tkinter.Button(win,text='check', font = ('Helvetica', 13), justify = 'right', command = butpr,fg='#000000',bg='#ffffff', width = 9)
but2=tkinter.Button(win, text='quit', font = ('Helvetica',13), command = win.destroy, fg='#000000',bg='#ffffff', width = 9)

#packing all


ent.pack(fill=tkinter.X)
but1.pack()
lab.pack()
but2.pack()

#background
win.configure(background='#ffffff')


win.mainloop()


 


