import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

from model import Model
from menu import Menu
import clear_terminal

if __name__ == "__main__":
    model = Model()
    clear_terminal.clear()
    while True:
        menu = Menu(model)
        menu.run()
