from textblob import TextBlob


def calculate_Subjectivity(sentence_dict, featureObj):

    for i in range(1, 6):
        subjectivity = []
        for sentence in sentence_dict[i]:
            sent = TextBlob(sentence)
            s = sent.sentiment.subjectivity
            subjectivity.append(s)
        featureObj.subjectivity[i] = subjectivity

    return featureObj


def calculate_Polarity(sentence_dict, featureObj):

    for i in range(1, 6):
        polarity = []
        for sentence in sentence_dict[i]:
            sent = TextBlob(sentence)
            p = sent.sentiment.polarity
            polarity.append(p)
        featureObj.polarity[i] = polarity
    return featureObj