import sys

lang = sys.argv[1]

if lang == 'Turkish':
    ud_path = './UD_Turkish-Kenet/'
    lang_code = 'tr'
elif lang == 'Finnish':
    ud_path = './UD_Finnish-PUD/'
    lang_code = 'fi'
elif lang == 'Chukchi':
    ud_path = './UD_Chukchi-HSE/'
    lang_code = 'ckt'
else:
    print("Invalid language name.")
    exit()

with open('./slurm/slurm-' + lang + '-test.out', 'r') as out:
    out_words = [word.replace('\n', '') for word in out.readlines()[7:-1]]

with open(ud_path + lang_code + '_words_train_filtered_shuf.txt', 'r') as train:
    train_words = [word.replace('\n', '') for word in train.readlines()]

with open(ud_path + lang_code + '_words_test_filtered_shuf.txt', 'r') as test:
    test_words = [word.replace('\n', '') for word in test.readlines()]

train_match = []
test_match = []

for word in out_words:
    if word in train_words:
        train_match.append(word)
    elif word in test_words:
        test_match.append(word)

print(f'---Matching words in train file: {len(train_match)}/{len(out_words)}')
for word in train_match:
    print(word)

print(f'---Matching words test file: {len(test_match)}/{len(out_words)}')
for word in test_match:
    print(word)
