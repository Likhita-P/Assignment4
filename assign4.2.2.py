vowel=('a','e','i','o','u','A','E','I','O','U')
def isvowel(char):
    if(len(char)==1):
        if char in vowel:
            return True
        else:
            return False
c=input("enter character")
res=isvowel(c)
print(res)

