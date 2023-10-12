#스택 수열
import sys

n = int(sys.stdin.readline())
stack = []
results = []  # push와 pop 연산을 기록할 리스트

next_num = 1  # 다음에 넣을 숫자를 나타내는 변수

for _ in range(n):
    num = int(sys.stdin.readline())

    while next_num <= num:
        stack.append(next_num)
        results.append('+')
        next_num += 1

    # 스택의 마지막 숫자가 num이랑 같다면 빼기
    if stack[-1] == num:
        stack.pop()
        results.append('-')

    #불가능
    else:
        print('NO')
        exit(0) #프로그램을 정상 종료하는 함수 호출

# 모든 연산을 수행한 후, 결과를 한줄씩 출력
for result in results:
    print(result)
