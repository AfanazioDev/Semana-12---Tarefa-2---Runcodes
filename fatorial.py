def main():
    n = int(input())

    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i

    print(fatorial)

if __name__ == '__main__':
    main()
