from collections import Counter
import sys
import re

if __name__ ==  "__main__":

    characters = '' # String of characters that words will be allowed to start with
    f = open(sys.argv[2], "w") # Overwrite file to save filtered list of words

    # Get string of letters for variable "characters"
    with open(sys.argv[1], encoding = 'utf-8') as fin: all_letters = ''.join(line[0] for line in fin if line)
    c = Counter(all_letters)
    print(c.most_common())
    print("Total number of characters: " + str(len(c)))
    num_letters = input('How many letters of the most common letters should I include?\n')
    for letter_tuple in c.most_common(int(num_letters)):
        characters += letter_tuple[0]
    
    # Add lines from arg1 file to arg2 file that don't have filtered letters at the beginning
    for line in open(sys.argv[1], encoding = 'utf-8'):
        if not any(line.startswith(x) for x in characters):
            continue
        f.write(line)

    f.close() # Close file for filtered list of words
