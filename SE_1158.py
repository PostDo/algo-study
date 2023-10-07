import sys
input = sys.stdin.readline
class CircleList:
    class Node:
        def __init__(self,item,link):
            self.item = item # 데이터 저장
            self.next = link # 다음 노드 저장
    
    def __init__(self):
        self.last = None # last는 연결리스트에서 마지막 노드를 가리킨다. 
        self.size = 0 # size는 연결리스트의 노드 수 --> 둘 다 아직 초기이니 없다. 
    
    # 삽입
    def insert(self,item): #item 매개변수를 받아서 새로운 노드 생성하고 리스트에 넣음
        n = self.Node(item,None)
        if(self.size == 0): # 리스트가 비어있다면 n의 next는 자기 자신
            n.next = n # next는 포인터로 다음 노드를 가리킨다. 
            self.last = n # last는 연결 리스트의 끝에 있는 노드를 가리키는 역할, 연결리스트의 마지막 노드와 첫번째 노드를 연결
        else: # 리스트가 비어있지 않은 경우라면
            n.next = self.last.next # n의 next는 리스트의 마지막 노드
            self.last.next = n # 리스트의 마지막 노드가 됨
        self.size += 1 # 새로운 노드가 추가되었음을 의미한다. 
    
    # 삭제 --> 삭제하려는 노드의 이전 노드 p의 next를 
    def delete(self,p): #p는 삭제하려는 노드의 이전 노드이다. 
        x = p.next # p.next는 삭제할 노드를 가리키는 포인터이다. x에는 삭제할 노드가 저장
        if(self.size == 1): # 리스트에 노드 1개 있으면
            self.last = None # 마지막 노드는 없음
        else: 
            p.next = x.next # p의 다음 노드를 삭제하려는 노드의 다음 노드로 연결, x가 2이면 3이 저장
        self.size -= 1 # -1해서 삭제를 나타냄
        return x.item # 삭제한 데이터 반환
 
    def print_list(self,N,K):
        L = [] # 빈 리스트,제거된 사람들 추가 됨
        p = self.last # 리스트의 마지막 노드를 가리킨다. 순열을 계산할 때 시작위치를 나타냄
 
        for _ in range(N): # 전체 인원 수 만큼 작업 반복
            for j in range(K-1): # k 번째 사람을 제거하기 위해 k-1명을 건너뛴다. 
                p = p.next #k번째 사람을 찾음, 삭제할 노드 
            L.append(self.delete(p)) # K번째 사람 삭제해서 리스트에 추가  
        return L


N,K = map(int,input().split())
c = CircleList() # 클래서 객체 c 
for i in range(N,0,-1): # 7~1
    c.insert(i) 

L = c.print_list(N,K) # 결과를 리스트로 저장
print('<',end='')
print(', '.join(str(x) for x in L),end='')
print('>')