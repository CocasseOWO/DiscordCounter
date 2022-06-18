import pyperclip
number = int(input("start number : "))
count = 0
loop = 0
res = ''

while loop < 10000:
    loop = loop + 1
    while count < 333:
        number = number + 1
        res += f'\n{number}'
        count = count + 1
    count = 0
    pyperclip.copy(res)
    res = ''
    input("paste then press enter")

input("press enter to exit")


