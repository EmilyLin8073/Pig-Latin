import os, timeit, string

file = 't8.shakespeare.txt'

def parse_file_and_read_words():
    # Make sure the test file is in the directory
    has_file = os.path.isfile('./%s' %file)
    
    if has_file:
        try:
            with open(file, 'r') as f:
                # Parse the file line by line
                for line in f:
                    # Parse each word in line
                    for word in line.split():
                        print(convert_to_pig_latin(word))
        except Exception as e:
            print('Error when reading and parsing the file: ', e)
    else:
        return 'No file in the directory'

def convert_to_pig_latin(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    ay = 'ay'
    yay = 'yay'
    has_punctuation = ''
    word_without_punctuation = ''
        
    # Check if there's punctuation at the end of the word
    if word[-1] in string.punctuation:
        has_punctuation = word[-1]
        word_without_punctuation = word[:-1]

    
    # If first character is vowel
    if word[0] in vowels:
        if has_punctuation:
            return word_without_punctuation + yay + has_punctuation
        else:
            return word + yay
    #If word begins with consonant or consonant cluster 
    elif word[0] not in vowels:
        if has_punctuation:
            # Find the first vowel position
            for pos, char in enumerate(word):
                if char in vowels:
                    return word_without_punctuation[pos:] + word_without_punctuation[:pos] + ay + has_punctuation
        else:
            # Find the first vowel position
            for pos, char in enumerate(word):
                if char in vowels:
                    return word[pos:] + word[:pos] + ay
    else:
        return word

if __name__ == '__main__':
    start = timeit.default_timer()
    parse_file_and_read_words()
    stop = timeit.default_timer()
    
    print('runtime: ', stop - start)
    