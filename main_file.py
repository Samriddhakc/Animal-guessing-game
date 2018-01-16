from tkinter import *
from Object_A16 import *

class Animal_guessing_GUI:

    def __init__(self, master):

        self.master = master
        self.object_file=animal_guessing_implementation()

    def update_text_box_yes(self,display_lab):

        self.object_file.yes_button()
        display_lab['text']=self.object_file.data()
        display_lab.grid(row=4,column=20)
        string=self.object_file.data()
        if string[-2]=="?":
            return
        elif string[-2]!="?" or string[-2]!="!":
            length=len(string)-2
            imp=""
            while string[length]!=" ":
                imp=string[length]+imp
                length=length-1
            print(imp+".gif")
            self.display_image(imp+".gif")

    def update_text_box_no(self,display_lab):

        self.object_file.no_button()
        display_lab['text']=self.object_file.data()
        display_lab.grid(row=20,column=20)
        if self.object_file.data()=="execute":
            display_lab['text']="What is the animal that you guessed and what would question would allow the AI to make the correct guess?"
            display_lab.config(font=("Courier",12))
            display_lab.grid(row=30, column=20)
            Label(self.master, text="Enter the animal you guessed here").grid(row=80, column=20)
            e1=Entry(self.master)
            e1.grid(row=100,column=20)
            Label(self.master, text="Enter the question here").grid(row=120, column=20)
            e2 = Entry(self.master)
            e2.grid(row=200,column=20)
            ok_button= Button(self.master, text="OK",command= lambda: self.ok(e1.get(),e2.get()))
            ok_button.grid(row=300,column=20)


    def ok(self,e1_data,e2_data):
        self.object_file.node_creator(" "+e1_data+"\n",e2_data+"\n")
        Label(self.master, text="Thanks for sharing.").grid(row=100, column=20)
        Label(self.master,text="Upload a picture to the file in the format and name in which other pictures are used to store other pictures").grid(row=300, column=20)


    def display_image(self,path):
        self.master.title("Join")
        self.master.geometry("300x300")
        picture=PhotoImage(file=path,format="gif")
        self.master.configure(background='grey')  #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        panel = Label(self.master, image = picture)  #The Pack geometry manager packs widgets in rows or columns.
        panel.image=picture
        panel.grid(row=50,column=50)


def main():

    '''Using Tkinter to show library'''

    root = Tk()
    title_text="WELCOME TO THE ANIMAL GUESSING GAME"
    root.title("WELCOME TO THE ANIMAL GUESSING GAME")
    label = Label(root, text=title_text)
    label.config(font=("Courier",20))
    label.grid(row=1,column=30)
    my_gui = Animal_guessing_GUI(root)
    object=animal_guessing_implementation()
    display_label=Label(root, text=object.data())
    display_label.config(font=("Courier",20))
    display_label.grid(row=5,column=20)
    yes_button = Button(root, text="YES",command= lambda:my_gui.update_text_box_yes(display_label))
    yes_button.grid(row=50, column=30)
    no_button= Button(root, text="NO",command= lambda: my_gui.update_text_box_no(display_label))
    no_button.grid(row=50, column=35)
    close_button=Button(root, text="CLOSE", command=root.quit)
    close_button.grid(row=100, column=40)
    mainloop()

main()
