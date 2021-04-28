import random

#slownik znakow
sz = 'abcdefghijklmnoprstwxyzqABCDEFGHIJKLMNOPRSTXYZQ@!$'
iloscZnakow = 8
haslo = "".join(random.sample(sz,iloscZnakow))
print(haslo)