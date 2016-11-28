import sys
import Pre_Processor as pre_processor
import Classification_Features as cf
import Feature_tf_idf as tf_idf
import Naive_Bayes as Naive_Bayes
import Support_Vector_Machine as Support_Vector_Machine
import Feature_Polarity_Subjectivity as PolaritySubjectivity
import Utils as Utils

if __name__ == "__main__":

    train_filepath = sys.argv[1]
    test_filepath = sys.argv[2]

    print(train_filepath)
    print(test_filepath)

    # Feature Object
    train_features = cf.Classification_Features()
    test_features = cf.Classification_Features()

    ##### Train data Processing #########

    train_features = pre_processor.perform_preprocessing(train_filepath, train_features)
    #print(train_features.word_dict)
    feature_Dict = Utils.get_feature_list(train_features)

    #print(feature_Dict)

    feature_obj = tf_idf.calculate_tfidf(feature_Dict, train_features)
    train_features = PolaritySubjectivity.calculate_Polarity(feature_Dict, train_features)
    train_features = PolaritySubjectivity.calculate_Subjectivity(feature_Dict, train_features)

    train_f = Utils.buildFeatureList(train_features)

    #print(train_f)

    #### Testing Data Processing###########


    test_features = pre_processor.perform_preprocessing(test_filepath, test_features)
    feature_Dict = Utils.get_feature_list(test_features)

    feature_obj = tf_idf.calculate_tfidf(feature_Dict, test_features)
    test_features = PolaritySubjectivity.calculate_Polarity(feature_Dict, test_features)
    test_features = PolaritySubjectivity.calculate_Subjectivity(feature_Dict, test_features)

    test_f = Utils.buildFeatureList(test_features)


    Algorithm_name = sys.argv[3]
    print('Algo-->', Algorithm_name)

    if Algorithm_name == "Naive_Bayes":
        print("===============================================NaiveBayes")
        Naive_Bayes.Naive_Bayes(train_f, test_f)

    elif Algorithm_name == "SVM":
        print("Support_Vector_Machine")
        Support_Vector_Machine.Support_Vector_Machine(train_f, test_f)