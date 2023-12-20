input = sys.stdin.readline

n, m = map(int, input().split())
result = [0 for i in range(n)]
pocket = []

for i in range(m):
    i, j, k = map(int, input().split())
    pok = [i,j,k]
    pocket.append(pok)

print(pocket)

for k in range(len(pocket)):
    for i in range(pocket[k][0],pocket[k][1]+1):
        result[i-1] = pocket[k][2]
        print(result)
    print(f"Step{k+1}!!!")

print(result)


