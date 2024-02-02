import re
from utils import LOGISTIC_REGRESSION_MODEL, W2VMODEL, loadObject_, VECTOR_SIZE
import numpy as np

# converting each sentence to list of words and inserting in sents
# processedData= processedData.a    pply(word_tokenize)


class textClassifier():

    def loadStopWords(self):
        stopWordsFile2 = open('./persian-stopwords/persian', encoding='utf-8')
        combined = stopWordsFile2.read().split('\n')
        return set(combined)

    def __init__(self) -> None:
        self.stopWords = self.loadStopWords()
        self.logisticClassifier = loadObject_(LOGISTIC_REGRESSION_MODEL)
        self.randomForstClassifier = loadObject_('rfclassifier')
        self.w2vmodel = loadObject_(W2VMODEL)
        self.labelEncoder = loadObject_('labelEncoder')

    def removeStopWords(self, text) -> list:
        textList = [word for word in text.split(' ') if word]
        cleanList = [word for word in textList if word not in self.stopWords]
        return cleanList

    def remove_urls(self, text: str):
        url_pattern = re.compile(r'https?://\S+')
        return url_pattern.sub('', text)

    def preProcesser(self, text: str):
        text = self.remove_urls(text)
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\d', '', text)
        text = re.sub(r'\\n', ' ', text)
        return text

    def vectorize(self, sentence):
        words_vecs = [self.w2vmodel.wv[word]
                      for word in sentence if word in self.w2vmodel.wv]
        if len(words_vecs) == 0:
            return np.zeros(VECTOR_SIZE)
        words_vecs = np.array(words_vecs)
        return words_vecs.mean(axis=0)

    def predict(self, text):
        text = self.preProcesser(text)
        textTokenized = self.removeStopWords(text)
        x_test = np.array([self.vectorize(textTokenized)])
        result = self.logisticClassifier.predict(x_test)
        return self.labelEncoder.inverse_transform(result)[0]
