# 성적이 낮은 순서로 학생 출력하기

n= int(input())

arr = []

for i in range(n):
    input_data = input().split()
    arr.append((input_data[0], input_data[1]))

arr = sorted(arr, key= lambda student: student[1]) # 점수를 정렬 기준으로 삼는다는 뜻

for student in arr:
    print(student[0], end=' ')

