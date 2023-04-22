import sys
import itertools

lang = sys.argv[1]
vowels = ''

if lang == 'Turkish':
    ud_path = './UD_Turkish-Kenet/'
    lang_code = 'tr'
    vowels = 'aeioöuıü'
elif lang == 'Finnish':
    ud_path = './UD_Finnish-PUD/'
    lang_code = 'fi'
    vowels = 'äöyaou'
elif lang == 'Chukchi':
    ud_path = './UD_Chukchi-HSE/'
    lang_code = 'ckt'
    vowels = 'aoиy'
elif lang == 'Test':
    ud_path = './UD_Turkish-Kenet/'
    lang_code = 'tr'
    vowels = 'aeioöuıü'
else:
    print("Invalid language name.")
    exit()

#with open('./slurm/slurm-' + lang + '-test.out', 'r') as out:
#    out_words = [word.replace('\n', '') for word in out.readlines()[7:-1]]
with open('./tmp.txt', 'r') as out:
    out_words = [word.replace('\n', '').lower() for word in out.readlines()]

two_vowel_words = []
two_vowel_words_masked = []

for word in out_words:
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

with open('tmp_output.src', 'w') as f:
    for word in two_vowel_words_masked:
        f.write(word + '\n')
    f.close()

with open('tmp_output.tgt', 'w') as f:
    for word in two_vowel_words:
        f.write(word + '\n')
    f.close()
