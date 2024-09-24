#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

WellWise

Entry point for the WellWise Program

Copyright 2024 Jenna Everard

"""

from GraphWell.graph_well import graphwell

def print_opening_image():
    v = r"""⠀⠀⠀

                   v  ~.      v                                    v  ~.      v
          v           /|                                  v           /|
                     / |          v                                  / |          v
              v     /__|__                                    v     /__|__
                  \--------/                                      \--------/
~~~~~~~~~~~~~~~~~~~`~~~~~~'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`~~~~~~'~~~~~~~~~~~~~~~~~~~~~~
"""
    print(v)
  
def print_program_name():
    v = r"""
.--.      .--.     .-''-.     .---.        .---.      .--.      .--. .-./`)     .-'''-.      .-''-.   
|  |_     |  |   .'_ _   \    | ,_|        | ,_|      |  |_     |  | \ .-.')   / _     \   .'_ _   \  
| _( )_   |  |  / ( ` )   ' ,-./  )      ,-./  )      | _( )_   |  | / `-' \  (`' )/`--'  / ( ` )   ' 
|(_ o _)  |  | . (_ o _)  | \  '_ '`)    \  '_ '`)    |(_ o _)  |  |  `-'`"` (_ o _).    . (_ o _)  | 
| (_,_) \ |  | |  (_,_)___|  > (_)  )     > (_)  )    | (_,_) \ |  |  .---.   (_,_). '.  |  (_,_)___| 
|  |/    \|  | '  \   .---. (  .  .-'    (  .  .-'    |  |/    \|  |  |   |  .---.  \  : '  \   .---. 
|  '  /\  `  |  \  `-'    /  `-'`-'|___   `-'`-'|___  |  '  /\  `  |  |   |  \    `-'  |  \  `-'    / 
|    /  \    |   \       /    |        \   |        \ |    /  \    |  |   |   \       /    \       /  
`---'    `---`    `'-..-'     `--------`   `--------` `---'    `---`  '---'    `-...-'      `'-..-'   
                                                                                                      
"""
    print(v)
    print("\nA program for integrating well logging and machine learning\n")
    print("Copyright 2024 Jenna Everard\n")
    print("Version 1.0.1\n\n")

def print_closing_image():
    v = r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡤⡀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡹⡟⢧⡌⢄⠀⣀⠀⣠⡪⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡴⠋⠀⡈⢯⡥⣧⣠⠎⠁⣠⡞⠑⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⠀⠀⠈⢦⠚⠟⢷⣄⡝⠋⢱⡤⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢩⡇⠀⠀⡤⣱⣤⣤⢿⣿⣄⠞⣠⣴⡋⠙⣆⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢾⣶⠢⠇⠀⠙⡇⠉⢹⣿⣿⠉⠀⣹⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠈⣆⠀⠈⢿⣷⡞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⠤⠷⢤⣀⠀⠀⠈⢧⢀⠞⠉⠛⠲⣄⠀⠀⢀⠞⠉⠳⣄⠀
⠤⣀⣀⠴⠋⠀⠀⠀⠀⠀⠈⠉⠓⠚⠁⠀⠀⠀⠀⠀⠙⠒⠃⠀⠀⠀⠀⠉
"""
    print(v)

if __name__ == "__main__":
    
    print_opening_image()
    print_program_name()
    
    print("---Welcome!---\n\n")
    
    print("\nWhich program would you like to run?\n\t1. GraphWell\n\t2. LithoLogic\n\t3. VeloSight\n\t4. DensiSense")
    response = input("Enter an option (1-4): ")
    
    valid_data_type = False
    while not valid_data_type:
        try:
            response = int(response)
            if response == 1:
                graphwell()
                valid_data_type = True
            elif response == 2:
                valid_data_type = True
                print("\nComing Soon :)\n")
            elif response == 3:
                valid_data_type = True
                print("\nComing Soon :)\n")
            elif response == 4:
                valid_data_type = True
                print("Coming Soon :)")
            else:
                response = input("Please enter either 1, 2, or 3: ")
        except ValueError:
            response = input("Please enter a number: ")
    
    print_closing_image()
    print("--TERMINATION--")