#https://github.com/Kamel773/SourceCodeClassification

import csvManager
import frequentItemSet
import predictionManager

def main():

    # textualTest=",Play the world's number 1 online action game. Engage in an incredibly realistic brand of terrorist warfare in this wildly popular team-based game. Ally with teammates to complete strategic missions. Take out enemy sites. Rescue hostages. Your role affects your team's success. Your team's success affects your role.,Play the world's number 1 online action game. Engage in an incredibly realistic brand of terrorist warfare in this wildly popular team-based game. Ally with teammates to complete strategic missions. Take out enemy sites. Rescue hostages. Your role affects your team's success. Your team's success affects your role.,Play the world's number 1 online action game. Engage in an incredibly realistic brand of terrorist warfare in this wildly popular team-based game. Ally with teammates to complete strategic missions. Take out enemy sites. Rescue hostages. Your role affects your team's success. Your team's success affects your role."
    # textualTest="Something's rotten in the land of the dead, and you're being played for a sucker. Meet Manny Calavera, travel agent at the Department of Death. He sells luxury packages to souls on their four-year journey to eternal rest. But there's trouble in paradise. Help Manny untangle himself from a conspiracy that threatens his very salvation.One of the most acclaimed adventure games of all time is now back, better than ever. Grim Fandango's epic story of four years in the life (or death) of Manny Calavera, travel agent to the dead, has been remastered to look, sound, and control even better than when it won GameSpot's Game of the Year award upon its original launch. Grim Fandango still stands as a classic of the genre, with unforgettable characters and unique combination of film noir and Mexican folklore. "
    # textualTest="Cyberpunk 2077 is an open-world, action-adventure story set in Night City, a megalopolis obsessed with power, glamour and body modification. You play as V, a mercenary outlaw going after a one-of-a-kind implant that is the key to immortality. You can customize your character's cyberware, skillset and playstyle, and explore a vast city where the choices you make shape the story and the world around you. Become a cyberpunk, an urban mercenary equipped with cybernetic enhancements and build your legend on the streets of Night City. Create your character from scratch and choose their background out of three unique Lifepaths. Take the role of a gang-wise Street Kid, freedom-loving Nomad, or a ruthless Corpo. Enter the massive open world of Night City, a place that sets new standards in terms of visuals, complexity and depth. Explore the bustling megalopolis of the future and its extensive districts, each with exceptional visual flavor, inhabitants and chances to earn cash. Interact with members of powerful gangs who rule the streets of Night City."
    # textualTest="There are two worlds. One we know as our world, a world of science and logic and stark reality. The other world lies behind the veil of sleep; an Arcadian realm of magic and chaos, a realm where dreams may come true. Imagine being able to travel between these two worlds, between Stark and Arcadia. Imagine being able to Shift between realities as easily as stepping through a doorway. In The Longest Journey, you can. And in order to save the precious Balance between worlds, between order and chaos, between science and magic, you must. The Longest Journey is an adventure through the twin worlds of Stark and Arcadia, seen through the eyes of April, an 18-year old art student. The game you cannot miss! Extraordinary adventure game with over 150 locations in two different dimensions. Gripping story with many twists, smooth gameplay, and a fantastic music, will accompany you throughout the entire game that is over 50 hours long. Very interesting characters, with great art design and intriguing background stories."
    # textualTest="America, 1899. Arthur Morgan and the Van der Linde gang are outlaws on the run. With federal agents and the best bounty hunters in the nation massing on their heels, the gang must rob, steal and fight their way across the rugged heartland of America in order to survive. As deepening internal divisions threaten to tear the gang apart, Arthur must make a choice between his own ideals and loyalty to the gang who raised him. Now featuring additional Story Mode content and a fully-featured Photo Mode, Red Dead Redemption 2 also includes free access to the shared living world of Red Dead Online, where players take on an array of roles to carve their own unique path on the frontier as they track wanted criminals as a Bounty Hunter, create a business as a Trader, unearth exotic treasures as a Collector or run an underground distillery as a Moonshiner and much more. With all new graphical and technical enhancements for deeper immersion, Red Dead Redemption 2 for PC takes full advantage of the power of the PC to bring every corner of this massive, rich and detailed world to life including increased draw distances; higher quality global illumination and ambient occlusion for improved day and night lighting; improved reflections and deeper, higher resolution shadows at all distances; tessellated tree textures and improved grass and fur textures for added realism in every plant and animal. Red Dead Redemption 2 for PC also offers HDR support, the ability to run high-end display setups with 4K resolution and beyond, multi-monitor configurations, widescreen configurations, faster frame rates and more."
    # textualTest="Neo Berlin 2062. Tina – a nine-year-old orphan – lives with SAM-53 – her big clumsy robot guardian –in a rooftop makeshift shelter in Neo-Berlin, a dark megalopolis controlled by corporations. Tina is an urban jungle kid, who has learned to live alone, scavenging from city dumpsters and eking out a living from scraps. Her funny robot is always with her, programmed to protect her no matter what.One day, the little girl discovers that her father left her an important mission: to finish his plan to save the world from grayness! Tina and SAM embark on an incredible adventure across different realities full of bizarre robotic creatures and grotesque human beings. Through puzzles and exciting dialogues, they’ll find out the true meaning of being alive."
    # 0textualTest = "Gran Turismo is a racing game. The player must maneuver a car to compete against artificially intelligent drivers on various race tracks. The game uses two different modes: Arcade Mode and Simulation Mode (Gran Turismo Mode in PAL and Japanese versions). In the arcade mode, the player can freely choose the courses and vehicles they wish to use. Winning races unlocks additional cars and courses. However, simulation mode requires the player to earn different levels of driver's licenses in order to qualify for events, and earn credits (money), trophies and prize cars by winning race championships. Winning one particular championship also unlocks a video and a few additional demonstration tracks. Credits can be used to purchase additional vehicles, and for parts and tuning. Gran Turismo features 140 cars and 11 race tracks (as well as their reversed versions). Two Honda NSX cars from 1992 were included in the Japanese version, but were removed from the North American and European versions. There is also a 1967 Chevrolet Corvette and a 1998 Mazda Roadster exclusive to the Arcade mode. "
    textualTest = "Pro Evolution Soccer (abbreviated as PES and currently branded as eFootball PES), known in Japan as Winning Eleven[a] (currently branded as eFootball Winning Eleven[b]), is a series of association football simulation video games developed and released annually since 1995. It is developed and published by Konami. It consists of eighteen main instalments and several spin-off style titles and it has seen releases on many different platforms. It is itself a sister series of Konami's earlier International Superstar Soccer and has been released under different names before the name Pro Evolution Soccer was established worldwide. The series has consistently achieved critical and commercial success. PES has also been used in esports. eFootball.Open (formerly known as PES World Finals or PES League) is the esports world championship held by Konami annually since 2010. In association football circles, Pro Evolution Soccer has a longstanding rivalry with EA's FIFA series.[1] PES is the second largest association football video game franchise after FIFA, with the rivalry between the two franchises considered the greatest rivalry in the history of sports video games.[2] Listed as one of the best-selling video game franchises, the PES series has sold 111 million copies worldwide, in addition to 400 million mobile game downloads, as of December 2020.[3] Konami also created a similar mobile game called PESCM or Pro Evolution Soccer Club Manager. "
    # textualTest = "Paradox Development Studio is back with the fourth installment of the award-winning Europa Universalis series. The empire building game Europa Universalis 4 gives you control of a nation to guide through the years in order to create a dominant global empire. Rule your nation through the centuries, with unparalleled freedom, depth and historical accuracy. True exploration, trade, warfare and diplomacy will be brought to life in this epic title rife with rich strategic and tactical depth."

    #mainTag = predictMainTopic(textualTest)

    predictSubTopics(textualTest, "sports")


