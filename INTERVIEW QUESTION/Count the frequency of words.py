def freq_word():
    strr = input('Enter the sentece: ')
    new_sentece = strr.split()
    d={}

    for i in new_sentece:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)
freq_word()
# 'sheena loves eating apple. her sister also loves eating apple.'
