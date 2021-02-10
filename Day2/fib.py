def gen_fib(num):
    out = [1, 1]
    if num < 2:
        return out[:num]
    while(len(out) < num):
        out.append(out[-1] + out[-2])
    return out

if __name__ == '__main__':
    print(gen_fib(1))
    print(gen_fib(10))