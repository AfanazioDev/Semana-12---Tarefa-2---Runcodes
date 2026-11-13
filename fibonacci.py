n = int(input())

t1 = 0
t2 = 1

sequencia = [str(t1), str(t2)]

for _ in range(2, n):
    proximo = t1 + t2
    sequencia.append(str(proximo))
    t1 = t2
    t2 = proximo

print(", ".join(sequencia))
