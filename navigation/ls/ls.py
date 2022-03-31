#!/usr/bin/python3

# Import needed classes 
import time
import sys
import os

# Import utilities from other folder
sys.path.insert(0, os.getcwd() + '/utils')
from utils import timed_print, print_line, ls_python

# Set the pace of the print statements and line nums
time_var = 0.01
line_num = 150

# Print the introduction text
def print_ls(path):

    print_line('#', line_num)
    with open(path) as f:
        lines = f.readlines()
    for line in lines:
        timed_print(line.strip(), time_var)


def get_user_choice():

    # Create set for non-hidden files
    compare_set = set()
    for item in ls_python():
        if(item[0] != '.'):
            compare_set.add(item)

    # Initialize set 
    responses = set()

    while responses != compare_set:

        timed_print('\tENTER A FILE: ', time_var)
        response = input('\t\t')
        if(response not in compare_set):
            timed_print('\tSorry, ' + response + ' is not a file in this directory! Try again ...', time_var)
        else:
            timed_print('\tCorrect! Keep going!', time_var)
            responses.add(response)

    timed_print('Well done, you got them all!', time_var)
    return(True)

def main():

    os.system('clear')
    print_ls('navigation/ls/ls_intro.txt')
    timed_print('Press any key when you\'ve ran the command: ', time_var)
    input()
    print_ls('navigation/ls/ls_quiz.txt')
    choice = get_user_choice()
    print_line('#', line_num)
        
if __name__ == '__main__':
	main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
