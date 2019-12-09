from tkinter import Tk, Frame, Label, Entry, Text, Button, StringVar, Canvas
from tkinter.ttk import Combobox


class ManageView:
    """ This class is responsible for:
        - create the main window
        - set the window
        - create methods for widgets that will be used in the apps """

    def __init__(self):
        self.root = None

    def create_root(self):
        """ This method creates the main window"""
        self.root = Tk()

    def parameter_root(self):
        """ this method is responsible for defining the characteristics
                of my main window with:
                - title
                # icon
                - size and location
                - minimum size"""
        self.root.title("Application Pur Beurre")
        self.root.geometry("450x620-20+20")
        self.root.minsize(450, 600)
        self.root['bg'] = 'white'

    @staticmethod
    def create_frame(master, bg='white', row=0, col=0, sticky='nesw',
                     padx=20, pady=20):
        """ This method creates a tkinter frame widgets.
            :param master: Tk (the parent window)
            :param bg: String (background color)
            :param row: Integer (line number where the frame will be placed)
            :param col: Integer (column number where the frame will be placed)
            :param sticky : String (placement in the cell)
            :param padx : Integer (horizontal outer margin)
            :param pady : Integer (vertical outer margin) """
        frame = Frame(master, bg=bg)
        frame.grid(row=row, column=col, sticky=sticky, padx=padx, pady=pady)
        return frame

    @staticmethod
    def create_label(master, text="text", font=("Arial", 8), bg="white",
                     fg='black', row=0, col=0, sticky='w', padx=0, pady=0):
        """ This method creates a tkinter label widget
            :param master: Tk (the parent window)
            :param text: String (text displayed inside the label)
            :param font: tuple (font: String, size_font: Integer)
            :param bg: String (background color)
            :param fg: String (font color)
            :param row: Int (line number where the frame will be placed)
            :param col: Int (column number where the label will be placed)
            :param sticky: String (placement in the cell)
            :param padx: Int (horizontal outer margin)
            :param pady: Int (vertical outer margin)
            :return: tkinter.label
                    """
        label = Label(master, text=text, font=font, bg=bg, fg=fg)
        label.grid(row=row, column=col, sticky=sticky, padx=padx, pady=pady)
        return label

    @staticmethod
    def create_entry(master, font=("Arial", 15), bg="#E5E3E3", fg='black',
                     row=0, col=0, sticky='e', padx=2, pady=5):
        """ This method creates a tkinter entry widget
            :param master: Tk (the parent window)
            :param font: tuple (font: String, size_font: Integer)
            :param bg: String (background color)
            :param fg: String (font color)
            :param row: Int (line number where the frame will be placed)
            :param col: Int (column number where the label will be placed)
            :param sticky: String (placement in the cell)
            :param padx: Int (horizontal outer margin)
            :param pady: Int (vertical outer margin)
            :return: tkinter.label
                    """
        entry = Entry(master, font=font, bg=bg, fg=fg)
        entry.grid(row=row, column=col, sticky=sticky, padx=padx, pady=pady)
        return entry

    @staticmethod
    def create_text(master, bg='white', font=("Arial", 8), fg='black',
                    height=2, width=65, wrap='word', padx=5, pady=5,
                    row=0, col=0, sticky='w'):
        """ This method creates a tkinter text widget
            :param master: Tk (the parent window)
            :param bg: String (background color)
            :param font: tuple (font: String, size_font: Integer)
            :param fg: String (font color)
            :param height: Integer (height in number of lines)
            :param width: Integer (width in number of characters)
            :param wrap: String (option of line jumps)
            :param padx: Integer (horizontal inside margin)
            :param pady: Integer (vertical inside margin)
            :param row: Integer (line number where the text will be placed)
            :param col: Integer (column number where the label will be placed)
            :param sticky: String (placement in the cell)
        :return: tkinter.text
        """
        text = Text(master, bg=bg, font=font, fg=fg, height=height,
                    width=width, wrap=wrap, padx=padx, pady=pady)
        text.grid(row=row, column=col, sticky=sticky)
        return text

    @staticmethod
    def create_button(master, text, command, font=("Arial", 20), bg='#ADD0EC',
                      fg='white', row=0, col=0, sticky='ns', padx=5, pady=5):
        """ This method creates a tkinter text widget
            :param master: Tk (the parent window)
            :param text: String (text displayed inside the label)
            :param command : func (method to call when you click the button)
            :param font: tuple (font: String, size_font: Integer)
            :param bg: String (background color)
            :param fg: String (font color)
            :param row: Integer (line number where the text will be placed)
            :param col: Integer (column number where the label will be placed)
            :param sticky: String (placement in the cell)
            :param padx: Int (horizontal outer margin)
            :param pady: Int (vertical outer margin)
            """
        button = Button(master, text=text, font=font, bg=bg, fg=fg,
                        command=command)
        button.grid(row=row, column=col, sticky=sticky, padx=padx, pady=pady)
        return button

    @staticmethod
    def create_combobox(master, values_list, command, row=0, col=0,
                        sticky='ns', padx=5, pady=5):
        """ This method creates a tkinter combobox widget
            :param master: Tk (the parent window)
            :param values_list: list (value list displayed inside the combobox)
            :param command : func (method to call when you click the button)
            :param row: Integer (line number where the text will be placed)
            :param col: Integer (column number where the label will be placed)
            :param sticky: String (placement in the cell)
            :param padx: Int (horizontal outer margin)
            :param pady: Int (vertical outer margin)
                    """
        control_variable = StringVar()
        combo = Combobox(master, height=40,
                         textvariable=control_variable, width=40)
        combo.grid(row=row, column=col, sticky=sticky, padx=padx, pady=pady)
        combo['values'] = values_list  # Values list
        combo.current(0)  # Choosing the current value
        # Action triggered by a selection in the list
        combo.bind('<<ComboboxSelected>>', command)
        return combo

    @staticmethod
    def create_line(master, row):
        """ This method creates a tkinter combobox widget
            :param master: Tk (the parent window)
            :param row: Integer (line number where the text will be placed)"""
        line = Canvas(master, bd=0, highlightthickness=0, bg="white",
                      height=20)
        line.create_line((10, 10), (400, 10), fill="#ADD0EC", width=2)
        line.grid(row=row, sticky='w')

    @staticmethod
    def create_canvas(master, bg="white", width=100, height=100,
                      row=0, col=0, sticky='ns', padx=0, pady=0):
        """ This method creates a tkinter canvas widget
            :param master: Tk (the parent window)
            :param bg: String (background color)
            :param width: Integer (width in number of characters)
            :param height: Integer (height in number of lines)
            :param row: Integer (line number where the text will be placed)
            :param col: Integer (column number where the label will be placed)
            :param sticky: String (placement in the cell)
            :param padx: Int (horizontal outer margin)
            :param pady: Int (vertical outer margin)"""
        canvas = Canvas(master, bg=bg, width=width, height=height)
        canvas.grid(row=row, column=col, sticky=sticky, padx=padx, pady=pady)
        return canvas