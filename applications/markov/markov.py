import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read().split()
    combos = {}
    for i, word in enumerate(words):
        if i == len(words) - 1:
            break
        if word in combos:
            combos[word].append(words[i+1])
        else:
            combos[word] = [words[i+1]]

    stop_req_quote = ['."', '!"', '?"']

    def check_start(word):
        if word[0].isupper() or word[0] == '"' and word[len(word) - 1] != '.':
            return True

    start_words = [word for word in combos.keys() if check_start(word)]

    def check_open_quote(word):
        if word[0] == '"':
            return True

    def check_close_quote(word):
        if word[len(word) - 1] == '"':
            return True

    def check_stop_quote(word):
        end = word[-2:]
        if end == '."' or end == '!"' or end == '?"':
            return True

    def check_stop(word):
        end = word[-1:]
        if end == '.' or end == '!' or end == '?':
            return True

    for _ in range(5):
        word = random.choice(start_words)

        open_quote = False

        while not check_stop(word) and not check_stop_quote(word):
            if check_open_quote(word):
                open_quote = True

            if check_close_quote(word):
                open_quote = False

            print(word, end=' ')

            word = random.choice(combos[word])

            if not open_quote:
                while check_close_quote(word):
                    word = random.choice(combos[word])
            else:
                while(check_open_quote(word)):
                    word = random.choice(combos[word])

        if open_quote:
            while not check_stop_quote(word):
                word = random.choice(combos[word])
        else:
            while check_close_quote(word):
                word = random.choice(combos[word])

        print(word, '\n\n')
