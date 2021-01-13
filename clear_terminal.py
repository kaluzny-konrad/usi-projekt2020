"""Moduł czyszczący terminal."""
from os import system, name, environ
from time import sleep 

def _clear_terminal():
    """Czyści terminal na Windows lub Unix/Mac."""
    if name == 'nt': #windows
        _ = system('cls') 
    else: #unix, mac
        _ = system('clear') 


def clear(FreezeTime = 0):
    """Czyści ekran - FreezeTime podany w sekundach."""
    sleep(FreezeTime)
    _clear_terminal()
