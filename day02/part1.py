from pprint import pprint
from collections import namedtuple

Round = namedtuple('Round', ['red', 'green', 'blue'])
Game = namedtuple('Game', ['rounds', 'id'])

# filename = 'example.txt'
filename = 'input.txt'

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


def validate_game(game):
    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    RED_LIMIT = 12
    GREEN_LIMIT = 13
    BLUE_LIMIT = 14

    for round in game.rounds:
        if round.red > RED_LIMIT:
            return False
        if round.green > GREEN_LIMIT:
            return False
        if round.blue > BLUE_LIMIT:
            return False

    return True
    
games = [parse_line(l) for l in lines]
games = [g for g in games if validate_game(g)]

valid_ids = [g.id for g in games]

pprint(sum(valid_ids))


