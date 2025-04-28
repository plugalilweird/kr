def read_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            yield line
