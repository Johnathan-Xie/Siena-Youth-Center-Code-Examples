#initial
def gen_table_basic(row_values, column_values, max_space = None):
    for i in row_values:
        for j in column_values:
            print(i * j, end=' ')
        print()
#final
def gen_table(row_values, column_values, max_space = None):
    if max_space == None:
        max_space = 0
        for i in row_values:
            for j in column_values:
                max_space = max(max_space, len(str(i * j)))
    
    for i in row_values:
        for j in column_values:
            print(i * j, end=' ' * (max_space - len(str(i * j)) + 1))
        print()

if __name__ == '__main__':
    gen_table(range(10), range(10))