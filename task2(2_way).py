dictionary = {'A': 2, 'C': 5, 'D': 8}
word = 'ACD'


result = ''
result += result.join(str(dictionary[char]) for char in word)
print(result)