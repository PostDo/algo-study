
word = input()
list = [0] * 26

for c in word:
    if 'a' <= c <= 'z':
        list[ord(c) - ord('a')] += 1

print(" ".join(map(str, list)))
