
def mean(num_list):
    return sum(num_list) / len(num_list)


def add_five(num_list):
    return [n + 5 for n in num_list]


# Use the if __name__ == '__main__' to prevent testing executable code from running when another script imports this module

def main():
    print('Testing mean function')
    n_list = [10, 20, 30, 40, 50]
    correct_mean = 30
    assert (mean(n_list) == correct_mean)

    print('Testing the add five function')
    correct_list = [15, 25, 35, 45, 55]
    assert (add_five(n_list) == correct_list)

    print('All test passed!')


if __name__ == '__main__':
    main()