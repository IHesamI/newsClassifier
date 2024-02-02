import pickle

topic_cluster_mapping = {
    "economic": [
        'Economy',
        'Economy.Bank and Bourse',
        'Economy.Oil',
        'Economy.Commerce',
        'Economy.Industry',
        'Economy.Agriculture',
        'Economy.Dwelling and Construction'
    ],
    "cultural and artistic": [
        'Science and Culture',
        'Science and Culture.Science.Book',
        'Literature and Art',
        'Literature and Art.Art',
        'Literature and Art.Art.Cinema',
        'Literature and Art.Art.Music',
        'Literature and Art.Art.Theater',
        'Science and Culture.Science',
        'Science and Culture.Science.Medicine and Remedy',
        'Literature and Art.Literature'
    ],
    "political": [
        'Politics',
        'Politics.Iran Politics'
    ],
    "technological": [
        'Science and Culture.Science.Information and Communication Technology'
    ],
    "sports": [
        'Sport',
        'Sport.World Cup'
    ],
    "social": [
        'Social',
        'Social.Women',
        'Social.Religion'
    ],
    "miscellaneous": [
        'Miscellaneous',
        'Miscellaneous.World News',
        'Miscellaneous.Urban',
        'Miscellaneous.Picture',
        'Miscellaneous.Happenings',
        'Miscellaneous.Islamic Councils',
        'Miscellaneous.Picture.Caricature'
    ],
    "tourism": [
        'Tourism'
    ],
    "environment": [
        'Natural Environment'
    ]
}

W2VMODEL = 'w2vmodel'
LOGISTIC_REGRESSION_MODEL = 'lrmodel'
VECTOR_SIZE, WINDOW, SEED, MIN_COUNT, WORKERS = 150, 5, 42, 5, 4


def categoesMapping(cat):
    for key, value in topic_cluster_mapping.items():
        if cat in value:
            return key


def saveObject_(obj, fileName: str):
    filetoSaved = open(fileName, 'ab')
    pickle.dump(obj, filetoSaved)


def loadObject_(fileName: str):
    fileToopen = open(fileName, 'rb')
    return pickle.load(fileToopen)
