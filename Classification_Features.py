class Classification_Features:

    def __init__(self):

        self.review_helpfulness = {}
        self.tf_idf = {}
        self.polarity = {}
        self.subjectivity = {}
        self.word_dict = {}

        for i in range(1, 6):
            self.review_helpfulness[i] = []
            self.tf_idf[i] = []
            self.polarity[i] = []
            self.subjectivity[i] = []
            self.word_dict[i] = []







