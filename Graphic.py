"""
Defines all the Frames used in the Project
@author: Aakash Maurya
"""

from re import match
from tkinter import *
from tkinter import Label, Frame, PhotoImage, StringVar
from User import MainUser
from Dictionary import English, StrToPara
from Bot import AppBot

class StartPage(Frame):
    def __init__(self, parent):
        Frame.__init__(self, bg='#66B2FF', width=500, height=800)
        self.Parent = parent
        
        Screen = Frame(self, bg='#66B2FF', width=500, height=800)
        Screen.place(x=0,y=0)
        Screen.bind("<Button-1>",self.Next)
        
        self.logo = PhotoImage(file="images/logo.png")
                
        Logo = Label(self, bg='#66B2FF', image=self.logo)
        Logo.place(relx=.5, rely=.45, anchor="center")
        Logo.bind("<Button-1>",self.Next)
        
        Status = "Welcome To The ChatBot App"
        if MainUser.UserPresent == True:
            Status = "Welcome " + MainUser.getName().title()

        Name = Label(self, bg='#66B2FF', text=Status, width=25, font=("", 18, "italic"))
        Name.place(relx=.5, rely=.67, anchor="center")
        Name.bind("<Button-1>",self.Next)
        
        Info = Label(self, bg='#66B2FF', text="TAP ANYWHERE TO CONTINUE", font=("", 10, "italic"))
        Info.place(relx=.5, rely=.75, anchor="center")
        Info.bind("<Button-1>",self.Next)


    def Next(self, event):
        if MainUser.UserPresent == False:
            self.Parent.Switch(SignUp)
        else:
            self.Parent.Switch(MainActivity)


