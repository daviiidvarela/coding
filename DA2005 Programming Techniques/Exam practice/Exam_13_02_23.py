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
# def reverse_word(s):
#     return s[::-1]

# #print(reverse_word("DA2005"))

# # B
# def reverse_words(s):
#     words = s.split(" ")
#     out = ""
#     for m in words:
#         out += reverse_word(m) + " "
#     return out

# print(reverse_words("Good luck on the exam"))

## Question 13

# def pair_with(x, mylist):
#     if mylist == []:
#         return []
#     else:
#         return [(x,mylist[0])] + pair_with(x,mylist[1:])

# print(pair_with(2,[1,2,3]))

## Question 14

# def to_pig_german(word):
#     for i in range(len(word)):
#         if word[i] in 'aeiouy':
#             first_vowel = i
#             break
#     return (word[first_vowel:] + word[:first_vowel] + "all")

# print(to_pig_german("knife"))

## Question 15

# while True:
#     x = input("Which sample file do you want to open? ")
#     try:
#         if 1 <= int(x) and int(x) <= 10:
#             with open("sample" + x + ".csv") as h:
#                 do_something(h)
#                 break
#     except ValueError:
#         print('Please put in an integer')
#     except FileNotFoundError:
#         print('Please input an existing filename.')

## Question 16

