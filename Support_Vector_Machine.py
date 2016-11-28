from sklearn import svm
from sklearn.feature_extraction import DictVectorizer
import Performance as performance

def Support_Vector_Machine(train_tf_idf_dict, test_tf_idf_dict):
    '''
    #Train data
    '''
    train_1_tf_idf=train_tf_idf_dict['1']
    train_2_tf_idf=train_tf_idf_dict['2']
    train_3_tf_idf=train_tf_idf_dict['3']
    train_4_tf_idf=train_tf_idf_dict['4']
    train_5_tf_idf=train_tf_idf_dict['5']
    training_data_X=[]
    training_data_Y=[]

    for list_each in train_1_tf_idf:
        training_data_X.append(list_each)
        training_data_Y.append('1')        
    for list_each in train_2_tf_idf:
        training_data_X.append(list_each)
        training_data_Y.append('2')
    for list_each in train_3_tf_idf:
        training_data_X.append(list_each)
        training_data_Y.append('3')
    for list_each in train_4_tf_idf:
        training_data_X.append(list_each)
        training_data_Y.append('4')
    for list_each in train_5_tf_idf:
        training_data_X.append(list_each)
        training_data_Y.append('5')

    vec = DictVectorizer()
    print(vec.fit_transform(training_data_X).toarray())
    clf = svm.SVC()
    clf.fit(vec.fit_transform(training_data_X), training_data_Y)

    print('Training end')
    
    '''
    #Test data
    '''

    classified_as_1=0
    correctly_classified_as_1=0
    belongs_to_1=0
    classified_as_2=0
    correctly_classified_as_2=0
    belongs_to_2=0
    classified_as_3=0
    correctly_classified_as_3=0
    belongs_to_3=0
    classified_as_4=0
    correctly_classified_as_4=0
    belongs_to_4=0
    classified_as_5=0
    correctly_classified_as_5=0
    belongs_to_5=0


    test_1_tf_idf=test_tf_idf_dict['1']
    test_2_tf_idf=test_tf_idf_dict['2']
    test_3_tf_idf=test_tf_idf_dict['3']
    test_4_tf_idf=test_tf_idf_dict['4']
    test_5_tf_idf=test_tf_idf_dict['5']
    training_data_X=[]

    for list_each in test_1_tf_idf:
        strdata=clf.predict(vec.transform(list_each))[0]
        if (strdata=='1'):
            classified_as_1=classified_as_1+1;
            correctly_classified_as_1=correctly_classified_as_1+1
        elif(strdata =='2'):
            classified_as_2=classified_as_2+1;
        elif(strdata =='3'):
            classified_as_3=classified_as_3+1;
        elif(strdata =='4'):
            classified_as_4=classified_as_4+1;
        elif(strdata =='5'):
            classified_as_5=classified_as_5+1;
        belongs_to_1=belongs_to_1+1

    for list_each in test_2_tf_idf:
        strdata=clf.predict(vec.transform(list_each))[0]
        if (strdata=='1'):
            classified_as_1=classified_as_1+1;
        elif(strdata =='2'):
            classified_as_2=classified_as_2+1;
            correctly_classified_as_2=correctly_classified_as_2+1
        elif(strdata =='3'):
            classified_as_3=classified_as_3+1;
        elif(strdata =='4'):
            classified_as_4=classified_as_4+1;
        elif(strdata =='5'):
            classified_as_5=classified_as_5+1;
        belongs_to_2=belongs_to_2+1

    for list_each in test_3_tf_idf:
        strdata=clf.predict(vec.transform(list_each))[0]
        if (strdata=='1'):
            classified_as_1=classified_as_1+1;
        elif(strdata =='2'):
            classified_as_2=classified_as_2+1;
        elif(strdata =='3'):
            classified_as_3=classified_as_3+1;
            correctly_classified_as_3=correctly_classified_as_3+1
        elif(strdata =='4'):
            classified_as_4=classified_as_4+1;
        elif(strdata =='5'):
            classified_as_5=classified_as_5+1;
        belongs_to_3=belongs_to_3+1

    for list_each in test_4_tf_idf:
        strdata=clf.predict(vec.transform(list_each))[0]
        if (strdata=='1'):
            classified_as_1=classified_as_1+1;
        elif(strdata =='2'):
            classified_as_2=classified_as_2+1;
        elif(strdata =='3'):
            classified_as_3=classified_as_3+1;
        elif(strdata =='4'):
            classified_as_4=classified_as_4+1;
            correctly_classified_as_4=correctly_classified_as_4+1
        elif(strdata =='5'):
            classified_as_5=classified_as_5+1;
        belongs_to_4=belongs_to_4+1

    for list_each in test_5_tf_idf:
        strdata=clf.predict(vec.transform(list_each))[0]
        if (strdata=='1'):
            classified_as_1=classified_as_1+1;
        elif(strdata =='2'):
            classified_as_2=classified_as_2+1;
        elif(strdata =='3'):
            classified_as_3=classified_as_3+1;
        elif(strdata =='4'):
            classified_as_4=classified_as_4+1;
        elif(strdata =='5'):
            classified_as_5=classified_as_5+1;
            correctly_classified_as_5=correctly_classified_as_5+1
 
        belongs_to_5=belongs_to_5+1
        dict1={}
    dict1['classified_as_1']=classified_as_1
    dict1['correctly_classified_as_1']=correctly_classified_as_1
    dict1['belongs_to_1']=belongs_to_1
    dict1['classified_as_2']=classified_as_2
    dict1['correctly_classified_as_2']=correctly_classified_as_2
    dict1['belongs_to_2']=belongs_to_2
    dict1['classified_as_3']=classified_as_3
    dict1['correctly_classified_as_3']=correctly_classified_as_3
    dict1['belongs_to_3']=belongs_to_3
    dict1['classified_as_4']=classified_as_4
    dict1['correctly_classified_as_4']=correctly_classified_as_4
    dict1['belongs_to_4']=belongs_to_4
    dict1['classified_as_5']=classified_as_5
    dict1['correctly_classified_as_5']=correctly_classified_as_5
    dict1['belongs_to_5']=belongs_to_5


    performance.calculate_accuracy('SVM',dict1)