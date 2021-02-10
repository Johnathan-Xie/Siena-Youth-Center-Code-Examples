def multiply_dict(inp):
    return {key: (value * key) for key, value in inp.items()}

def make_numerical(values):
    unq_vals = list(set(values))
    mapping = {unq_vals[i]: i for i in range(len(unq_vals))}
    return [mapping[i] for i in values]

if __name__ == '__main__':
    print(multiply_dict({3: 5, 5: 10}))
    print(make_numerical(['these', 'are', 'some', 'things', 'these', 'some', 'these', 'things']))