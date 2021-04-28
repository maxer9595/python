for i in range(1,101):
    #dla podzielnych przz 3 i 5
    if i % 3 == 0 and i % 5 == 0:
        print ('FizzBuzz')
    #dla podzielnych przez 3
    elif i % 3 == 0:
        print ('Fizz')
    #dla podzielnych przez 5
    elif i % 5 == 0:
        print ('Buzz')
    #inaczej wypisz liczbę
    else:
        print (i)