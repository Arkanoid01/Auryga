from PythonFiles import csvManager, frequentItemSet, predictionManager

def calculateSubTopics(labels):
    path = labels
    lines = csvManager.readFromCsv(path)
    labels = []
    for line in lines:
        labels.append(line)

    mainTags = ["action","adventure","platformer","rpg","simulation","strategy","sports"]
    blackList = ["indie","casual","early_access"]
    supports = {'action':0.015, 'adventure':0.013, 'platformer':0.0025, 'rpg':0.0075, 'simulation':0.007, 'strategy':0.0075, 'sports':0.001}
    #supports = {'action':0.03, 'adventure':0.03, 'platformer':0.01, 'rpg':0.01, 'simulation':0.01, 'strategy':0.01, 'sports':0.005}
    subTags = {}

    for mainTopic in mainTags:
        frequentSubTags = frequentItemSet.getFrequentSet(mainTopic, mainTags, labels, supports.get(mainTopic))
        frequentSubTags.append(mainTopic)
        for black in blackList:
            if(black in frequentSubTags):
                frequentSubTags.remove(black)
        subTags[mainTopic] = frequentSubTags

    return subTags


def trainMainTopics(labelsPath,tagDescriptionPath):
    path = labelsPath
    lines = csvManager.readFromCsv(path)
    labels = []
    for line in lines:
        labels.append(line)

    path = tagDescriptionPath
    lines = csvManager.readFromCsv(path)
    tagDescriptions = {}
    for line in lines:
        tagDescriptions[line[0]]=line[1:]

    mainTags = ["action","adventure","rpg","platformer","simulation","strategy","sports"]

    dictForTraining = {}
    for tag in tagDescriptions.keys():
        if(tag in mainTags):
            dictForTraining[tag] = tagDescriptions.get(tag)

    model,tfidf_transformer,count_vect = predictionManager.train(dictForTraining)

    return model,tfidf_transformer,count_vect


def predictTopic(textualTest,model,tfidf_transformer,count_vect):

    #print(len(dictForTraining))
    predicted = predictionManager.predict(textualTest, model, tfidf_transformer, count_vect)
    return(predicted)


def trainSubTopics(frequentSubTags,labelsPath,tagDescriptionPath):

    path = labelsPath
    lines = csvManager.readFromCsv(path)
    labels = []
    for line in lines:
        labels.append(line)

    path = tagDescriptionPath
    lines = csvManager.readFromCsv(path)
    tagDescriptions = {}
    for line in lines:
        tagDescriptions[line[0]]=line[1:]

    dictForTraining = {}
    for tag in tagDescriptions.keys():
        if(tag in frequentSubTags):
            dictForTraining[tag] = tagDescriptions.get(tag)

    model, tfidf_transformer, count_vect = predictionManager.train(dictForTraining)

def trainModels(labelsPath,tagDescriptionPath,frequentSubTags):
    models = {}
    path = labelsPath
    lines = csvManager.readFromCsv(path)
    labels = []
    for line in lines:
        labels.append(line)

    path = tagDescriptionPath
    lines = csvManager.readFromCsv(path)
    tagDescriptions = {}
    for line in lines:
        tagDescriptions[line[0]]=line[1:]

    mainTags = ["action","adventure","rpg","platformer","simulation","strategy","sports"]

    dictForTraining = {}
    for tag in tagDescriptions.keys():
        if(tag in mainTags):
            dictForTraining[tag] = tagDescriptions.get(tag)

    model,tfidf_transformer,count_vect = predictionManager.train(dictForTraining)
    modelTriple = [model, tfidf_transformer, count_vect]
    models["mainTags"]=modelTriple


    for mainTag in mainTags:
        dictForTraining = {}
        for tag in tagDescriptions.keys():
            if(tag in frequentSubTags.get(mainTag)):
                dictForTraining[tag] = tagDescriptions.get(tag)
        model,tfidf_transformer,count_vect = predictionManager.train(dictForTraining)
        modelTriple = [model, tfidf_transformer, count_vect]
        models[mainTag]=modelTriple

    return models

def firstRun():
    #apre i file di kaggle e genera 2 elementi, labels in cui per ogni riga contiene tutti i tag associati ad un gioco
    # e tagDescriptions in cui ogni riga contiene un tag e tutti i giochi che sono stati trovati con quel tag
    # entrambe non hanno id del gioco ma sono sincronizzate, nel senso la prima riga corrisponde al primo gioco

    basepath = "Data/steam/Evaluation/Round10/Training/"
    descriptionsPath = "Data/steam/Evaluation/Round10/Training/steam_description_data.csv"
    tagsPath = "Data/steam/Evaluation/Round10/Training/steamspy_tag_data.csv"

    labels, tagDescriptions = csvManager.getLabelsAndTagDescriptions(descriptionsPath, tagsPath)
    csvManager.writeTagDescriptions2csv(tagDescriptions, basepath)
    csvManager.writeLabels2csv(labels, basepath)