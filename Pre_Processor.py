import sys
import Utils
from nltk import PorterStemmer
from nltk.corpus import stopwords
import os

def sentence_split(paragraph, separator):
    s_list = [paragraph]
    for char in separator:
        s = []
        for substr in s_list:
            s.extend(substr.split(char))
        s_list = s
    return s_list


def remove_punchuation_marks(paragraph):

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
    f_dict = Utils.convert_file_to_dictionary(file_1)
    f_text = f_dict['text']

    #print(f_text)

    # print('\n Original Document\n')
    # print(f_doc)

    f_words = remove_punchuation_marks(f_text)
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

    return [words_after_stemming, f_dict['helpfulness'], f_dict['score']]


def parse_directory_for_files(dirPath, feature_obj):


    for root, dir, files in os.walk(dirPath):

        for file in files:
            f = os.path.join(root, file)
            [words_in_file, helpfulness, score] = preprocess_file(f)
            #print(words_in_file)

            feature_obj.review_helpfulness[score].append(helpfulness)
            feature_obj.word_dict[score].append(words_in_file)

    return feature_obj


def perform_preprocessing(dirPath, feature_obj):

    return parse_directory_for_files(dirPath, feature_obj)



if __name__ == "__main__":
    dirPath = sys.argv[1]
    print(dirPath)

    perform_preprocessing(dirPath)

    # for k in word_dict:
    #    print(k, ' ', word_dict[k])

    # print(word_dict)