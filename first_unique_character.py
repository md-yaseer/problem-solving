s = input()

result_index = -1
for i in range(len(s)):
    repeated = False
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            repeated = True
            break
    if not repeated:
        result_index = i
        break
print(result_index)
