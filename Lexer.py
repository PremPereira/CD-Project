
key_words = ["int","main","for","begin","end","if","printf"]

symbols = {';': "sc", '(': "l_para", ')': "r_para", '+': "add_op", '-': "sub_op", '*': "mul_op", '/': "div_op", ',': "cm"}


token = []



ch = " "
fptr = open("code2.txt","r")

def next_char():
    global ch

    ch = fptr.read(1)
    return ch

def ident_or_int():
    is_number = True
    text = ""

    while ch.isalnum() or ch == '_':
        text += ch
        if not ch.isdigit():
            is_number = False
        next_char()

    if text[0].isdigit():
        if not is_number:
            print("Invalid number!")
            exit(0)
        n = int(text)
        return "integer",n

    if text in key_words:
        return text,1

    return "identifier",text

def follow(expected,ifyes,ifno):
    if next_char() == expected:
        return ifyes,1

    return ifno,1


def gettoken():
    while ch.isspace():
        next_char()

    if len(ch) == 0 : return "EOI",1
    elif ch == '<' : return follow('=',"re_le","re_lt")
    elif ch == '>' : return follow('=',"re_ge","re_gt")
    elif ch == '=' : return follow('=',"re_eq","assign")
    elif ch == '!' : return follow('=',"re_ne","re_not")
    elif ch in symbols:
        sym = symbols[ch]
        next_char()
        return sym,1

    else : return ident_or_int()




#main
while True:
    t = gettoken()

    tok = t[0]


    if tok == "integer": print("integer    %d" % (t[1]))
    elif tok == "identifier": print("identifier   %s" % (t[1]))
    else:
        print(t[0])

    if tok == "EOI":
        break

