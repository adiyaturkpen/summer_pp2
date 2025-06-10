def rev(sen):
    words=sen.split()
    rev_words = words[::-1]
    rev_sen=' '.join(rev_words)
    print(rev_sen)
sen=input()
rev(sen)