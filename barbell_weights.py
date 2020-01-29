import itertools

weights = [2, 5, 25]  # you can change the set of weights available
qty_of_weights = [40, 15, 5]  # this is a list of the quantity available of each weight


def restricted_combinations(total_weight):
    """Calculates the different combination of weights on a barbel to reach a target weight"""
    max_of_each_weight = [
        [*range(0, min(total_weight // weights[i] // 2 * 2, qty_of_weights[i]) + 1, 2)] for i in
        range(len(weights))]
    return [comb for comb in itertools.product(*max_of_each_weight) if attempt(comb, total_weight)]


def unrestricted_combinations(total_weight):
    """Calculates the different combination of weights on a barbel to reach a target weight"""
    max_of_each_weight = [[*range(0, total_weight // weight // 2 * 2 + 1, 2)] for weight in weights]
    return [comb for comb in itertools.product(*max_of_each_weight) if attempt(comb, total_weight)]


def attempt(combination: tuple, target_weight: int):
    """Tests if a certain combination of weights achieves the desired total and returns a boolean"""
    total_weight = 0
    for i in range(len(weights)):
        total_weight += weights[i] * combination[i]
    return target_weight == total_weight


# From here on is just testing the above method and printing solutions


def check_answers(solutions, target_weight):
    for solution in solutions:
        temp_weight = 0
        for i in range(len(weights)):
            temp_weight += solution[i] * weights[i]
        if not target_weight == temp_weight:
            return False
    return True


def test_answers(solutions, target_weight):
    if check_answers(solutions, target_weight):
        print("Test PASSED!")
    else:
        print("Test FAILED")


def print_solutions(solutions):
    print(len(solutions), 'possible combinations found')
    for solution in solutions:
        temp_weight = 0
        for i in range(len(weights)):
            temp_weight += solution[i] * weights[i]
            print(solution[i], 'x', str(weights[i]) + 'kg', end="   ")
        print('=', str(temp_weight) + 'kg')


if __name__ == "__main__":
    target = 130  # try adjusting this number

    test_solutions = restricted_combinations(target)
    print_solutions(test_solutions)
    test_answers(test_solutions, target)
