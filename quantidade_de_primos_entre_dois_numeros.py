def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    x = int(input())
    y = int(input())

    inicio = min(x, y)
    fim = max(x, y)

    for num in range(inicio, fim + 1):
        if eh_primo(num):
            print(num)

if __name__ == '__main__':
    main()
