"""Moduł czyszczący terminal."""
from os import system, name
from time import sleep 

def _clear_terminal(): 
    if name == 'nt': #windows
        _ = system('cls') 
    else: #unix, mac
        _ = system('clear') 


def clear(FreezeTime = 0):
    """Czyści ekran - FreezeTime podany w sekundach."""
    sleep(FreezeTime)
    _clear_terminal()