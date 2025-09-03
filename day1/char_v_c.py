def c_charIsVorC(c):
    if(c.isalpha()):
        if(c in ['a','e','i','o','u']):
            print(c," is vowel")
        else:
            print(c," is consonent")
    else:
        print(c ," is not character")
n=input("enter character = ")
c_charIsVorC(n)