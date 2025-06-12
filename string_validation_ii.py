s = input()
if len(s) < 3:
    print('invalid')
else:
    if s[1] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        print('vowel')
    elif s[1].isalpha():
        print('consonant')
    elif s[1].isdigit():
        print('digit')
    else:
        print('other')
