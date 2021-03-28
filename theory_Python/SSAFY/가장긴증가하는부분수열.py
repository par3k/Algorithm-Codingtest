# LIS는 Longest Increasing Subsequence 의 약자
# 어떤 수열에서 특정 부분을 지워서 만들어 낼 수 있는 증가 부분 수열이다.
# 부분수열의 숫자들은 원 배열에서 위치가 이어져 있지 않아도 된다는 특징이 있다.
# LIS는 보통 순증가하는 부분 수열을 대상으로 한다.
# 예를 들어 [1, 4, 6, 8, 3, 5, 6, 7]일 때, [1, 6, 8], [4, 6, 8],
# [1, 7]은 증가 부분 수열인데 이중 가장 긴 부분 열은 [1, 3, 5, 6, 7]이된다.
# 이때 중간의 4, 6, 8 등은 생략한 것을 알 수 있다.


def LIS(arr):
    if not arr:
        return 0

    ans = 1
    for i in range(len(arr)):
        nxt = list()
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                nxt.append(arr[j])
            ans = max(ans, 1 + LIS(nxt))
    return ans