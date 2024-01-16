from GUI.main_application import MainApplication
from GUI.insert_ds import InsertDs

import tkinter as tk


def main():
    root = tk.Tk()
    frames = {'Controllo DS': InsertDs}
    app = MainApplication(parent=root, frames=frames)
    app.grid()
    app.mainloop()


if __name__ == '__main__':
    main()
