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
else:
    print("Invalid language name.")
    exit()

with open('./slurm/slurm-' + lang + '-test.out', 'r') as out:
    out_words = [word.replace('\n', '') for word in out.readlines()[7:-1]]

two_vowel_words = []

for word in out_words:
    vowel_count = 0
    two_vowel_words_vowel_index = []
    for i, char in enumerate(word):
        if char in vowels:
            vowel_count += 1
            two_vowel_words_vowel_index.append(i)
    if vowel_count >= 2:
        list_combinations = itertools.permutations(two_vowel_words_vowel_index)
        for lst in list_combinations:
            masked_word = word
            for index in lst:
                two_vowel_words.append(masked_word[:index] + '_' + masked_word[index + 1:])

print(two_vowel_words)

