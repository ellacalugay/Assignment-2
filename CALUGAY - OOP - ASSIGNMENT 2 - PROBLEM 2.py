# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #2 | PROBLEM 2 - DECRYPTION

# Import the necessary module from the colorama package, pyfiglet, as well as termcolor and time.
from termcolor import colored
from pyfiglet import Figlet
import time

# ASCII art for the header with ANSI escape codes for color
print("\033[38;5;218m" + """
┼┼┼┼┼┼┼┼┼┼┼┼▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄┼┼┼┼┼┼┼┼┼┼┼  
┼┼┼┼┼┼┼┼┼┼┼┼█▒▒░░░░░░░░░▒▒█┼┼┼┼┼┼┼┼┼┼┼ 
┼┼┼┼┼┼┼┼┼┼┼┼█░░█░░░░░█░░█┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼─▄▄──█░░░▀█▀░░░█──▄▄─┼┼┼┼┼┼┼┼ 
┼┼┼┼┼┼┼┼┼█░░█─▀▄░░░░░░░▄▀─█░░█┼┼┼┼┼┼┼┼ 
┼┼┼┼┼┼██░██░████░██░░░██░░░█████┼┼┼┼┼┼
┼┼┼┼┼┼██▄██░██▄▄░██░░░██░░░██░██┼┼┼┼┼┼
┼┼┼┼┼┼██▀██░██▀▀░██░░░██░░░██░██┼┼┼┼┼┼
┼┼┼┼┼┼██░██░████░████░████░█████┼┼┼┼┼┼                                         
""" + "\033[0m")

# Record the start time.
start_time = time.time()

# Ask the user to provide an encrypted text to be decrypted with some foreground colors and background colors.
user_input_string = input("\033[38;5;139;1m\033[48;5;225mEnter a string to decrypt:\033[0m \033[34m")
output_str = ""

# Go through each character in the string.
for char in range(len(user_input_string)): 
#   If the symbol is asterisk "*", replace it with the character "a"
    if user_input_string[char] == "*":
        output_str += "a" 
#   If the symbol is ampersand "&", replace it with the character "e"
    elif user_input_string[char] == "&":
        output_str += "e"
 #   If the symbol is hash "#", replace it with the character "i"
    elif user_input_string[char] == "#":
        output_str += "i"
#   If the symbol is plus "+", replace it with the character "o"
    elif user_input_string[char] == "+":
        output_str += "o"
#   If the symbol is exclamation point "!", replace it with the character "u"
    elif user_input_string[char] == "!":
        output_str += "u"
    else:
        output_str += user_input_string[char]

# Import the Figlet module to create ASCII art and set the font, justification, and width.
notice = Figlet(font="Roman", justify="center", width=150)
print("\n") # special character that represents a newline  to make it more readable
# Print a horizontal line with flower emoji on each side to visually separate the output.
print("\x1b[95m 🌸" * 50 + "\x1b[0m") 
# Print a message indicating that the decrypted text follows with magenta text on a light background.
print("\033[38;5;139;1m\033[48;5;225m  The Plain Text:  \033[0m")
# Create ASCII art of the decrypted text in yellow text and print it out.
print("\n") # special character that represents a newline  to make it more readable
print(format(colored(notice.renderText(output_str), "yellow"))) # print output with some fg and bg color.
# Print another horizontal line with flower emoji on each side to visually separate the output.
print("\x1b[95m 🌸" * 50 + "\x1b[0m")

# Record the end time.
end_time = time.time()

# Calculate the input time and print it.
print("\n") #special character that represents a newline to separate different parts of the output.
input_time = end_time - start_time
print("{:^30}".format("\x1b[33m🦋 🦋 🦋 🦋 🦋 🦋 🦋 🦋 🦋 🦋 🦋\x1b[0m"))
print("{:^62}".format("\033[38;5;139;1m\033[48;5;225mInput time: {:.2f} seconds\033[0m".format(input_time)))
print("{:^30}".format("\x1b[33m🦋 🦋 🦋 🦋 🦋 🦋 🦋 🦋 🦋 🦋 🦋\x1b[0m"))

