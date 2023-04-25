import sys
import itertools

def masking(word_lst):

    two_vowel_words = []
    two_vowel_words_masked = []
    
    for word in word_lst:
        vowel_count = 0
        two_vowel_words_vowel_index = []
        list_combinations = []
        for i, char in enumerate(word):
            if char in vowels:
                vowel_count += 1
                two_vowel_words_vowel_index.append(i)
        if vowel_count >= 2:
            for i in range(vowel_count - 1):
                list_combinations = itertools.combinations(two_vowel_words_vowel_index, i + 1)
                for lst in list_combinations:
                    masked_word = word
                    for index in lst:
                        masked_word = masked_word[:index] + '_' + word[index+1:]
                    two_vowel_words_masked.append(masked_word)
                    two_vowel_words.append(word)

    return two_vowel_words, two_vowel_words_masked 

def save_file(word_lst, path):
    with open(path, 'w') as f:
        for word in word_lst:
            f.write(word + '\n')
        f.close()

#--- Main Executable ---#
lang = sys.argv[1]
vowels = ''

if lang == 'Turkish':
    ud_path = '../../UD/UD_Turkish-Kenet/'
    train_path = './Turkish/'
    test_path = '../data/Turkish/'
    lang_code = 'tr_'
    vowels = 'aeioöuıü'
elif lang == 'Finnish':
    ud_path = '../../UD/UD_Finnish-PUD/'
    train_path = './Finnish/'
    test_path = '../data/Finnish/'
    lang_code = 'fi_'
    vowels = 'äöyaou'
elif lang == 'Chukchi':
    ud_path = '../../UD/UD_Chukchi-HSE/'
    train_path = './Chukchi/'
    test_path = '../data/Chukchi/'
    lang_code = 'ckt_'
    vowels = 'aэиoyяеёю'
else:
    print("Invalid language name.")
    exit()

with open('../../slurm/slurm-' + lang + '-test.out', 'r') as out:
    test_words = [word.replace('\n', '') for word in out.readlines()[7:-1]]

with open(ud_path + lang_code + 'words_train_filtered.txt', 'r') as out:
    train_words = [word.replace('\n', '') for word in out.readlines()]

test_words, test_words_masked = masking(test_words)
train_words, train_words_masked = masking(train_words)

save_file(train_words, train_path + 'tgt-train.txt')
save_file(train_words_masked, train_path + 'src-train.txt')
save_file(test_words, test_path + 'tgt-test.txt')
save_file(test_words_masked, test_path + 'src-test.txt')
