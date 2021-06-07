import argparse

my_parser = argparse.ArgumentParser(description='Reading the argument from txt file', fromfile_prefix_chars='@')

my_parser.add_argument('a', help='a first argument')
my_parser.add_argument('b', help='a second argument')
my_parser.add_argument('c', help='a third argument')
my_parser.add_argument('-v', '--verbose', action='store_true', help='an optional argument')

args = my_parser.parse_args()

print('If you read this line it means that you have provided all the parameters')
