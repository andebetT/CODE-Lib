#sales promotion
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    total_bottles = N

    while N >= K:
        new_bottles = N // K
        total_bottles += new_bottles
        N = new_bottles + (N % K)

print(total_bottles)
