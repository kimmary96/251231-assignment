def fizzbuzz(n):
    """1부터 n까지의 FizzBuzz를 출력"""
    for i in range(1, n + 1):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

if __name__ == "__main__":
    fizzbuzz(31)
