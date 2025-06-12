s = list(input())

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

j = 0
vowel = [0] * len(s)

for i in range(len(s)):
    if s[i] in vowels:
        vowel[j] = s[i]
        j += 1

for i in range(len(s)):
    if s[i] in vowels:
        j -= 1
        s[i] = vowel[j]

print(''.join(s))

# hello
# holle

# hello world
# hollo werld

# Mohanmmed Yaseer

# Mehemmad Yesaor
