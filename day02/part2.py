from pprint import pprint
from collections import namedtuple

Round = namedtuple('Round', ['red', 'green', 'blue'])
Game = namedtuple('Game', ['rounds', 'id'])

filename = 'example.txt'
# filename = 'input.txt'

with open(filename, 'r') as fp:
    lines = fp.read().splitlines()


def parse_line(line):
    line = line[len('Game '):]

    # get the rounds and game id
    game_id, rounds = line.split(': ')
    game_id = int(game_id)

    game = Game(id=int(game_id), rounds=[])

    # get the rounds out
    rounds = rounds.split('; ')
    for round in rounds:
        red = 0
        green = 0
        blue = 0

        for chunk in round.split(', '):
            num, color = chunk.split(' ')

            if color == 'red':
                red += int(num)
            elif color == 'green':
                green += int(num)
            elif color == 'blue':
                blue += int(num)
        
        round = Round(
            red=red,
            green=green,
            blue=blue
        )

        game.rounds.append(round)

    return game


def game_power(game):
    min_red = 0
    min_green = 0
    min_blue = 0

    for round in game.rounds:
        if round.red > min_red:
            min_red = round.red
        if round.green > min_green:
            min_green = round.green
        if round.blue > min_blue:
            min_blue = round.blue

    return min_red * min_blue * min_green
    
games = [parse_line(l) for l in lines]
games = [game_power(g) for g in games]

pprint(sum(games))


