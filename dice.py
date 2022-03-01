import random

def main():
    roll = 'y'
    score = Score()
    score.old_score = 0
    while roll != 'n':
        while True:
            roll = input('Roll the dice? [y/n] ')
            if roll.lower() != 'y' and roll.lower() != 'n':
                print(f'Sorry, but "{roll}" is not a valid input. Please try again.')
            else:
                break
        if roll.lower() == 'y':
            dice = []
            dice = generate_dice()
            print(f'You rolled: {dice[0]} {dice[1]} {dice[2]} {dice[3]} {dice[4]}')
            if 1 in dice or 5 in dice:
                for die in dice:
                    this_die = Die()
                    this_die.die_value = die
                    score.new_score = this_die.give_score()
                    score.old_score = score.update_score()
                print(f'Your score: {score.old_score}')
            else:
                print('Craps!')
                roll = 'n'

def generate_dice():
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    die_3 = random.randint(1, 6)
    die_4 = random.randint(1, 6)
    die_5 = random.randint(1, 6)

    return die_1, die_2, die_3, die_4, die_5

class Die:
    # The responsibility of a Die is to hold the
    # value of a die and return its point value

    def __init__(self):
        # Initializes the attribute die_value
        self.die_value = ''

    def give_score(self):
        # A method that returns the score value
        # of a 1 or 5 die, and nothing else
        if self.die_value == 1:
            return 100
        elif self.die_value == 5:
            return 50
        else:
            return 0

class Score:
    # The responsibility of a Score is to hold the running
    # value of the player's score and update it appropriately

    def __init__(self):
        # Initializes the attributes new_score and old_score
        self.new_score = ''
        self.old_score = ''

    def update_score(self):
        # A method that takes the old score and adds the new
        # score to produce the new running score of the player
        self.old_score += self.new_score
        return self.old_score


if __name__ == '__main__':
    main()