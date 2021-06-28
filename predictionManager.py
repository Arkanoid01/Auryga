import operator

from sklearn.naive_bayes import MultinomialNB, GaussianNB, ComplementNB

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer



def predict(data,textualTest):

    ###Extracting features
    print('Extracting features from dataset')
    count_vect = TfidfVectorizer(input ='train',stop_words = {'english'},lowercase=True,analyzer ='word')

    train_data = []
    label_data = []
    for label in data.keys():
        texts = data.get(label)
        print(label)
        print(len(texts))
        for text in texts:
            train_data.append(text)
            label_data.append(label)

    #print(len(train_data))
    #print(len(list(data.keys())))


    train_vectors = count_vect.fit_transform(train_data)
    train_vectors.shape
    tfidf_transformer = TfidfTransformer()
    train_tfidf = tfidf_transformer.fit_transform(train_vectors)
    train_tfidf.shape
    # with open('train.pickle', 'wb') as fin:
    #      pickle.dump(train_vectors, fin)
    print('Training a Multinomial Naive Bayes (MNB)')
    ###train model
    out_dict={}
    #feature_extraction(train_data)
    #model = MultinomialNB()
    #model = GaussianNB()
    model = ComplementNB()

    X_new_counts = count_vect.transform([textualTest])
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)


    model.fit(train_tfidf, label_data).predict(X_new_tfidf)
    #model.fit(train_tfidf, label_data).predict(X_new_tfidf)

    for prob in model.predict_proba(X_new_tfidf):
        for cat, p in zip(model.classes_, prob):
            # print(cat+":"+str(p))
            out_dict.update({cat: str(p)})
            ranked_dict = sorted(out_dict.items(), key=operator.itemgetter(1), reverse=True)

    print (ranked_dict)
    return ranked_dict