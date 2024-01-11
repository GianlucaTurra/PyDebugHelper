from GUI.main_application import MainApplication
from GUI.insert_ds import InsertDs

import tkinter as tk


def main():
    root = tk.Tk()
    app = MainApplication(parent=root, frame=InsertDs)
    app.mainloop()


if __name__ == '__main__':
    main()
