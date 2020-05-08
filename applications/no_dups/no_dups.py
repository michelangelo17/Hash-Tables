def no_dups(s):
    str_dict = {}
    word_list = s.split()
    for word in word_list:
        if word in str_dict:
            pass
        else:
            str_dict[word] = None
    return ' '.join(str_dict.keys())


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
