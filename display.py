from tkinter import HORIZONTAL, Frame, Label, CENTER, Button, Scale, Entry
import tkinter as tk
from settings import *


class Screen(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('Belief Revision Agent')
        self.master.bind("<Key>", self.key_down)

        self.init_grid()


    def init_grid(self):
        """
        Description:
            Initialize the grid corresponding to the display of the game. Here all the buttoms, frames,
            labels, etc. are defined and initialize.
        """
        window = Frame(self, bg=COLOR_PALETTE['background'])
        window.grid()

        displayCell = Frame(window, bg=COLOR_PALETTE['window'])
        displayCell.rowconfigure(0, minsize=300, weight=1)
        displayCell.columnconfigure(0, minsize=300, weight=1)
        displayCell.grid(row=0, column=0, padx=20, pady=20, sticky='ew')
        display = Label(displayCell, bg=COLOR_PALETTE['window'], text='BELIEF SYSTEM', font=SUB_FONT)
        display.grid(sticky='nw')

        # Input cell for proposition and (commands)?
        #entryFrame = Frame(window, bg=COLOR_PALETTE['window'])
        #entryFrame.grid(row=2, column=0, padx=20, sticky='ew')
        entryCell = Entry(window, bg=COLOR_PALETTE['window'], font=SUB_FONT, width=80)
        entryCell.grid(row=2, column=0, padx=20, sticky='w')

        # Possible logic operators
        operatorFrame = Frame(window, bg=COLOR_PALETTE['background'])
        operators = ['NEG', 'OR', 'AND', '->', '<->']
        operators_commands = [self.insertNEG, self.insertOR, self.insertAND,
                              self.insertIMPLICATION, self.insertBIMPLICATION]
        for i, operator in enumerate(operators):
            button = Button(operatorFrame, bg=COLOR_PALETTE['buttoms'],
                            text=operator, command=operators_commands[i],
                            font=SUB_FONT_BOLD, relief=tk.RAISED)
            button.grid(row=0, column=i, padx=5, pady=5, sticky='ew')
        operatorFrame.grid(row=3, column=0, padx=20, pady=20)

        # Complex fucntions buttons
        #### Implement on the right side of the window screen


    def run(self):
        self.update_idletasks()
        self.mainloop()
     

    def key_down(self, event):
        key = event.keysym
        print(event)
        if key == KEY_QUIT: exit()

    def insertNEG(self):
        pass
    
    def insertOR(self):
        pass
    
    def insertAND(self):
        pass

    def insertIMPLICATION(self):
        pass
    
    def insertBIMPLICATION(self):
        pass
        


if __name__ == '__main__':
    whole_display = Screen()
    whole_display.run()


