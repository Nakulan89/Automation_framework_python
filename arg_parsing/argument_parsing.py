import argparse
import os
import sys

my_parser = argparse.ArgumentParser(description='List the contents of folder', epilog='Enjoy the program ! :)',
                                    prefix_chars='-')

my_parser.add_argument('-path', default='C:\\', required=False, type=str, help='the path to list')

args = my_parser.parse_args()

input_path = args.path

if not os.path.isdir(input_path):
    print("The specified path does not exist")
    sys.exit()

print('\n'.join(os.listdir(input_path)))
