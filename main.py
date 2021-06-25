from createtab import *
from dropmenu import *
import tkinter.font as tkfont
import math

NUM_TAB = "Numbers"
TEXT_TAB = "Text"

FIND_PI_DIGIT = "Find PI to Nth digit"
FIND_E_DIGIT = "Find E to the Nth digit"
CALCULATOR = "Calculator"

REVERSE_STRING = "Reverse String"
PALINDROME = "Check Palindrome"


# Drop menu options for Number tab
def set_number_menu(command=None):
    number_menu = tk.OptionMenu(root.num_tab, tk_var,
                                CALCULATOR,
                                FIND_PI_DIGIT,
                                FIND_E_DIGIT,
                                command=command)
    number_menu.pack()


# Drop menu options for Text tab
def set_text_menu(command=None):
    text_menu = tk.OptionMenu(root.text_tab, tk_var,
                              REVERSE_STRING,
                              PALINDROME,
                              command=command)
    text_menu.pack()


# Change tabs
def on_tab_selected(e):
    selected_tab = e.widget.select()
    tab_text = e.widget.tab(selected_tab, "text")

    # ----------------------------------------------------------------------------------------
    if tab_text == NUM_TAB:
        # Destroy all widgets when tab switching
        for widget in root.num_tab.winfo_children():
            widget.destroy()
        root.create_menu(root.num_tab)

        # Number tab
        def number_command(x):
            # Destroy all widgets and replace with widgets needed for new menu
            for widget in root.num_tab.winfo_children():
                widget.destroy()
            root.create_menu(root.num_tab)
            set_number_menu(number_command)

            # calculate numbers
            # -------------------------------------------------------------------------------------------------
            if x == CALCULATOR:
                tk_var.set(CALCULATOR)  # Keep memory of choice
                label_text = tk.StringVar()
                tk.Label(menu.mainframe, text="Enter Num 1:", font=fontStyle).grid(row=0, pady=5)
                tk.Label(menu.mainframe, text="Enter Num 2:", font=fontStyle).grid(row=1, pady=5)
                tk.Label(menu.mainframe, text="Result of Calculation:", font=fontStyle).grid(row=3, pady=5)
                tk.Label(menu.mainframe, text="", textvariable=label_text, font=fontStyle).grid(row=3, column=1)
                num1 = tk.Entry(menu.mainframe)
                num2 = tk.Entry(menu.mainframe)
                num1.grid(row=0, column=1, ipadx=5, ipady=5, pady=5)
                num2.grid(row=1, column=1, ipadx=5, ipady=5, pady=5)

                def add_nums():
                    res = int(num1.get()) + int(num2.get())
                    label_text.set(res)

                def sub_nums():
                    res = int(num1.get()) - int(num2.get())
                    label_text.set(res)

                def multiply_nums():
                    res = int(num1.get()) * int(num2.get())
                    label_text.set(res)

                def divide_nums():
                    res = int(num1.get()) / int(num2.get())
                    label_text.set(res)

                def pow_nums():
                    res = pow(int(num1.get()), int(num2.get()))
                    label_text.set(res)

                add = tk.Button(menu.mainframe, text="Add", command=add_nums)
                add.grid(row=4, column=1, padx=5, pady=5)

                subtract = tk.Button(menu.mainframe, text="Subtract", command=sub_nums)
                subtract.grid(row=5, column=1, padx=5, pady=5)

                multiply = tk.Button(menu.mainframe, text="Multiply", command=multiply_nums)
                multiply.grid(row=6, column=1, padx=5, pady=5)

                divide = tk.Button(menu.mainframe, text="Divide", command=divide_nums)
                divide.grid(row=7, column=1, padx=5, pady=5)

                exp = tk.Button(menu.mainframe, text="Power", command=pow_nums)
                exp.grid(row=8, column=1, padx=5, pady=5)
            # -------------------------------------------------------------------------------------------------

            # Find Pi to Nth Digit
            elif x == FIND_PI_DIGIT:
                tk_var.set(FIND_PI_DIGIT)  # Keep memory of choice
                label_text = tk.StringVar()
                tk.Label(menu.mainframe, text="How many digits of PI \n\n do you want to see", font=fontStyle).grid(
                    row=0,
                    column=1,
                    pady=5)
                tk.Label(menu.mainframe, text="PI:", font=fontStyle).grid(row=2, column=0, pady=5)
                tk.Label(menu.mainframe, text="", textvariable=label_text, font=fontStyle).grid(row=2, column=1,
                                                                                                pady=5)

                nth_digit = tk.Entry(menu.mainframe)
                nth_digit.grid(row=1, column=1, ipadx=5, ipady=5, pady=5)

                # Find PI Nth digit using math.pi, goes up to 50
                def find_nth_digit_pi(n):
                    label_text.set(format(math.pi, ".{}g".format(n)))

                find_pi_button = tk.Button(menu.mainframe, text=FIND_PI_DIGIT,
                                           command=lambda: find_nth_digit_pi(nth_digit.get()))
                find_pi_button.grid(row=1, column=2, columnspan=2, rowspan=1, padx=5, pady=5)
            # -------------------------------------------------------------------------------------------------

            # Find Pi to Nth Digit
            elif x == FIND_E_DIGIT:
                tk_var.set(FIND_E_DIGIT)  # Keep memory of choice
                label_text = tk.StringVar()
                tk.Label(menu.mainframe, text="How many digits of e \n\n do you want to see", font=fontStyle).grid(
                    row=0,
                    column=1,
                    pady=5)
                tk.Label(menu.mainframe, text="e:", font=fontStyle).grid(row=2, column=0, pady=5)
                tk.Label(menu.mainframe, text="", textvariable=label_text, font=fontStyle).grid(row=2, column=1,
                                                                                                pady=5)

                nth_digit = tk.Entry(menu.mainframe)
                nth_digit.grid(row=1, column=1, ipadx=5, ipady=5, pady=5)

                # Find e Nth digit using math.e, goes up to 50
                def find_nth_digit_e(n):
                    label_text.set(format(math.e, ".{}g".format(n)))

                find_pi_button = tk.Button(menu.mainframe, text=FIND_E_DIGIT,
                                           command=lambda: find_nth_digit_e(nth_digit.get()))
                find_pi_button.grid(row=1, column=2, columnspan=2, rowspan=1, padx=5, pady=5)

        set_number_menu(number_command)
    # -------------------------------------------------------------------------------------------------------------

    if tab_text == TEXT_TAB:
        # Text Tab
        # Destroy widgets when switching to tab
        for widget in root.text_tab.winfo_children():
            widget.destroy()
        root.create_menu(root.text_tab)

        # Destroy all widgets and replace with widgets needed for new menu
        def text_command(x):
            for widget in root.text_tab.winfo_children():
                widget.destroy()
            root.create_menu(root.text_tab)
            set_text_menu(text_command)

            # -------------------------------------------------------------------------------------------------
            if x == REVERSE_STRING:
                tk_var.set(REVERSE_STRING)  # Keep memory of choice
                label_text = tk.StringVar()
                tk.Label(menu.mainframe, text="Enter String to reverse:", font=fontStyle).grid(row=0, pady=5)
                tk.Label(menu.mainframe, text="Reversed String:", font=fontStyle).grid(row=2, pady=5)
                tk.Label(menu.mainframe, text="", textvariable=label_text, font=fontStyle).grid(row=2, column=1)
                text = tk.Entry(menu.mainframe)
                text.grid(row=0, column=1, ipadx=5, ipady=5, pady=5)

                # Reverse the string
                def reverse_string(string):
                    string = [char for char in string]
                    string.reverse()
                    reversed_str = ""
                    for char in string:
                        reversed_str += char
                    label_text.set(reversed_str)

                reverse_button = tk.Button(menu.mainframe, text=REVERSE_STRING,
                                           command=lambda: reverse_string(text.get()))
                reverse_button.grid(row=0, column=2, padx=5, pady=5)

            # --------------------------------------------------------------------------------------------------------------
            elif x == PALINDROME:
                tk_var.set(PALINDROME)  # Keep memory of choice
                label_text = tk.StringVar()
                tk.Label(menu.mainframe, text="Enter String to Check if palindrome:", font=fontStyle).grid(row=0,
                                                                                                           pady=5)
                tk.Label(menu.mainframe, text="Is palindrome?:", font=fontStyle).grid(row=2, pady=5)
                tk.Label(menu.mainframe, text="", textvariable=label_text, font=fontStyle).grid(row=2, column=1)
                text = tk.Entry(menu.mainframe)
                text.grid(row=0, column=1, ipadx=5, ipady=5, pady=5)

                # Check if string is a palindrome
                def is_palindrome(string):
                    old_string = string.casefold()
                    string = string.casefold()
                    string = [char for char in string]
                    string.reverse()
                    palindrome_string = ""
                    for char in string:
                        palindrome_string += char

                    if palindrome_string == old_string:
                        label_text.set(palindrome_string + " is a palindrome")
                    else:
                        label_text.set(old_string + " is not a palindrome")
                palindrome_button = tk.Button(menu.mainframe, text=PALINDROME,
                                              command=lambda: is_palindrome(text.get()))
                palindrome_button.grid(row=0, column=2, padx=5, pady=5)

        set_text_menu(text_command)
        # -------------------------------------------------------------------------------------------------
    tk_var.set('Function')  # set the default option


# on change dropdown value
def change_dropdown(*args):
    print(tk_var.get())


class MainApplication(tk.Tk):
    def __init__(self):
        # tk.Frame.__init__(self, parent, *args, **kwargs)
        tk.Tk.__init__(self)
        self.title("Project Showcase")
        self.geometry("700x600")

        # Tabs
        global ct
        ct = CreateTabs(self)
        self.num_tab = ct.create_tab()
        self.text_tab = ct.create_tab()
        ct.bind("<<NotebookTabChanged>>", on_tab_selected)
        ct.add(self.num_tab, text=NUM_TAB)
        ct.add(self.text_tab, text=TEXT_TAB)
        ct.pack(expand=True, fill="both")
        self.create_menu(self.num_tab)

    # Dropdown menu
    def create_menu(self, tab):
        global menu, tk_var, popup_menu
        menu = CreateMenu(tab)
        tk_var = tk.StringVar(self)


if __name__ == "__main__":
    root = MainApplication()
    fontStyle = tkfont.Font(family="Lucida Grande", size=14)
    tk_var.trace('w', change_dropdown)
    root.mainloop()
