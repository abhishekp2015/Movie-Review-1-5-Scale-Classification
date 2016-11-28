import nltk
import Performance as performance
from sklearn.feature_extraction import DictVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV

def SVM_Multiclass(train_tf_idf_dict, test_tf_idf_dict):
    '''
    #Train data
    '''

    # pos_list=train_input_list['pos']
    # neg_list=train_input_list['neg']
    train_1_tf_idf = train_tf_idf_dict[1]
    train_2_tf_idf = train_tf_idf_dict[2]
    train_3_tf_idf = train_tf_idf_dict[3]
    train_4_tf_idf = train_tf_idf_dict[4]
    train_5_tf_idf = train_tf_idf_dict[5]
    training_data_X = []
    training_data_Y = []

    for list_each in train_1_tf_idf:
        training_data_X.append(list_each)
        training_data_Y.append(1)
    for list_each in train_2_tf_idf:
        training_data_X.append(list_each)
        training_data_Y.append(2)
    for list_each in train_3_tf_idf:
        training_data_X.append(list_each)
        training_data_Y.append(3)
    for list_each in train_4_tf_idf:
        training_data_X.append(list_each)
        training_data_Y.append(4)
    for list_each in train_5_tf_idf:
        training_data_X.append(list_each)
        training_data_Y.append(5)

    vec = DictVectorizer()
    #from sklearn.naive_bayes import MultinomialNB
    #clf = MultinomialNB()
    #clf.fit(vec.fit_transform(training_data_X), training_data_Y)

    '''
    param_grid = [
        {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
        {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
    ]
    '''

    #svm_multi = OneVsRestClassifier(LinearSVC(random_state=0))
    #cv = StratifiedShuffleSplit(n_splits=5, test_size=0.2, random_state=42)
    #grid = GridSearchCV(svm_multi, param_grid=param_grid, cv=cv)
    #grid.fit(vec.fit_transform(training_data_X), training_data_Y)

    #print("The best parameters are %s with a score of %0.2f->" % (grid.best_params_, grid.best_score_))

    '''
    C_2d_range = [1e-2, 1, 1e2]
    gamma_2d_range = [1e-1, 1, 1e1]
    classifiers = []
    for C in C_2d_range:
        for gamma in gamma_2d_range:
            clf = svm_multi(C=C, gamma=gamma)
            clf.fit(X_2d, y_2d)
            classifiers.append((C, gamma, clf))
    '''

    svm_multi = OneVsRestClassifier(LinearSVC(random_state=0))
    svm_multi.fit(vec.fit_transform(training_data_X), training_data_Y)

    '''
    #Test data
    '''

    print('Training end')

    classified_as_1 = 0
    correctly_classified_as_1 = 0
    belongs_to_1 = 0
    classified_as_2 = 0
    correctly_classified_as_2 = 0
    belongs_to_2 = 0
    classified_as_3 = 0
    correctly_classified_as_3 = 0
    belongs_to_3 = 0
    classified_as_4 = 0
    correctly_classified_as_4 = 0
    belongs_to_4 = 0
    classified_as_5 = 0
    correctly_classified_as_5 = 0
    belongs_to_5 = 0

    test_1_tf_idf = test_tf_idf_dict[1]
    test_2_tf_idf = test_tf_idf_dict[2]
    test_3_tf_idf = test_tf_idf_dict[3]
    test_4_tf_idf = test_tf_idf_dict[4]
    test_5_tf_idf = test_tf_idf_dict[5]

    for list_each in test_1_tf_idf:
        strdata=svm_multi.predict(vec.transform(list_each))[0]
        if (strdata==1):
            classified_as_1=classified_as_1+1;
            correctly_classified_as_1=correctly_classified_as_1+1
        elif(strdata ==2):
            classified_as_2=classified_as_2+1;
        elif(strdata ==3):
            classified_as_3=classified_as_3+1;
        elif(strdata ==4):
            classified_as_4=classified_as_4+1;
        elif(strdata ==5):
            classified_as_5=classified_as_5+1;
        belongs_to_1=belongs_to_1+1

    for list_each in test_2_tf_idf:
        strdata=svm_multi.predict(vec.transform(list_each))[0]
        if (strdata==1):
            classified_as_1=classified_as_1+1;
        elif(strdata ==2):
            classified_as_2=classified_as_2+1;
            correctly_classified_as_2=correctly_classified_as_2+1
        elif(strdata ==3):
            classified_as_3=classified_as_3+1;
        elif(strdata ==4):
            classified_as_4=classified_as_4+1;
        elif(strdata ==5):
            classified_as_5=classified_as_5+1;
        belongs_to_2=belongs_to_2+1

    for list_each in test_3_tf_idf:
        strdata=svm_multi.predict(vec.transform(list_each))[0]
        if (strdata==1):
            classified_as_1=classified_as_1+1;
        elif(strdata ==2):
            classified_as_2=classified_as_2+1;
        elif(strdata ==3):
            classified_as_3=classified_as_3+1;
            correctly_classified_as_3=correctly_classified_as_3+1
        elif(strdata ==4):
            classified_as_4=classified_as_4+1;
        elif(strdata ==5):
            classified_as_5=classified_as_5+1;
        belongs_to_3=belongs_to_3+1

    for list_each in test_4_tf_idf:
        strdata=svm_multi.predict(vec.transform(list_each))[0]
        if (strdata==1):
            classified_as_1=classified_as_1+1;
        elif(strdata ==2):
            classified_as_2=classified_as_2+1;
        elif(strdata ==3):
            classified_as_3=classified_as_3+1;
        elif(strdata ==4):
            classified_as_4=classified_as_4+1;
            correctly_classified_as_4=correctly_classified_as_4+1
        elif(strdata ==5):
            classified_as_5=classified_as_5+1;
        belongs_to_4=belongs_to_4+1

    for list_each in test_5_tf_idf:
        strdata=svm_multi.predict(vec.transform(list_each))[0]
        if (strdata==1):
            classified_as_1=classified_as_1+1;
        elif(strdata ==2):
            classified_as_2=classified_as_2+1;
        elif(strdata ==3):
            classified_as_3=classified_as_3+1;
        elif(strdata ==4):
            classified_as_4=classified_as_4+1;
        elif(strdata ==5):
            classified_as_5=classified_as_5+1;
            correctly_classified_as_5=correctly_classified_as_5+1

        belongs_to_5 = belongs_to_5 + 1

    # print('Classification end')

    #    print('classified_as_pos-->', classified_as_pos)
    #    print('correctly_classified_as_pos->', correctly_classified_as_pos)
    #    print('belongs_to_pos-->', belongs_to_pos)
    #    print('classified_as_neg->', classified_as_neg)
    #    print('correctly_classified_as_neg-->', correctly_classified_as_neg)
    #    print('belongs_to_neg-->', belongs_to_neg)
    dict1 = {}
    dict1['classified_as_1'] = classified_as_1
    dict1['correctly_classified_as_1'] = correctly_classified_as_1
    dict1['belongs_to_1'] = belongs_to_1
    dict1['classified_as_2'] = classified_as_2
    dict1['correctly_classified_as_2'] = correctly_classified_as_2
    dict1['belongs_to_2'] = belongs_to_2
    dict1['classified_as_3'] = classified_as_3
    dict1['correctly_classified_as_3'] = correctly_classified_as_3
    dict1['belongs_to_3'] = belongs_to_3
    dict1['classified_as_4'] = classified_as_4
    dict1['correctly_classified_as_4'] = correctly_classified_as_4
    dict1['belongs_to_4'] = belongs_to_4
    dict1['classified_as_5'] = classified_as_5
    dict1['correctly_classified_as_5'] = correctly_classified_as_5
    dict1['belongs_to_5'] = belongs_to_5

    performance.calculate_accuracy('SVM_Multiclass', dict1)
