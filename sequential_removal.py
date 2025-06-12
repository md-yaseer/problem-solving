s = input()

sequence = []
# Derive Sequence
for i in range(1, len(s)//2):
    sequence.append(pow(2, i))

new_str = ''
for j in range(len(s)):
    if j not in sequence:
        new_str = new_str + s[j]
print(new_str)
