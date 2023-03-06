# s = 'DA2004'
# print({ x : s.count(x) for x in s })

# s = "DA2004"
# out = ""
# for x in s:
#     try:
#         for y in range(int(x)):
#             out += x
#     except:
#         out += "X"
# print(out)

# def foo(mylist):
#     m = 0
#     while mylist:
#         x = mylist.pop()
#         if x > m:
#             m = x
#     return m
# lista = [4,3,1,2,5,0]
# print(foo(lista))

## Question 11 CORRECT
# def percent_to_float(s):
#     s = s[:-1]
#     m = float(int(s)/100)
#     return m
#print(percent_to_float('80%'))

## Question 12
# A
def reverse_word(s):
    return s[::-1]

#print(reverse_word("DA2005"))

# B
def reverse_words(s):
    words = s.split(" ")
    out = ""
    for m in words:
        out += reverse_word(m) + " "
    return out

print(reverse_words("Good luck on the exam"))
