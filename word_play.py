def words_with_20_characters(file):
    fin = open(file)
    for line in fin:
        word = line.strip(' ')
        if len(word) > 20:
            print(word)


def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True


def words_no_e(file):
    fin = open(file)
    total_words = 0
    no_e_words = 0
    for line in fin:
        word = line.strip()
        total_words += 1
        if has_no_e(word):
            print(word)
            no_e_words += 1
    print(f'The porcentaje of no e: {(no_e_words*100)/total_words}')


def uses_only(word, string):
    pass



if __name__ == '__main__':
    '''
    words_with_20_characters('words.txt')
    print(has_no_e('Hello'))
    '''
    words_no_e('words.txt')
