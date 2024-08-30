def ceasar_cipher(direct, text, step):
    ru_lower = [chr(i) for i in range(ord('а'), ord('я') + 1)]
    ru_upper = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
    en_lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    en_upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    answer = ''
    alphabet = ''

    if direct == 'dec':
        step *= -1

    for char in text:
        if char in ru_lower:
            alphabet = ru_lower
        elif char in ru_upper:
            alphabet = ru_upper
        elif char in en_lower:
            alphabet = en_lower
        elif char in en_upper:
            alphabet = en_upper
        else:
            answer += char
            continue

        new_index = (alphabet.index(char) + step) % len(alphabet)
        answer += alphabet[new_index]

    return answer


direction = input('Шифрование или дешифрование (enc шиф/dec деш): ')

if direction in ('enc', 'шиф'):
    text = input('Текст для шифрования: ')
elif direction in ('dec', 'деш'):
    text = input('Текст для дешифрование: ')

# shift_step = int(input('Введите шаг сдвига: '))
# print(ceasar_cipher(direction, text, shift_step))


for step in range(1, 26):
    print(ceasar_cipher(direction, text, step))

# def ceasar_cipher(text):
#     en_lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
#     en_upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

#     answer = ''
#     alphabet = ''
    
#     parts = text.split()
#     for part in parts:
#         step = 0
#         for i in part:
#             if i in en_lower or i in en_upper:
#                 step += 1
                
#         for char in part:
#             if char in en_lower:
#                 alphabet = en_lower
#             elif char in en_upper:
#                 alphabet = en_upper
#             else:
#                 answer += char
#                 continue

#             new_index = (alphabet.index(char) + step) % len(alphabet)
#             answer += alphabet[new_index]
#         answer += ' '
#     return answer


# text = input()

# print(ceasar_cipher(text))








