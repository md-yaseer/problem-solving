array = input().split('#')
a = array[0].split(',')
b = array[1].split(',')

# Convert (Cast) string to integer
for i in range(len(a)):
    a[i] = int(a[i])

for i in range(len(b)):
    b[i] = int(b[i])

result = []
for element in a:
    if element in b:
        result.append(element)
        
print(result)   