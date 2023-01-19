def encode(text):
    result = ""
    count = 0
    prev_char = text[0]
    for char in text:
        if char != prev_char:
            result+=f"{count}{prev_char}"
            prev_char = char
            count = 1
        else:
            count+=1
    else:
        result+= f"{count}{prev_char}"
    return result

def decode(text):
    result = ""
    digit = True
    count = 0
    for char in text:
        if digit:
            count = int(char)
            digit = False
        else:
            result+=count*char
            digit = True
    return result

text = '11112222333444ggggeeeeqqqwww'
print(f'Исходный текст: {text}')
encode_text = encode(text)
decode_text = decode(encode_text)
print(f'Результат сжатия данных: {encode_text}')
print(f'Результат сжатия данных: {decode_text}')