def calculateSubTopics(labels):
    path = labels
    lines = csvManager.readFromCsv(path)
    labels = []
    for line in lines:
        labels.append(line)

    mainTags = ["action","adventure","platformer","rpg","simulation","strategy","sports"]
    blackList = ["indie","casual","early_access"]
    supports = {'action':0.015, 'adventure':0.013, 'platformer':0.0025, 'rpg':0.0075, 'simulation':0.007, 'strategy':0.0075, 'sports':0.001}

    subTags = {}

    for mainTopic in mainTags:
        frequentSubTags = frequentItemSet.getFrequentSet(mainTopic,mainTags,labels,supports.get(mainTopic))
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
    predicted = predictionManager.predict(textualTest,model,tfidf_transformer,count_vect)
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

    labels, tagDescriptions = csvManager.getLabelsAndTagDescriptions(descriptionsPath,tagsPath)
    csvManager.writeTagDescriptions2csv(tagDescriptions,basepath)
    csvManager.writeLabels2csv(labels,basepath)

#main()
#firstRun()

def predictSubTopicsOld(textualTest, mainTopic,labelsPath,tagDescriptionPath):
    #single usage version
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

    mainTags = ["action","adventure","platformer","rpg","simulation","strategy","sports"]
    blackList = ["indie","casual","early_access"]
    supports = {'action':0.015, 'adventure':0.013, 'platformer':0.0025, 'rpg':0.0075, 'simulation':0.007, 'strategy':0.0075, 'sports':0.001}


    frequentSubTags = frequentItemSet.getFrequentSet(mainTopic,mainTags,labels,supports.get(mainTopic))
    frequentSubTags.append(mainTopic)
    for black in blackList:
        if(black in frequentSubTags):
            frequentSubTags.remove(black)


    print(frequentSubTags)

    dictForTraining = {}
    for tag in tagDescriptions.keys():
        if(tag in frequentSubTags):
            dictForTraining[tag] = tagDescriptions.get(tag)

    print(len(dictForTraining))

    predictionManager.predict(dictForTraining, textualTest)