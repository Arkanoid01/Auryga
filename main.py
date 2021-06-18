#https://github.com/Kamel773/SourceCodeClassification
import operator

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
import csvManager

def main():
    results = csvManager.getData()

    #csvManager.write2csv(data,label)
    #predict_topics(results)

def predict_topics(data):
    ###Extracting features
    print('Extracting features from dataset')
    count_vect = TfidfVectorizer(input ='train',stop_words = {'english'},lowercase=True,analyzer ='word')

    train_data = []
    label_data = []
    for label in data.keys():
        texts = data.get(label)
        for text in texts:
            train_data.append(text)
            label_data.append(label)

    print(len(train_data))
    print(len(list(data.keys())))


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
    clf = MultinomialNB()

    X_new_counts = count_vect.transform(["America, 1899. Arthur Morgan and the Van der Linde gang are outlaws on the run. With federal agents and the best bounty hunters in the nation massing on their heels, the gang must rob, steal and fight their way across the rugged heartland of America in order to survive. As deepening internal divisions threaten to tear the gang apart, Arthur must make a choice between his own ideals and loyalty to the gang who raised him."
                                         "Red Dead Redemption 2 also includes the shared living world of Red Dead Online – forge your own path as you battle lawmen, outlaw gangs and ferocious wild animals to build a life on the American frontier. Build a camp, ride solo or form a posse and explore everything from the snowy mountains in the North to the swamps of the South, from remote outposts to busy farms and bustling towns. Chase down bounties, hunt, fish and trade, search for exotic treasures, run your own underground Moonshine distillery, or become a Naturalist to learn the secrets of the animal kingdom and much more in a world of astounding depth and detail – includes all new features, gameplay content and additional enhancements released since launch."
                                         "America, 1899. Arthur Morgan and the Van der Linde gang are outlaws on the run. With federal agents and the best bounty hunters in the nation massing on their heels, the gang must rob, steal and fight their way across the rugged heartland of America in order to survive. As deepening internal divisions threaten to tear the gang apart, Arthur must make a choice between his own ideals and loyalty to the gang who raised him."
                                         "Red Dead Redemption 2 also includes the shared living world of Red Dead Online – forge your own path as you battle lawmen, outlaw gangs and ferocious wild animals to build a life on the American frontier. Build a camp, ride solo or form a posse and explore everything from the snowy mountains in the North to the swamps of the South, from remote outposts to busy farms and bustling towns. Chase down bounties, hunt, fish and trade, search for exotic treasures, run your own underground Moonshine distillery, or become a Naturalist to learn the secrets of the animal kingdom and much more in a world of astounding depth and detail – includes all new features, gameplay content and additional enhancements released since launch."])
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)


    clf.fit(train_tfidf, label_data).predict(X_new_tfidf)


    for prob in clf.predict_proba(X_new_tfidf):
        for cat, p in zip(clf.classes_, prob):
            # print(cat+":"+str(p))
            out_dict.update({cat: str(p)})
            ranked_dict = sorted(out_dict.items(), key=operator.itemgetter(1), reverse=True)

    print (ranked_dict)

main()
