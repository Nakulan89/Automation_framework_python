import argparse

tank_fish = {'tank_a': 'shark, tuna, herring',
             'tank_b': 'cod, founder'}

my_parser = argparse.ArgumentParser(description='List the fish in aquarium')
my_parser.add_argument('tank', type=str, help='Tank to print fish from')
my_parser.add_argument('--upper_case', default=False, action='store_true')

args = my_parser.parse_args()

fish = tank_fish.get(args.tank, '')

if args.upper_case:
    fish = fish.upper()

print(fish)

