import csvManager
import main
import predictionManager

def evaluate(round):
    #supponendo che siano sicuramente allineati

    steam_data = "Data/steam/Evaluation/Round"+round+"/Test/steam_data.csv"
    labels = "Data/steam/Evaluation/Round"+round+"/Training/labels.csv"
    tagDescriptions = "Data/steam/Evaluation/Round"+round+"/Training/tagDescriptions.csv"

    tests = csvManager.readFromCsv(steam_data)

    frequentSubTags = main.calculateSubTopics(labels)

    counter = 0
    threshold = 8
    successRateThreshold = 1
    globalPrecision = 0
    globalRecall = 0
    globalSuccessRate = 0

    #model,tfidf_transformer,count_vect = main.trainMainTopics("Data/steam/Evaluation/Round1/Training/labels.csv", "Data/steam/Evaluation/Round1/Training/tagDescriptions.csv")
    models = main.trainModels(labels, tagDescriptions, frequentSubTags)

    for test in tests:
        #print(test[1])
        if(test[0]=="steam_appid"):
            continue
        trueTopics = list(filter(None,test[2:]))

        mainTag = main.predictTopic(test[1], models.get("mainTags")[0], models.get("mainTags")[1], models.get("mainTags")[2])[0][0]

        trueTopics = list(set(frequentSubTags.get(mainTag)) & set(trueTopics))

        if(mainTag in trueTopics):
            counter+=1

            predicted = main.predictTopic(test[1], models.get(mainTag)[0], models.get(mainTag)[1], models.get(mainTag)[2])
            predictedTags = []
            for tuple in predicted[:threshold]:
                predictedTags.append(tuple[0])
            globalPrecision = (globalPrecision+precision(predictedTags, trueTopics))
            globalRecall = (globalRecall+recall(predictedTags, trueTopics))
            globalSuccessRate = (globalSuccessRate+success_rate(predictedTags, trueTopics, successRateThreshold))
        #if(counter>1000):
        #    break

    print("global precision: "+str(globalPrecision/counter))
    print("globalRecall: " + str(globalRecall/counter))
    print("globalSuccessRate: " + str(globalSuccessRate/counter))


def success_rate(predicted, actual, n):
    if actual:
        match = [value for value in predicted if value in actual]
        if len(match)>=n:
            return 1
        else:
            return 0
    else:
        return -1


def precision(predicted,actual):
    if actual:
        true_p = len([value for value in predicted if value in actual])
        false_p = len([value for value in predicted if value not in actual])
        return (true_p / (true_p + false_p))*100
    else:
        return -1


def recall(predicted,actual):
    if actual:
        true_p = len([value for value in predicted if value in actual])
        false_n =len([value for value in actual if value not in predicted])
        return (true_p/(true_p + false_n))*100
    else:
        return -1


def startEvaluation():

    for round in range(1, 11):
        evaluate(str(round))

startEvaluation()