def word_count(s):
    s += ' '
    word_dict = {}
    cur_word = ''
    for c in s:
        if c.isspace():
            if cur_word in word_dict:
                word_dict[cur_word] += 1
            elif cur_word != '':
                word_dict[cur_word] = 1
            cur_word = ''
        elif c.isalnum() or c == "'":
            cur_word += c.lower()
    return word_dict


if __name__ == "__main__":
    # print(word_count("Hello    hello"))
    print(word_count('a a\ra\na\ta \t\r\n'))
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(word_count(
    #     'This is a test of the emergency broadcast network. This is only a test.'))
