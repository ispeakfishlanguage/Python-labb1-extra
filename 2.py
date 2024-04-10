def stringBits(myString):
    # Ta vartannat tecken från strängen som börjar vid index 0
    result = myString[::2]
    return result

# Testar funktionen
print(stringBits('Hello'))  # 'Hlo'
print(stringBits('Hi'))  # 'H'
print(stringBits('Heeololeo'))  # 'Hello'
