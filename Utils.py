
def convert_file_to_dictionary(file_name):
    print(file_name)
    f_content = open(file_name, 'r', encoding="latin1")
    f_doc = f_content.read()
    file_data=f_doc.split('\n')
    file_data=file_data[:-1]
    #print(file_data)
    new_dict={}

    den = int(file_data[0].split(':')[1].strip().split('/')[1])
    if den == 0:
        new_dict['helpfulness'] = 0
    else:
        new_dict['helpfulness']=float(file_data[0].split(':')[1].strip().split('/')[0])/float(file_data[0].split(':')[1].strip().split('/')[1])

    new_dict['score']=int(float(file_data[1].split(':')[1].strip()))

    ff = file_data[2].split('review/text:')
    #print(ff)
    new_dict['text']=ff[len(ff)-1].strip()
    return new_dict


def get_feature_list(feature_Dict):

    f_Dict = {}
    for i in range(1, 6):
        feature_list = feature_Dict.word_dict[i]
        feature_v = []

        for word_list in feature_list:
            sentence = None
            for word in word_list:
                if sentence == None:
                    sentence = word
                else:
                    sentence = sentence + " " + word
            feature_v.append(sentence)

        f_Dict[i] = feature_v
    return f_Dict


def buildFeatureList(featureObj):

    feature_dict = {}

    for i in range(1, 6):

        helpfulness = featureObj.review_helpfulness[i]
        subjectivity = featureObj.subjectivity[i]
        polarity = featureObj.polarity[i]
        tf_idf = featureObj.tf_idf[i]

        #print(helpfulness)
        #print(subjectivity)
        #print(polarity)
        #print(tf_idf)


        f_list = []
        for j in range(len(helpfulness)):

            #print("\n\n==============================================================\n\n")
            feature_d = tf_idf[j]
            feature_d['helpfulness'] = helpfulness[j]
            feature_d['subjectivity'] = subjectivity[j]
            feature_d['polarity'] = polarity[j]
            #fprint("\n\n==============================================================\n\n")

            f_list.append(feature_d)

        #print(f_list)
        feature_dict[i] = f_list

    return feature_dict


def printstats(p_dict):
    fo = open('size_feature_vector' + '_output.txt', 'w')

    for i in range(1, 6):
        #print(i, ' ->', len(p_dict[i]))
        fo.write(i, ' ->', len(p_dict[i])