class SignUp(Frame):
    def __init__(self, parent):
        Frame.__init__(self, width=500, height=800)
        self.Parent = parent
        self.PageNo = 0
        self.NewUser = ["", "", "", "", ""]
        
        Screen = Frame(self, bg='#FF9933', width=500, height=800)
        Screen.place(x=0,y=0)
        Screen.focus_set()
        Screen.bind("<Button-1>", self.Next)
        Screen.bind("<Key>", self.Input)
        
        self.logo = PhotoImage(file="images/logo.png")
        self.logo = self.logo.subsample(5,5)
                
        Logo = Label(self, bg='#FF9933', image=self.logo)
        Logo.place(x=10, y=10)
        Logo.bind("<Button-1>",self.Next)
        
        self.Lines = ["Hello, My Name is Lucia.",
                      "I Am A ChatBot, Just For You.",
                      "If You Have Come Across \nAny Problem in English,\n\n\nWhere You Don't Know \nThe Meaning of Any Word,",
                      "Just Ask Me,\n\nI Am Always Ready \nTo Answer Your Questions",
                      "But First, \nHow About We Start With You\n\nWould You Tell Me Your Name ?",
                      "So, {}, \nAre you a Male or Female ?",
                      "Would You Also Tell Me Your Age Please",
                      "Hmm, {} Years... ,\n\n{}",
                      "We're Almost Done, But Almost\nCan You Please Share Your Email ID",
                      "Oh,\n\nAnd Your Phone No. May Also Be Useful",
                      "And Now, We Are Done.\n\nThank You For Your Time"]
        
        self.Text = StringVar()
        self.Data = StringVar()
        self.Text.set(self.Lines[0])
        
        Intro = Label(self, bg='#FF9933', textvariable=self.Text, font=("", 18, "bold"))
        Intro.place(relx=.5, rely=.5, anchor="center")
        Intro.bind("<Button-1>", self.Next)
        
        self.tip = StringVar()
        self.tip.set("Tap Anywhere")
        self.Hint = Label(self, bg='#FF9933', textvariable=self.tip, font=("", 10, "italic"))
        self.Hint.place(relx=.5, rely=.95, anchor='center')
        self.Hint.bind("<Button-1>", self.Next)


    def Next(self, event):
        if self.PageNo < 3:
            self.PageNo += 1
            self.Text.set(self.Lines[self.PageNo])


        if self.PageNo == 3:
            self.Data.set("")
            self.PageNo += 1
            self.Text.set(self.Lines[self.PageNo])
            self.Test = Label(self, bg='#FF9933', textvariable=self.Data, font=("", 18, "bold"))
            self.Test.place(relx=.5, rely=.65, anchor="center")
            self.tip.set("Type Your Name and Enter")


        elif self.PageNo == 7:
            self.PageNo += 1
            self.Text.set(self.Lines[self.PageNo])
            self.Test = Label(self, bg='#FF9933', textvariable=self.Data, font=("", 18, "bold"))
            self.Test.place(relx=.5, rely=.65, anchor="center")
            self.Data.set("")
            self.tip.set("Type Your Email and Enter (<name>@<service>.<extn>)")
        
        elif self.PageNo == 10:
            MainUser.save(self.NewUser)
            self.Parent.Switch(StartPage)


    def Input(self, event):
        if event.char == "":
            pass
        
        elif ord(event.char) == 13 and self.PageNo == 4:
            if len(self.Data.get()) > 0:
                self.PageNo += 1
                self.NewUser[0] = self.Data.get().title()
                self.Text.set(self.Lines[self.PageNo].format(self.Data.get()))
                self.Data.set("")
                self.tip.set("Type Your Gender and Enter ('Male' or 'Female')")
            else:
                self.Text.set(self.Lines[self.PageNo].format(self.Data.get()))
        
        elif ord(event.char) == 13 and self.PageNo == 5:
            if len(self.Data.get()) > 0 and self.Data.get().lower() in ("male", "female"):
                self.PageNo += 1
                self.NewUser[2] = self.Data.get().title()
                self.Text.set(self.Lines[self.PageNo].format(self.Data.get()))
                self.Data.set("")
                self.tip.set("Type Your Age and Enter")
            else:
                pass
        
        elif ord(event.char) == 13 and self.PageNo == 6:
            if len(self.Data.get()) > 0 and self.Data.get().isdigit():
                self.PageNo += 1
                self.NewUser[1] = self.Data.get()
                self.Text.set(self.Lines[self.PageNo].format(self.Data.get(), self._AgeRemark(int(self.Data.get()))))
                self.Data.set("")
                self.Test.destroy()
                self.tip.set("Tap Anywhere")
            else:
                pass
        
        elif ord(event.char) == 13 and self.PageNo == 8:
            if len(self.Data.get()) > 0 and match(r'\w+@\w+.\w+', self.Data.get()):
                self.PageNo += 1
                self.NewUser[3] = self.Data.get()
                self.Text.set(self.Lines[self.PageNo])
                self.Data.set("")
                self.tip.set("Type Your Phone No. and Enter (8-digit)")
            else:
                pass

        elif ord(event.char) == 13 and self.PageNo == 9:
            if len(self.Data.get()) == 8 and self.Data.get().isdigit():
                self.PageNo += 1
                self.NewUser[4] = self.Data.get()
                self.Text.set(self.Lines[self.PageNo])
                self.Data.set("")
                self.Test.destroy()
                self.tip.set("Tap Anywhere")
            else:
                pass
        
        elif self.PageNo == 8 and match(r'[\w@.]', event.char):
            self.Data.set(self.Data.get() + event.char)
        elif match(r'[A-Za-z0-9\s]', event.char):
            self.Data.set(self.Data.get() + event.char)
        elif ord(event.char) == 8:
            self.Data.set(self.Data.get()[:-1])
    
    def _AgeRemark(self, age):
        if 0 < age < 10:
            return "Well, Chidren Are Curious Nowadays...\nIndeed They Are"
        if 9 < age < 20:
            return "You Are Still Quite Young"
        if 19 < age < 29:
            return "The Starting Age Of A Responsible Adult"
        if 28 < age < 51:
            return "I'm Curious To Know, How Were Your Prime Dyas"
        if 50 < age < 100:
            return "Its a Surprise To See Elderly People To Use This App"
        else:
            return "If You Don't Want Tell Me, Thats Fine"


