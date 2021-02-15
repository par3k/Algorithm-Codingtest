n = 1260
count = 0

list = [500, 100, 50, 10]

for i in list:  # O(K) 즉, list 갯수만금 복잡도는 영향을 받는다.
    count += n // i
    n = n % i

print(count)
