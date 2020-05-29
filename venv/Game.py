# Rock Paper Scissor using Python Tkinter
# Author: Shekhar Adhikari
# This is my original work


import random
from tkinter import *  # importing everything
import tkinter.messagebox as mb
from PIL import Image, ImageTk

class Game:
    def __init__(self, master):  # everything is store inside the master
        self.master = master


        master.title("Rock, Paper, Scissor - Shekhar")
        master.geometry('900x800+580+150')
        master.resizable(width=FALSE, height=FALSE)
        master.configure(bg='Light Green')
        master.label = Label(master, text='Are you ready to play?', fg="BLACK", bg="RED",
                             font=("Times New Roman", 16, 'bold', 'italic', 'underline'))
        master.label.pack(pady=25, padx=4, side=TOP)
        master.label = Label(master, text="Choose between Rock, Paper and Scissor!", fg="BLACK", bg="RED",
                             font=("Times New Roman", 16, 'bold', 'italic'))
        master.label.pack(pady=25, padx=3, side=TOP)

        self.player_choices = ["Rock","Paper","Scissor"]
        # Exit Button - to exit the game
        self.quitButton = Button(master, text="Exit the game!", fg="BLACK", bg="SKY BLUE",
                                 font=("Times New Roman", 16, 'bold'), command=master.quit)
        self.quitButton.pack(side=BOTTOM, anchor=S, padx=100, pady=70)

        # To print the message on screen for computer
        self.message = StringVar()
        self.message_label = Message(master,width=-20, textvariable=self.message, justify=LEFT, bg='YELLOW', borderwidth=2)
        self.message.set('Are you Ready?')
        self.message_label.pack(side=BOTTOM, anchor=W, padx=24, pady=0)

        # reset score button
        self.resetButton = Button(master, text="Reset", fg="BLACK", bg="SKY BLUE", font=("Times New Roman", 16, 'bold'),
                                  command=self.reset_rules)
        self.resetButton.pack(side=BOTTOM, anchor=SW, padx=20, pady=10)

        # score card for computer

        self.computer_score = IntVar(master,value=0)
        self.computer_score_keeper = Entry(master, width=6, state=DISABLED, disabledbackground="white", justify=CENTER,
                                           textvariable=self.computer_score)
        self.computer_score_Label = Label(master, text='Computer Score', fg='RED')
        self.computer_score_keeper.pack(side=BOTTOM, pady=0, padx=30, anchor=SW)
        # self.computer_score_keeper.bind("<Key>", "pass")
        self.computer_score_Label.pack(side=BOTTOM, pady=5, padx=4, anchor=SW)

        # score cared for user

        self.user_score = IntVar(master, value=0)
        self.user_score_keeper = Entry(master, width=6, state=DISABLED, disabledbackground="white", justify=CENTER,
                                       textvariable=self.user_score)
        self.user_score_Label = Label(text='User Score', fg='RED')
        self.user_score_keeper.pack(side=BOTTOM, pady=0, padx=30, anchor=SW)
        self.user_score_Label.pack(side=BOTTOM, pady=5, padx=18, anchor=SW)

        # Button for Rock
        self.Rock = Image.open("rock.png")
        self.photo_Rock = ImageTk.PhotoImage(self.Rock)
        self.Rock_btn = Button(master, text='1',image=self.photo_Rock,command=self.user_choice_rock)
        #self.Rock_btn.bind("<Button>",self.rock_rules(event=FIRST))
        self.Rock_btn.setvar(name='Rock_Button', value='Rock')
        # self.Rock_button.getvar(name="Button")
        self.Rock_btn.pack(side=LEFT, padx=45, pady=10, anchor=NW)


        # Button for Paper
        self.Paper = Image.open("paper.png")
        self.photo_paper = ImageTk.PhotoImage(self.Paper)
        self.paper_btn = Button(master, image=self.photo_paper,command=self.user_choice_paper)
        #self.paper_btn.bind("<Button>",self.paper_rules)
        self.paper_btn.setvar(name='Paper_Button', value='Paper')
        self.paper_btn.pack(side=LEFT, padx=45, pady=10, anchor=N)
        # print(self.paper_btn.getvar(name='Paper_Button'))

        # Button for Scissor
        self.Scissor = Image.open("scissor.png")
        self.photo_Scissor = ImageTk.PhotoImage(self.Scissor)
        self.scissor_btn = Button(master, image=self.photo_Scissor,command=self.user_choice_scissor)
        #self.scissor_btn.bind("<Button-1>",self.scissor_rules)
        self.scissor_btn.setvar(name='Scissor_Button', value='Scissor')
        self.scissor_btn.pack(side=LEFT, padx=45, pady=10, anchor=NE)
        # print(self.scissor_btn.getvar(name='Scissor_Button'))


        #global is helpful because we can use it inside the function and does not need to be locally.
        #Her we are just extracting the value of the button using get and set methods(just playing around)
        global Button1_Rock
        Button1_Rock = self.Rock_btn.getvar(name='Rock_Button')


        global Button2_Paper
        Button2_Paper = self.paper_btn.getvar(name='Paper_Button')


        global Button3_Scissor
        Button3_Scissor = self.scissor_btn.getvar(name='Scissor_Button')

        global Array
        Array = [Button1_Rock,Button2_Paper,Button3_Scissor]
        #using gloval variable called counter inside function to test it
        global counter
        counter = 0
        counter += 1

    #Here we are using global variable inside the function which is named Array just
    #to play around and global counter to set the increment and store inside the entry box:
    def user_choice_rock(self):
        new_choice = Array
        new_choice = random.choice(new_choice)
        print('When you clicked on Rock, what did you get?' + "" + new_choice)
        if new_choice == 'Rock':
            self.message.set('\nIt is a tie\n' 'Both selected Rock\n')
        elif new_choice == 'Scissor':
            self.message.set('Computer:' + ' ' + new_choice + ' ' + 'User:Rock\n' + ' ' '\n\n     User wins')
            self.user_score.set(self.user_score.get() + counter)
        else:
            new_choice == 'Paper'
            self.computer_score.set(self.computer_score.get() + 1)
            self.message.set('Computer:' + ' ' + new_choice + ' ' + 'User:Rock\n' + ' ' '\n\n Computer wins')

    def user_choice_paper(self):
        new_choice = self.player_choices
        new_choice = random.choice(new_choice)
        print('When you clicked on Paper, what did you get?' + "" + new_choice)

        if new_choice == 'Paper':
            self.message.set('\nIt is a tie\n' 'Both selected Paper\n')

        elif new_choice == 'Scissor':
            self.computer_score.set(self.computer_score.get() + 1)
            self.message.set('Computer:' + ' ' + new_choice + ' ' + 'User:Paper\n' + ' ' '\n\n Computer wins')

        else:
            new_choice == 'Rock'
            self.user_score.set(self.user_score.get() + 1)
            self.message.set('Computer:' + ' ' + new_choice + ' ' + 'User:Paper\n' + ' ' '\n\n     User wins')

    def user_choice_scissor(self):
        new_choice = self.player_choices
        new_choice = random.choice(new_choice)
        print('When you clicked on Paper, what did you get?' + "" + new_choice)

        if new_choice == 'Scissor':
            self.message.set('\nIt is a tie\n' 'Both selected Scissor\n')
        elif new_choice == 'Paper':
            self.user_score.set(self.user_score.get() + 1)
            self.message.set('Computer:' + ' ' + new_choice + ' ' + 'User:Scissor\n' + ' ' '\n\n User wins')

        else:
            new_choice == 'Rock'
            self.computer_score.set(self.computer_score.get() + 1)
            self.message.set('Computer:' + ' ' + new_choice + ' ' + 'User:Scissor\n' + ' ' '\n\n     Computer wins')

    ## To reset the score card
    def reset_rules(self):
        value_for_computer = self.computer_score.get()
        value_for_user = self.user_score.get()
        if value_for_computer > 0 or value_for_user > 0:
            self.computer_score.set(value=0)
            self.user_score.set(value=0)
        else:
            pass
    #def on_closing():
    #msgbox= mb.askquestion('You have been pranked! haha')
    #if msgbox == 'yes':
        #pass
    #else:
        #root.destroy()

root = Tk()
#root.protocol("WM_DELETE_WINDOW",on_closing) #this is how you closed ok learned one knew cool thing
my_gui = Game(root) #everything is stored here
root.mainloop()


