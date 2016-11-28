import sys
from nltk import PorterStemmer
from nltk.corpus import stopwords
import os
import re

word_dict = {}


def sentence_split(paragraph, separator):
    s_list = [paragraph]
    for char in separator:
        s = []
        for substr in s_list:
            s.extend(substr.split(char))
        s_list = s
    return s_list


def remove_punchuation_marks(paragraph):
    '''
    sentences = re.split('!|,|.', paragraph)
    '''

    delimiters = (",", "|", "+", "-", ".", "(", ")", "!", "?")
    sentences = sentence_split(paragraph, delimiters)

    wordlist = []

    for sentence in sentences:
        # print('sentence-->', sentence)
        words = sentence.split()
        wordlist.extend(words)

    # print('ans-->', wordlist)
    return wordlist


def perform_stemming(f_words):
    stemmer = PorterStemmer()
    stem_words = [stemmer.stem(word) for word in f_words]
    return stem_words


def remove_stop_words(f_words):
    filtered_words = [word for word in f_words if word not in stopwords.words('english')]
    return filtered_words


def convert_to_lower_case(f_words):
    words_lower_case = [word.lower() for word in f_words]
    return words_lower_case


def print_word_list_as_document(words):
    print(' '.join(words))


# Remove punchuation marks
# Tokenization of text into words
# Change text to lower case
# Removal of Stop words
# Stemming of the document

def preprocess_file(file_1):
    f_content = open(file_1, 'r', encoding="latin1")
    f_doc = f_content.read()

    # print('\n Original Document\n')
    # print(f_doc)

    f_words = remove_punchuation_marks(f_doc)
    # print('\nAfter punchuation handling\n')
    # print(f_words)

    # f_words = f_doc.split()

    # convert all the words to lower case
    words_lower_case = convert_to_lower_case(f_words)

    # print('\nAfter stop words removal\n')
    words_after_stop_word_removal = remove_stop_words(words_lower_case)
    # print_word_list_as_document(words_after_stop_word_removal)

    # print('\nAfter Stemming\n')
    words_after_stemming = perform_stemming(words_after_stop_word_removal)
    # print_word_list_as_document(words_after_stemming)

    return words_after_stemming


def parse_directory_for_files(dirPath):
    global word_dict

    for root, dir, files in os.walk(dirPath):
        for file in files:
            f = os.path.join(root, file)
            words_in_file = preprocess_file(f)

            # print('file--->', file)


            if 'pos' in f:
                print('pos  file--->', file)
                word_dict['pos'].append(words_in_file)
                # print('inside pos', word_dict['pos'])

            elif 'neg' in f:
                print('neg  file--->', file)
                word_dict['neg'].append(words_in_file)
                # print('neg', word_dict['neg'])


def define_word_dict():
    global word_dict

    word_dict['pos'] = []
    word_dict['neg'] = []


def perform_preprocessing(dirPath):
    global word_dict

    define_word_dict()
    parse_directory_for_files(dirPath)
    # print(word_dict)
    return word_dict


if __name__ == "__main__":
    dirPath = sys.argv[1]
    print(dirPath)

    perform_preprocessing(dirPath)

    # for k in word_dict:
    #    print(k, ' ', word_dict[k])

    # print(word_dict)