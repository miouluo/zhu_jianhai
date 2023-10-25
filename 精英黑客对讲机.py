dict1 = {'0': 'O', '1': 'I', '2': 'Z', '3': 'E', '4': 'Y',
         '5': 'S', '6': 'G', '7': 'L', '8': 'B', '9': 'P'}


def s(a):
    b = ''
    for char in a:
        if char.isdigit():
            b += dict1[char]
        else:
            b += char
    return b


a = input('请输入暗语：')

print('转换后是：', s(a))
