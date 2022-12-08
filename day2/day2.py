ROCK_OTHER = 'A'
PAPER_OTHER = 'B'
SCISSORS_OTHER = 'C'

ROCK = 'X'
PAPER = 'Y'
SCISSORS = 'Z'

LOSE_LETTER = "X"
DRAW_LETTER = "Y"
WIN_LETTER = "Z"

ROCK_POINTS = 1
PAPER_POINTS = 2
SCISSORS_POINTS = 3

LOSS = 0
DRAW = 3
WIN = 6

get_points = {
    ROCK: ROCK_POINTS,
    PAPER: PAPER_POINTS,
    SCISSORS: SCISSORS_POINTS
}


def get_points_with_force(other_choice, points_from_force):
    # We win
    if points_from_force == 6:
        if other_choice == ROCK_OTHER:
            return get_points.get(PAPER)
        elif other_choice == PAPER_OTHER:
            return get_points.get(SCISSORS)
        else:
            return get_points.get(ROCK)
    # We lose
    elif points_from_force == 0:
        if other_choice == ROCK_OTHER:
            return get_points.get(SCISSORS)
        elif other_choice == PAPER_OTHER:
            return get_points.get(ROCK)
        else:
            return get_points.get(PAPER)
    # We draw
    else:
        if other_choice == ROCK_OTHER:
            return get_points.get(ROCK)
        elif other_choice == PAPER_OTHER:
            return get_points.get(PAPER)
        else:
            return get_points.get(SCISSORS)


def get_points_from_force(choice_input):
    if choice_input == 'X':
        return 6
    elif choice_input == 'Y':
        return 3
    else:
        return 0


def get_winner_points(me, other):
    if me == ROCK and other == ROCK_OTHER:
        return DRAW
    elif me == PAPER and other == PAPER_OTHER:
        return DRAW
    elif me == SCISSORS and other == SCISSORS_OTHER:
        return DRAW
    elif me == ROCK and other == SCISSORS_OTHER:
        return WIN
    elif me == PAPER and other == ROCK_OTHER:
        return WIN
    elif me == SCISSORS and other == PAPER_OTHER:
        return WIN
    else:
        return LOSS


if __name__ == '__main__':
    f = open('day2/day4-test.txt', 'r')
    data = [d.strip() for d in f.readlines()]

    points = []

    for i in range(len(data)):
        opponent, outcome = data[i].split(' ')
        points_choice = get_points_with_force(opponent, outcome)
        print(f'Round {i + 1}: {opponent} {outcome} {point} {points_choice}')
        points.append(point + points_choice)

    print(points)
    print(len(points))
    print(sum(points))
    f.close()
