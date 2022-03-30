#!/usr/bin/python3

import time
import sys


def timed_print(string, delay):
	for char in string:
		print(char, end='')
		sys.stdout.flush()
		time.sleep(delay)
	print()
		


def main():
	timed_print("Hello, there :)", 0.08)

if __name__ == '__main__':
	main()
