#/usr/bin/python3

# Import needed classes 
import time
import sys
import os

# Import utilities from other folder
sys.path.insert(0, os.getcwd() + '/utils')
from utils import timed_print, print_line, cd_python, pwd_python

# Set the pace of the print statements and line nums
time_var = 0.01
line_num = 150

# Print the introduction text
def print_cd(path):

    print_line('#', line_num)
    with open(path) as f:
        lines = f.readlines()
    for line in lines:
        timed_print(line.strip(), time_var)

def cd_test(subfolder):

    # Get the absolute path 
    cd_python(subfolder)
    compare = pwd_python()
    cd_python('..')

    while True:

        timed_print('\tCURRENT LOCATION: ', time_var)
        response = input('\t\t')

        if(compare == response):
            timed_print('Awesome job!', time_var)
            break
        else:
            timed_print('Whoops, try again ...', time_var)

def main():

    os.system('clear')
    print_cd('navigation/cd/cd_intro.txt')
    timed_print('Press any key when you\'ve ran the command: ', time_var)
    input()
    cd_test('introduction')
    print_line('#', line_num)
        
if __name__ == '__main__':
	main()