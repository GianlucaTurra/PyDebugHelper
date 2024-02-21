"""
Applicazione di supporto per il debug

Author: Gianluca Turra
Version: 0.241202
"""

from app.application import App
from app.notebook.app_notebook import AppNoteBook


def main():
    app = App(AppNoteBook)
    app.run()


if __name__ == '__main__':
    main()
