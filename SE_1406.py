import sys

# 커서 왼쪽, 오른쪽에 있는 문자들을 저장하는 스택
left_stack = list(input()) # 초기 입력 문자열
right_stack = [] # 빈 스택

# 명령어의 개수
M = int(input())

for i in range(M):
    A = sys.stdin.readline().split() 

    if A[0] == "L" and left_stack: 
        right_stack.append(left_stack.pop())

    elif A[0] == "P" :
        left_stack.append(A[1])
    
    elif A[0] == "D" and right_stack:
        left_stack.append(right_stack.pop())

    elif A[0] == "B" and left_stack:
        left_stack.pop()


print("".join(left_stack + list(reversed(right_stack))))