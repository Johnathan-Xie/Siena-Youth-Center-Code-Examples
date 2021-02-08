def print_py(size):
    for i in range(size):
        print(' ' * (size - i) + '*' * (i * 2 + 1))

if __name__ == '__main__':
    print_py(10)