# https://www.codewars.com/kata/5547929140907378f9000039/train/python
# Vowel remover
# Easy
# 
# 

def shortcut( s ):
    whitelist = "aeiou"
    new_s = ''.join(c for c in s if c not in whitelist)

    #arr = list(str)
    return new_s


print(shortcut('hello'),'hll')    