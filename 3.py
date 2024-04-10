def doubleChar(s):
    result = ''
    for char in s:
        result += char * 2
    return result

# Testing the function
print(doubleChar('The'))  # 'TThhee'
print(doubleChar('AAbb'))  # 'AAAAbbbb'
print(doubleChar('Hi-There'))  # 'HHii--TThheerree'
