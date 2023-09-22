room_number = input()  

number_count = [0] * 10  

for i in room_number:
    if i == '6' or i == '9' :
        if number_count[6] >= number_count[9]:
            number_count[9] += 1
        else :
            number_count[6] += 1

    else :
        number_count[int(i)] += 1


max_count = max(number_count)
print(max_count)



