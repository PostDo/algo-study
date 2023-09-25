# 배열에서 수 두수를 뽑았아서 x가 나와야 한다.
# 같은 수를 두번 뽑는 경우는 없어야 한다. (2, 2) (3, 3)
# (2, 3) (3, 2)를 뽑으면 안된다.

from collections import defaultdict


n = int(input()) # 숫자 입력받기
list = list(map(int, input().split())) # 배열 
x = int(input()) # x값


num_count = defaultdict(int)

# 딕셔너리 사용해서 각 숫자의 개수 추가 
for num in list :
    num_count[num] += 1  


# 결과값 (쌍의 개수 초기화)
pair_count = 0

for num in list: 
    
    # 같은 숫자끼리 중복되는 경우 제외하기 
    
        
         
    else : 
        
        
        
    



# 중복 제거를 위해 // 2 해줌
print(pair_count // 2)





