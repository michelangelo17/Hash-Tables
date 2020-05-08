with open("robin.txt") as f:
    words = f.read().split()

    word_count = {}

    for word in words:
        word = word.lower()

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    all_items = list(word_count.items())

    all_items.sort(key=lambda x: x[1], reverse=True)

    largest_key = max(len(key) for key in word_count.keys())

    for item in all_items:
        if not item[0].isalpha():
            pass
        else:
            space_num = largest_key - len(item[0])
            spaces = ' ' * space_num + '  '
            line = '#' * item[1]

            print(f'{item[0]}:{spaces}{line}')
