import customtkinter as ctk

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.inputs = ""
        self.geometry("315x470")
        self.title("CALCULATOR")
        self.configure(fg_color= "lightblue")

        label = ctk.CTkLabel(self, text="CALCULATOR", fg_color="transparent", text_color="#3B8ED0", font=("Bahnschrift", 24), pady=15)
        label.grid(row=0, column=0, sticky="nsew")

        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=2, column=0, padx=10, pady=0)

        for i in range(10):
            button = ctk.CTkButton(button_frame, height=50, width=85, text=i, font=("Bahnschrift", 18),
                                    command=lambda v=i: self.num_button_click(v))
            col = 0
            if i%3 == 1:
                col = 1
            elif i%3 == 2:
                col = 2
            button.grid(row=(i//3)+1, column=col, padx=6, pady=10)

        edit_buttons = {"Enter":(5, 2), "+":(5, 1), "-":(5, 0), "*":(4, 1), "/":(4, 2)} # dict key = name value = (r, c)

        for button_name in edit_buttons.keys():
            button = ctk.CTkButton(button_frame, height=50, width=85, text=button_name, text_color="#DBDBDB", font=("Bahnschrift", 18), 
                                   command=lambda v=button_name: self.edit_button_click(v))
            button.grid(row=edit_buttons[button_name][0], column=edit_buttons[button_name][1], padx=6, pady=10)

        self.textbox = ctk.CTkTextbox(self, width=100, height=70, fg_color="#DBDBDB", text_color="#3B8ED0", font=("Bahnschrift", 18), border_color="#3B8ED0", border_width=2)
        self.textbox.grid(row=1, column=0, padx=10, pady=0, sticky="nsew")

        clear = ctk.CTkButton(self, width=20, corner_radius=0, text="CLR", font=("Bahnschrift", 20),  fg_color="#DBDBDB", text_color="#7A7A7A", command=lambda: self.clear())
        clear.grid(row=1, column=0, sticky="se", padx=20, pady=5)


    def num_button_click(self, num):
        self.inputs += str(num)
        self.textbox.insert("end", str(num))

    def edit_button_click(self, value):
        if value == "Enter":
            try:
                result = eval(self.inputs)
                self.textbox.delete("1.0", "end")
                self.textbox.insert("end", str(result))
                self.inputs = str(result)
            except (ZeroDivisionError, SyntaxError) as e:
                self.textbox.delete("1.0", "end")
                self.textbox.insert("end", "ERROR")
                self.inputs = ""
            
        else:
            self.inputs += value          
            self.textbox.insert("end", str(value))
    
    def clear(self):
        self.textbox.delete("1.0", "end")
        self.inputs = ""

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()