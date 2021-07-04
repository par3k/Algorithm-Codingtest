## 기능개발 - 문제 설명
# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다.
# 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고,
# 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가
# 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

progresses = [95, 90, 99, 99, 80, 99] # [93, 30, 55]
speeds = [1, 1, 1, 1, 1, 1] # [1, 30, 5]


def solution(progresses, speeds):
    answer = []
    while progresses:
        cnt = 0
        for i in range(len(speeds)):
            progresses[i] += speeds[i]

        if progresses[0] >= 100:
            while progresses:
                if progresses[0] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    cnt += 1
                else:
                    break
            answer.append(cnt)
    return answer


print(solution(progresses, speeds))