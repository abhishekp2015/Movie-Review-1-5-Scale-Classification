import sys
import Pre_processor as pre_processor
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

    ##### Train data Processing #########
    train_data = pre_processor.perform_preprocessing(train_filepath)
    feature_list = Utils.get_feature_list(train_data)

    [train_pos_tf_idf, train_neg_tf_idf] = tf_idf.calculate_tfidf(feature_list)
    [train_pos_polarity, train_neg_polarity] = PolaritySubjectivity.calculate_Polarity(feature_list)
    [train_pos_subjectivity, train_neg_subjectivity] = PolaritySubjectivity.calculate_Subjectivity(feature_list)

    train_pos = Utils.buildFeatureList(train_pos_tf_idf, train_pos_polarity, train_pos_subjectivity)
    train_neg = Utils.buildFeatureList(train_neg_tf_idf, train_neg_polarity, train_neg_subjectivity)

    #### Testing Data Processing###########

    test_data = pre_processor.perform_preprocessing(test_filepath)
    feature_list = Utils.get_feature_list(test_data)

    [test_pos_tf_idf, test_neg_tf_idf] = tf_idf.calculate_tfidf(feature_list)
    [test_pos_polarity, test_neg_polarity] = PolaritySubjectivity.calculate_Polarity(feature_list)
    [test_pos_subjectivity, test_neg_subjectivity] = PolaritySubjectivity.calculate_Subjectivity(feature_list)

    test_pos = Utils.buildFeatureList(test_pos_tf_idf, test_pos_polarity, test_pos_subjectivity)
    test_neg = Utils.buildFeatureList(test_neg_tf_idf, test_neg_polarity, test_neg_subjectivity)


    Algorithm_name = sys.argv[3]
    print('Algo-->', Algorithm_name)

    if Algorithm_name == "Naive_Bayes":
        print("===============================================NaiveBayes")
        Naive_Bayes.Naive_Bayes(train_pos, train_neg, test_pos, test_neg)

    elif Algorithm_name == "SVM":
        print("Support_Vector_Machine")
        Support_Vector_Machine.Support_Vector_Machine(train_pos, train_neg, test_pos, test_neg)