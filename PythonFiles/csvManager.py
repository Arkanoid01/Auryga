import csv

def read(file):
    with open(file) as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')

        lines = []

        for row in reader:
            lines.append(row)

        return lines

def writeTagDescriptions2csv(tagDescriptions,path):

    with open(path+"/tagDescriptions.csv", 'w') as writer:
        csvWriter = csv.writer(writer, delimiter=',')
        for tag in tagDescriptions.keys():
            data = []
            data.append(tag)
            for elem in tagDescriptions.get(tag):
                data.append(elem)
            csvWriter.writerow(data)

def writeLabels2csv(labels,path):
    with open(path+"/labels.csv", 'w') as writer:
        csvWriter = csv.writer(writer, delimiter=',')
        for label in labels:
            csvWriter.writerow(label)

def readFromCsv(path):
    csv_file = open(path)
    csv_reader = csv.reader(csv_file, delimiter=',')
    results = []
    for row in csv_reader:
        results.append(row)

    return results

def getLabelsAndTagDescriptions(pathDescription,pathTags):
    descriptions = read(pathDescription)
    #games = read("Data/steam/steam.csv")
    tags = read(pathTags)

    text = []
    labels = []

    tag_pos = [] #contiene la lista di tutti i tag che ci sono

    for tag in tags[0]:
        if(tag=="appid"):
            continue
        tag_pos.append(tag)

    counter = 0
    for description in descriptions:
        if(counter>len(descriptions)):
        #if(counter>100):
            break
        for gameTags in tags:
            if(description[0]==gameTags[0]):
                pos=0
                localLabels = []
                for singleTag in gameTags[1:]:
                    if(int(singleTag)>0):
                        localLabels.append(tag_pos[pos])
                        pos+=1
                    else:
                        pos+=1
                text.append(description[3])
                labels.append(localLabels)
        counter+=1

    results = {}

    for i in range(0,len(text)):
        for label in labels[i]:
            internalTag = results.get(label)
            if not isinstance(internalTag, list):
                l = []
                l.append(text[i])
                results[label] = l
            else:
                internalTag.append(text[i])
                results[label] = internalTag


    return labels, results
