#!/usr/bin/python3
def uppercase(str):
    result = ''
    for let in str:
        asci_let = ord(let)
        if (asci_let >= 97 and asci_let <= 122):
            up_let = chr(asci_let - 32)
            result += up_let
        else:
            result += chr(asci_let)
    print("{}".format(result))