# ASCII art for the outer with ANSI escape codes for color
print("\033[38;5;105m" + """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠒⠒⠲⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡤⠶⠲⠦⣄⠀⠀⠀⣀⣀⣀⣀⣤⣤⣼⣃⣀⡴⠋⠛⢦⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⢋⡴⠖⠦⣄⣨⠷⠚⠉⠉⠀⠀⠀⠀⠀⠀⠈⠉⠲⢤⡀⢈⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣏⢸⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣼⠃⠀⠀⠀⠀⠀⠀⠀⢀⣀⡠⠤⠤⠤⠤⠄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢻⡜⢦⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⢀⠴⠋⢡⣦⣤⣀⠀⠀⠀⠀⠀⠀⠉⠑⠲⠤⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢹⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀⠀⠀⠀⢷⠀⠀⠀⣰⠃⠀⠀⣾⣿⠛⠻⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠢⣄⠀⠀⠀⠀
⠀⠀⠀⢸⡇⠀⠀⠀⠀⠐⠶⠆⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⢸⡄⠀⠀⡇⠀⠀⣸⣿⣷⣶⣶⠿⠃⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀
⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⣠⡀⣀⠤⠒⠋⠉⠙⠒⠾⣿⠇⠀⠀⠀⠀⠀⢧⠀⠀⢧⠀⢠⣿⡏⠀⠈⣿⡦⠀⣿⡇⢀⣼⣶⢄⣀⣀⡀⠀⠀⢠⣦⡌⢣⡀
⠀⠀⠀⢸⡇⠀⠀⠀⠀⠈⢿⠟⠁⠀⠰⢿⡿⠂⠀⠀⠈⢣⠀⠀⠀⠀⠀⠸⡇⠀⠈⢦⠘⠻⠿⣶⣾⡿⠃⠀⣿⣥⣾⠟⢡⣾⡟⠛⢿⣧⠀⣼⣿⠃⠀⢳
⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⡞⠀⠀⣄⣠⣼⢿⣦⣴⠆⠀⠈⡆⠀⠀⠀⠀⢠⡇⠀⠀⠀⠳⣄⠀⠀⠀⠀⠀⣠⣿⡿⠃⠀⣾⣿⠛⠻⢿⡿⢰⣿⠏⠀⠀⢸
⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⢷⠀⠀⠈⠉⠷⠴⠟⠀⠀⠀⣰⠃⠀⠀⠀⣠⡞⠀⠀⠀⠀⠀⠈⠑⢦⣀⠀⠼⠿⠋⠀⠀⠀⠈⠻⢷⣶⡆⢠⣬⡉⠀⠀⢀⡾
⠀⠀⠀⠀⠹⣄⠀⠀⠀⠀⠈⠣⣀⠀⠀⠀⠀⠀⠀⢀⡴⠃⠀⣀⡤⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢑⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠁⣀⡤⠞⠀
⠀⠀⠀⠀⠀⠈⠓⢦⣤⣄⣀⣀⣈⣓⣒⣤⣤⣶⡾⠿⢶⣾⣯⣭⣤⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⡴⠋⠀⠀⣄⣠⡴⠞⠒⠢⠤⠀⠐⠒⠚⠋⠉⠀⠀⠀
⠀⠀⠀⠀⣀⣤⠶⠚⠉⠁⣸⠟⠉⠉⠙⢧⣀⠀⠀⠀⡸⢻⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠑⠒⠊⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣸⠋⠉⠉⠁⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠈⠑⠒⠚⠁⢸⡟⠶⢤⣄⡀⠀⠀⢠⣦⣤⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢹⡄⠀⠀⠀⠀⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠈⠙⢳⣄⠈⢻⣿⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠳⣤⣀⣀⣀⣤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⣏⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⠿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⠀⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠉⠻⣦⠀⠀⠀⣀⣤⠞⠛⠲⣤⣀⣤⠶⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠘⣟⠛⢿⡁⠀⠀⠀⠀⠀⠀⠀⠀⢿⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠈⢳⠀⠛⢦⣄⠀⠀⠀⠀⠀⣰⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣄⠀⠀⢀⣤⠀⣠⡾⠀⠀⠀⠙⠷⣄⣀⢀⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""" + "\033[0m")

# End of code.
