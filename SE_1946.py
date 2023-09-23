import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    applicant = []
    for _ in range(N):
        applicant.append(list(map(int, input().split())))
    
    applicant.sort()

    cut_line = applicant[0][1] 

    cnt = 1  
    for i in applicant:
        if cut_line > i[1]:
            cnt += 1
            cut_line = i[1] 
    
    print(cnt)