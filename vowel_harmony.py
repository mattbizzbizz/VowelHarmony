import sys

lang = sys.argv[1]

if not(lang == 'Turkish' or lang == 'Finnish' or lang == 'Chukchi'):
    print("Invalid language name.")
    exit()

### Open Turkish test.py out file
with open('./slurm/slurm-' + lang + '-test.out', 'r') as f:
    words = [word.replace('\n', '') for word in f.readlines()[7:-1]] # Remove header, tail, and newlines


if lang == "Turkish":

    back_vowel_incorrect_dict = {} # List of words that violate back vowel harmony
    round_vowel_incorrect_dict = {} # List of words that violate round vowel harmony
    
    back_vowel_set = {'a', 'o', 'u', 'ı'}
    round_vowel_set = {'o', 'ö', 'u', 'ü'}
    
    ### Iterate through words in Turkish test.py out file
    for word in words:
    
        back_vowel_word = False # Bool for whether the word has a back vowel
        round_vowel_word = False # Bool for whether the word has a round vowel
    
        vowels = set() # Set of vowels in word
    
        ### Iterate through characters in word
        for char in word:
    
            ### Check if character is a vowel and add it to set
            if char in 'aeioöuıü': vowels.add(char)
    
        ### Check if any vowels in words are back vowels
        if back_vowel_set.intersection(vowels):
    
            ### Check if any vowels aren't back vowels and add to dictionary with value of inconsistent vowel
            if back_vowel_set.union(vowels) != back_vowel_set: back_vowel_incorrect_dict[word] = vowels.difference(back_vowel_set)
    
        ### Check if any vowels in words are round vowels
        if round_vowel_set.intersection(vowels):
    
            ### Check if any vowels aren't round vowels and add to dictionary with value of inconsistent vowel
            if round_vowel_set.union(vowels) != round_vowel_set: round_vowel_incorrect_dict[word] = vowels.difference(round_vowel_set)
    
    
    total = len(words) # Total number of words
    total_back_vowel_correct =  total - len(back_vowel_incorrect_dict) # Total number of correctly formed back vowel words
    total_round_vowel_correct =  total - len(round_vowel_incorrect_dict) # Total number of correctly formed round vowel words
    
    ### Print out total, number of words that follow back/round vowel harmony, and percent of words that follow back/round vowel harmony
    print(f'---Total: {total}---')
    print('---Back Vowels---')
    print(f'-Number correct: {total_back_vowel_correct}')
    print(f'-Percent correct: {(total_back_vowel_correct / total) * 100}')
    print(f'-List of non-Back Harmony Compliant Words: {back_vowel_incorrect_dict}')
    print('---Round Vowels---')
    print(f'-Number correct: {total_round_vowel_correct}')
    print(f'-Percent correct: {(total_round_vowel_correct / total) * 100}')
    print(f'-List of non-Round Harmony Compliant Words: {round_vowel_incorrect_dict}')


elif lang == "Finnish":

    back_vowel_incorrect_dict = {} # List of words that violate back vowel harmony
    front_vowel_incorrect_dict = {} # List of words that violate front vowel harmony
    
    back_vowel_set = {'ä', 'ö', 'y'}
    front_vowel_set = {'a', 'o', 'u'}
    
    ### Iterate through words in Turkish test.py out file
    for word in words:
    
        back_vowel_word = False # Bool for whether the word has a back vowel
        front_vowel_word = False # Bool for whether the word has a front vowel
    
        vowels = set() # Set of vowels in word
    
        ### Iterate through characters in word
        for char in word:
    
            ### Check if character is a vowel that contributes to vowel harmony and add it to set
            if char in 'äöyaou': vowels.add(char)
    
        ### Check if any vowels in words are back vowels
        if back_vowel_set.intersection(vowels):
    
            ### Check if any vowels aren't back vowels and add to dictionary with value of inconsistent vowel
            if back_vowel_set.union(vowels) != back_vowel_set: back_vowel_incorrect_dict[word] = vowels.difference(back_vowel_set)
    
        ### Check if any vowels in words are front vowels
        if front_vowel_set.intersection(vowels):
    
            ### Check if any vowels aren't front vowels and add to dictionary with value of inconsistent vowel
            if front_vowel_set.union(vowels) != front_vowel_set: front_vowel_incorrect_dict[word] = vowels.difference(front_vowel_set)
    
    
    total = len(words) # Total number of words
    total_back_vowel_correct =  total - len(back_vowel_incorrect_dict) # Total number of correctly formed back vowel words
    total_front_vowel_correct =  total - len(front_vowel_incorrect_dict) # Total number of correctly formed front vowel words
    
    ### Print out total, number of words that follow back/front vowel harmony, and percent of words that follow back/front vowel harmony
    print(f'---Total: {total}---')
    print('---Back Vowels---')
    print(f'-Number correct: {total_back_vowel_correct}')
    print(f'-Percent correct: {(total_back_vowel_correct / total) * 100}')
    print('---Front Vowels---')
    print(f'-Number correct: {total_front_vowel_correct}')
    print(f'-Percent correct: {(total_front_vowel_correct / total) * 100}')
    print(f'-List of Vowel Harmony Violating Words: {front_vowel_incorrect_dict}')

elif lang == "Chukchi":

    low_vowel_incorrect_dict = {} # List of words that violate low vowel harmony
    high_vowel_incorrect_dict = {} # List of words that violate high vowel harmony
    
    low_vowel_set = {'ä', 'o'}
    high_vowel_set = {'и', 'y'}
    
    ### Iterate through words in Turkish test.py out file
    for word in words:
    
        low_vowel_word = False # Bool for whether the word has a low vowel
        high_vowel_word = False # Bool for whether the word has a high vowel
    
        vowels = set() # Set of vowels in word
    
        ### Iterate through characters in word
        for char in word:
    
            ### Check if character is a vowel that contributes to vowel harmony and add it to set
            if char in 'aoиy': vowels.add(char)
    
        ### Check if any vowels in words are low vowels
        if low_vowel_set.intersection(vowels):
    
            ### Check if any vowels aren't low vowels and add to dictionary with value of inconsistent vowel
            if low_vowel_set.union(vowels) != low_vowel_set: low_vowel_incorrect_dict[word] = vowels.difference(low_vowel_set)
    
        ### Check if any vowels in words are high vowels
        if high_vowel_set.intersection(vowels):
    
            ### Check if any vowels aren't high vowels and add to dictionary with value of inconsistent vowel
            if high_vowel_set.union(vowels) != high_vowel_set: high_vowel_incorrect_dict[word] = vowels.difference(high_vowel_set)
    
    
    total = len(words) # Total number of words
    total_low_vowel_correct =  total - len(low_vowel_incorrect_dict) # Total number of correctly formed low vowel words
    total_high_vowel_correct =  total - len(high_vowel_incorrect_dict) # Total number of correctly formed high vowel words
    
    ### Print out total, number of words that follow low/high vowel harmony, and percent of words that follow low/high vowel harmony
    print(f'---Total: {total}---')
    print('---Low Vowels---')
    print(f'-Number correct: {total_low_vowel_correct}')
    print(f'-Percent correct: {(total_low_vowel_correct / total) * 100}')
    print('---High Vowels---')
    print(f'-Number correct: {total_high_vowel_correct}')
    print(f'-Percent correct: {(total_high_vowel_correct / total) * 100}')
    print(f'-List of Vowel Harmony Violating Words: {low_vowel_incorrect_dict}')
