#!/usr/bin/env python3

import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

player = {"name": "Gary", "remaining_lives": 3}

clear()
