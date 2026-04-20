from classes.main_window import *


def main():
    window = MainWindow()
    window.create_gui()
    window.root.mainloop()

if __name__ == "__main__":
    main()