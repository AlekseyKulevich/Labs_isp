def factorial(num):
    if num == 0:
        return 1
    else:
        return factorial(num - 1) * num

def main():
    try:
        n = int(input('Enter your number: '))
        print(n, '! = ', factorial(int(n)))
    except:
        print('Wrong input!')

if __name__ == "__main__":
    main()
