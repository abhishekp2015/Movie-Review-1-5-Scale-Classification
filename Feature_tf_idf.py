from sklearn.feature_extraction.text import TfidfVectorizer
import sys
import numpy as np
import pickle
import csv
import Utils as Utils

#corpus = [["This is very strange", "This is very nice"]]
#corpus = [["This", "is", "very", "strange"], ["This", "is", "very", "nice"]]

all_word_list = []

def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def save_as_csv(obj, name):

    l = obj[0]
    header = []

    for k in l:
        header.append(k)

    data = []
    for list_obj in obj:
        d_list = []
        for k in header:
            d_list.append(list_obj[k])
        data.append(d_list)

    #print(header)

    myfile = open(name+'_as_.csv', 'w',  newline='\n')
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(data)




def calculate_tfidf(feature_dict, feature_obj):

    for i in range(1, 6):
        vectorizer1 = TfidfVectorizer(min_df=1)
        X = vectorizer1.fit_transform(feature_dict[i])
        tf_idf = np.array(X.todense()).tolist()

        f_dict = []
        for l in tf_idf:
            d = dict(zip(vectorizer1.get_feature_names(), l))
            f_dict.append(d)

        #print(f_dict)
        feature_obj.tf_idf[i] = f_dict
    return feature_obj


if __name__ == "__main__":

    dir1 = sys.argv[1]
    calculate_tfidf(dir1)