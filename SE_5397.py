T = int(input())

for _ in range(T):
    left_stack = []
    right_stack = []
    cmd = input()


    for i in cmd:
        if i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif i == '-':
            if left_stack: 
                left_stack.pop() 
        else: 
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    
    print(''.join(left_stack))