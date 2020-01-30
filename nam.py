
numbers1 = [
    "", "jedna", "dva", "tri", "štyri", "päť", "šesť", "sedem", "osem", "deväť", "desať",
    "jedenásť", "dvanásť", "trinásť", "štrnásť", "pätnásť", "šestnásť", "sedemnásť", "osemnásť", "devätnásť"
]

numbers2 = [
    "", "dve", "tri", "štyri", "päť", "šesť", "sedem", "osem", "deväť"
]

pellebois = [
    "m", "b", "tr", "kvadr", "kvint", "sext", "sept", "okt", "non", "dec",
    "undec", "duodec", "tredec", "kvadrodec", "kvindec", "sexdec", "septendec", "oktodec", "novemdec"
]

endings = [
    "ilión", "ilióny", "iliónov",
    "iliarda", "iliardy", "iliárd"
]


def isnumquick(s):
    l = ord('0')
    u = ord('9')
    for i in s:
        c = ord(i)
        if c < l or c > u:
            return False
    return True


def decas(s, feminine = False):
    if s == "00" or s == "1":
        return ""

    num = int(s)
    if num < 20:
        if feminine and num == 2:
            return "dve"
        return numbers1[num - 1]
    else:
        ending = "dsať" if int(s[0]) < 5 else "desiat"
        return numbers1[int(s[0])] + ending + numbers1[int(s[1])]


def hundas(s, feminine = False):
    if s[0] == '0':
        return decas(s[1:], feminine)

    return numbers2[int(s[0]) - 1] + "sto" + decas(s[1:], feminine)


def main():
    number = input("Input number: ")
    while not isnumquick(number):
        print("Number must be a valid integer!")
        number = input("Input number: ")
    
    if number == "0":
        print("nula")
        return

    output = [ ]
    
    triplet_count, left_over = divmod(len(number), 3)
    
    group = triplet_count + (1 if left_over > 0 else 0)

    for i in range(triplet_count + 1):
        offset = left_over + i * 3
        if offset == 0:
            continue
        num = number[max(0, offset - 3):offset]

        tail = ""
        feminine = False
        if group == 2:
            tail = "tisíc"
        elif group != 1:
            n = int(num)
            ending_index = 0 if n == 1 else (1 if n < 5 else 2)
            g, r = divmod(group - 3, 2)
            feminine = r > 0
            separator = (' ' if group > 2 else '')
            tail = separator + pellebois[g] + endings[(3 if feminine else 0) + ending_index] + separator
        group -= 1

        if len(num) < 3:
            output.append(decas(num, feminine) + tail)
        else:
            output.append(hundas(num, feminine) + tail)
    
    print(''.join(output))
    

main()

