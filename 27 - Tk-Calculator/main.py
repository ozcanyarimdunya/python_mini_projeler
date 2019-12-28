try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


class Calculator:
    def __init__(self):
        self._stack = []
        self._valid = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/'
        ]

    def add(self, text):
        if text not in self._valid:
            return ''
        self._stack.append(text)
        return text

    def get(self):
        return ''.join(self._stack)

    def evaluate(self):
        try:
            result = eval(self.get())
        except Exception as ex:
            result = ex

        return str(result)

    def reset(self):
        self._stack = []


class Window(tk.Tk):
    is_reset = True

    def __init__(self):
        super().__init__()

        self.calculator = Calculator()

        self.geometry(self.get_geometry())
        self.resizable(False, False)
        self.title("Tk-Calculator")

        self.result = tk.StringVar()
        self.ent_result = tk.Entry(self, textvariable=self.result)
        self.ent_result.place(relx=0.031, rely=0.031, relheight=0.266, relwidth=0.953)
        self.ent_result.configure(background="white", font="TkFixedFont", justify='right')

        self.btn_7 = tk.Button(self)
        self.btn_7.place(relx=0.031, rely=0.344, height=41, width=61)
        self.btn_7.configure(text='7')

        self.btn_8 = tk.Button(self)
        self.btn_8.place(relx=0.281, rely=0.344, height=41, width=61)
        self.btn_8.configure(text='8')

        self.btn_9 = tk.Button(self)
        self.btn_9.place(relx=0.531, rely=0.344, height=41, width=61)
        self.btn_9.configure(text='9')

        self.btn_add = tk.Button(self)
        self.btn_add.place(relx=0.781, rely=0.344, height=41, width=61)
        self.btn_add.configure(text='+')

        self.btn_4 = tk.Button(self)
        self.btn_4.place(relx=0.031, rely=0.5, height=41, width=61)
        self.btn_4.configure(text='4')

        self.btn_5 = tk.Button(self)
        self.btn_5.place(relx=0.281, rely=0.5, height=41, width=61)
        self.btn_5.configure(text='5')

        self.btn_6 = tk.Button(self)
        self.btn_6.place(relx=0.531, rely=0.5, height=41, width=61)
        self.btn_6.configure(text='6')

        self.btn_sub = tk.Button(self)
        self.btn_sub.place(relx=0.781, rely=0.5, height=41, width=61)
        self.btn_sub.configure(text='-')

        self.btn_2 = tk.Button(self)
        self.btn_2.place(relx=0.281, rely=0.656, height=41, width=61)
        self.btn_2.configure(text='2')

        self.btn_1 = tk.Button(self)
        self.btn_1.place(relx=0.031, rely=0.656, height=41, width=61)
        self.btn_1.configure(text='1')

        self.btn_3 = tk.Button(self)
        self.btn_3.place(relx=0.531, rely=0.656, height=41, width=61)
        self.btn_3.configure(text='3')

        self.btn_mul = tk.Button(self)
        self.btn_mul.place(relx=0.781, rely=0.656, height=41, width=61)
        self.btn_mul.configure(text='x')

        self.btn_c = tk.Button(self)
        self.btn_c.place(relx=0.031, rely=0.813, height=41, width=61)
        self.btn_c.configure(text='C', activebackground='#FFF')

        self.btn_0 = tk.Button(self)
        self.btn_0.place(relx=0.281, rely=0.813, height=41, width=61)
        self.btn_0.configure(text='0')

        self.btn_eq = tk.Button(self)
        self.btn_eq.place(relx=0.531, rely=0.813, height=41, width=61)
        self.btn_eq.configure(text='=', activebackground='#456')

        self.btn_div = tk.Button(self)
        self.btn_div.place(relx=0.781, rely=0.813, height=41, width=61)
        self.btn_div.configure(text='/')

        self.init_events()

    def init_events(self):
        # button events
        self.btn_0.bind('<Button-1>', func=lambda event: self.key_clicked('0'))
        self.btn_1.bind('<Button-1>', func=lambda event: self.key_clicked('1'))
        self.btn_2.bind('<Button-1>', func=lambda event: self.key_clicked('2'))
        self.btn_3.bind('<Button-1>', func=lambda event: self.key_clicked('3'))
        self.btn_4.bind('<Button-1>', func=lambda event: self.key_clicked('4'))
        self.btn_5.bind('<Button-1>', func=lambda event: self.key_clicked('5'))
        self.btn_6.bind('<Button-1>', func=lambda event: self.key_clicked('6'))
        self.btn_7.bind('<Button-1>', func=lambda event: self.key_clicked('7'))
        self.btn_8.bind('<Button-1>', func=lambda event: self.key_clicked('8'))
        self.btn_9.bind('<Button-1>', func=lambda event: self.key_clicked('9'))

        # operation events
        self.btn_add.bind('<Button-1>', func=lambda event: self.key_clicked('+'))
        self.btn_sub.bind('<Button-1>', func=lambda event: self.key_clicked('-'))
        self.btn_mul.bind('<Button-1>', func=lambda event: self.key_clicked('*'))
        self.btn_div.bind('<Button-1>', func=lambda event: self.key_clicked('/'))
        self.btn_c.bind('<Button-1>', func=lambda event: self.clear_clicked())
        self.btn_eq.bind('<Button-1>', func=lambda event: self.enter_clicked())

        # global events
        self.bind('<Return>', func=lambda event: self.enter_clicked())
        self.bind('<Key>', func=lambda event: self.key_clicked(event.char))

    def key_clicked(self, key):
        if self.is_reset:
            self.result.set('')
            self.is_reset = False

        self.result.set(self.result.get() + self.calculator.add(key))

    def enter_clicked(self):
        self.result.set(self.result.get() + '=' + self.calculator.evaluate())
        self.calculator.reset()
        self.is_reset = True

    def clear_clicked(self):
        self.result.set('')
        self.calculator.reset()

    def get_geometry(self):
        width = height = 320
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        geometry = '{}x{}+{}+{}'.format(width, height, x, y)
        return geometry


if __name__ == '__main__':
    window = Window()
    window.mainloop()
