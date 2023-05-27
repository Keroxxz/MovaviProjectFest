dictionary = {'A': 2, 'C': 5, 'D': 8}
word = 'ACD'

def digitsfin(word):
    result = ''
    for char in word:
        result += (str(dictionary[char]))
    return result

f = digitsfin(word)
print(f)
