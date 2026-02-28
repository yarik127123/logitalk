from customtkinter import*



Class MainWindow(CTk):
    def __init__(self):
        super().__init--()
        self.geometry("700x500")
        self.title("logtalk")



        self.menu_btn = CTkButton(self,width=200,text="menu",corner_radius=0)
        self.menu_btn.place(x=0,y=0)

        self.menu_frame = CTkframe(self,width=200,height=500,corner_radius=0)
        self.menu_frame.place(x=0, y=0)

        self.chat_frame = CTkScrollableFrame(self)
        self.chat_frame.place(x=0. y=9)

        self.send_frame = CTkFrame(Self)
        self.senf_frame.place(x=0,y=0)

        self.pin_btn = CTkButton(self,self.send_frame,text="pin")
        self.pin_btn = C


        self.adaptive_ui()

    def adaptive_ui(self):
        self.menu_frame.place(x = 0, y = self.menu_btn.winfo_height())
        self.after(50,self.adaptive_ui)



main = MainWindow()
main.mainloop()
