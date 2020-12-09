STOP_WORDS = [
    ' a ', ' an ', ' and ', ' are ', ' as ', ' at ', ' be ', ' by ', ' for ', ' from ', ' has ', ' he ',
    ' i ', ' in ', ' is ', ' it ', ' its ', ' of ', ' on ', ' that ', ' the ', ' to ', ' were ',
    ' will ', ' with '
]

PUNC = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    opened_file = open(file, "r")
    print(opened_file.read().lower().replace(',',''))



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

def remove_stop_words(stop_words_list, file):
    for word in stop_words_list:
        if word in file:
            file=file.replace(word, " ")
    return file

def remove_punctuation(punc, file):
    for element in punc:
        if element in file:
            file=file.replace(element, " ")
    return

data_text = remove_stop_words(STOP_WORDS, file)
print(data_text)
final_text = remove_punctuation(punc, data_text)
print(final_text)