class MainActivity(Frame):
    def __init__(self, parent):
        Frame.__init__(self, bg='#DAE8FC', width=500, height=800)
        self.Parent = parent
        self.Message = StringVar()
        self.Chat = StringVar()
        self.AllChat = []
        self.Option = StringVar()
        self.Learn = None
        self.Focus = False
        self.botsingle = PhotoImage(file="images/BotSingleLine.png")
        self.botsingle = self.botsingle.subsample(2,2)
        self.botmultiple = PhotoImage(file="images/BotMultipleLine.png")
        self.botmultiple = self.botmultiple.subsample(2,2)
        self.usersingle = PhotoImage(file="images/UserSingleLine.png")
        self.usersingle = self.usersingle.subsample(2,2)
        self.usermultiple = PhotoImage(file="images/UserMultipleLine.png")
        self.usermultiple = self.usermultiple.subsample(2,2)

        
        Header = Frame(self, bg='#FA6800', width=500, height=60)
        Header.place(x=0, y=0)
        self.logo = PhotoImage(file="images/logo2.png")
        self.logo = self.logo.subsample(10,10)
                
        Logo = Label(Header, bg='#FA6800', image=self.logo)
        Logo.place(x=-5, y=-2)
        
        Name = Label(Header, bg='#FA6800', text=MainUser.getName(), font=("", 12, "bold"))
        Name.place(relx=.5, rely=.5, anchor='center')

        self.news = PhotoImage(file="images/new.png")
        self.news = self.news.subsample(11,11)

        Daily = Label(Header, bg='#FA6800', image=self.news)
        Daily.place(x=440, y=-1)
        Daily.bind("<Button-1>", self.NewUpdate)

        self.Inbox = Label(self, bg='#DAE8FC', width=50, height=34, font=("", 12, "bold"))
        self.Inbox.place(x=0, y=60)
        
        self.textbox = PhotoImage(file="images/text.png")
        self.textbox = self.textbox.subsample(2,2)
        
        Input = Label(self, width=500, height=100, image=self.textbox)
        Input.place(x=0, y=710)

        Hint = Label(self, bg="#DAE8FC", textvariable=self.Option, font=("", 10))
        Hint.place(x=10, y=710)
        Hint.bind("<Key>", self.Input)
        
        Chatbox = Label(self, bg='#FFFFFF', textvariable=self.Message, width=45, height=1, font=("", 12, "bold"))
        Chatbox.place(x=10, y=755)
        Chatbox.focus_set()
        Chatbox.bind("<Key>", self.Input)


    def Input(self, event):
        if event.char == "":
            pass
        
        elif ord(event.char) == 13:
            if len(self.Message.get()) > 0:
                self.AllChat.insert(0, [1, self.Message.get()])
                if len(self.AllChat) > 6:
                    self.AllChat.pop(6)
                #self.Update()
                self.Reply(self.Message.get())
                self.Update()
                self.Message.set("")
                self.Option.set("")
            else:
                pass
        
        elif ord(event.char) == 8:
            if len(self.Message.get()) > 0:
                self.Message.set(self.Message.get()[0:-1])
            self.Option.set(English.Suggestion(self.Message.get()))
        
        elif match(r'.', event.char):
            self.Message.set(self.Message.get() + event.char)
            self.Option.set(English.Suggestion(self.Message.get()))


    def NewUpdate(self, event):
        if self.Focus == False:
            self.Learn = Frame(self, bg='#FFF2CC', width=500)
            self.Learn.place(relx=.5, rely=.5, anchor="center")
            New_Word = (English.NewWord())
            H = Label(self.Learn, bg='#EA6B66', text=New_Word[0].upper(), width=60, font=("", 10, "bold"))
            H.grid(row=0, ipady=5)
            T = Label(self.Learn, bg='#FFF2CC', text=StrToPara(New_Word[1][0], 60), width=60, font=("", 10, "italic"))
            T.grid(row=1, pady=10)
            self.Focus = True
        else:
            self.Learn.destroy()
            self.Update()
            self.Focus = False

    def Update(self):
        self.Inbox.destroy()
        self.Inbox = Label(self, bg='#DAE8FC', width=50, height=34)
        self.Inbox.place(x=0, y=60)
        curMsg =""
        for chat in range(len(self.AllChat)):
            MsgLen = len(self.AllChat[chat][1])
            if self.AllChat[chat][0] == 0:
                if MsgLen < 55:
                    Box = Label(self.Inbox, image=self.botsingle, borderwidth=0)
                    Box.pack(side='bottom', anchor='se')
                    Msg = Label(Box, bg='#FFFFFF', text=self.AllChat[chat][1], font=("", 11, "bold"))
                    Msg.place(relx=.5, rely=.65, anchor="center")
                elif MsgLen < 75:
                    Box = Label(self.Inbox, image=self.botsingle, borderwidth=0)
                    Box.pack(side='bottom', anchor='se')
                    Msg = Label(Box, bg='#FFFFFF', text=self.AllChat[chat][1], font=("", 8, "bold"))
                    Msg.place(relx=.5, rely=.65, anchor="center")
                elif MsgLen < 160:
                    curMsg = self.AllChat[chat][1]
                    Box = Label(self.Inbox, image=self.botmultiple, borderwidth=0)
                    Box.pack(side='bottom', anchor='se')
                    Msg = Label(Box, bg='#FFFFFF', text=StrToPara(self.AllChat[chat][1], 75), font=("", 8, "bold"))
                    Msg.place(relx=.5, rely=.5, anchor="center")
            else:
                if MsgLen < 55:
                    Box = Label(self.Inbox, image=self.usersingle, borderwidth=0)
                    Box.pack(side='bottom', anchor='se')
                    Msg = Label(Box, bg='#FFFFFF', text=self.AllChat[chat][1], font=("", 11, "bold"))
                    Msg.place(relx=.5, rely=.35, anchor="center")
                elif MsgLen < 100:
                    Box = Label(self.Inbox, image=self.usermultiple, borderwidth=0)
                    Box.pack(side='bottom', anchor='se')
                    Msg = Label(Box, bg='#FFFFFF', text=StrToPara(self.AllChat[chat][1], 55))
                    Msg.place(relx=.5, rely=.35, anchor="center")
    
    def Reply(self, chat):
        self.AllChat.insert(0, [0, AppBot.Response(chat)])
        if len(self.AllChat) > 7:
            self.AllChat.pop(7)