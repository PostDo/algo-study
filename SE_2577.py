number1 = int(input())
number2 = int(input())
number3 = int(input())

result = number1 * number2 * number3
result_str = str(result)


List = [0] * 10


for i in result_str:
    List[int(i)] += 1


for i in range(10):
    print(List[i])
