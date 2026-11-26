s = input()


def hashtag_gen(text):
    new_s = text.replace(' ','_')
    new_s = '#' + new_s
    return new_s

print(hashtag_gen(s))
