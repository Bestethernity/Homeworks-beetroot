def count_lines(name):
    with open(name, 'r') as f:
        f = f.readlines()
        num_lines = 0
        for line in f:
            num_lines += 1

    print('Number of lines in file is ', num_lines)


def count_char(name):
    with open(name, 'r') as f:
        f = f.readlines()
        num_char = 0
        for line in f:
            for char in line:
                if char != " " and char != "\n":
                    num_char += 1

    print('Number of characters in lines is ', num_char)


def test_all(name):
    with open(name, 'r') as f:
        f = f.readlines()
        num_lines = 0
        num_char = 0
        for line in f:
            num_lines += 1
            for char in line:
                if char != " " and char != "\n":
                    num_char += 1

    print('Number of lines in file is ', num_lines)
    print('Number of characters in lines is ', num_char)



