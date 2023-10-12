# 모든 수의 합
import sys

K = int(sys.stdin.readline())
stack = []

for _ in range(K):
    cmd = int(sys.stdin.readline())

    if cmd > 0:
        stack.append(cmd)
    elif cmd == 0 and len(stack) > 0:
        stack.pop()

print(sum(stack))


