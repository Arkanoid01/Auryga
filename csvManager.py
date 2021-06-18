import csv

def read(file):
    with open(file) as fp:
        reader = csv.reader(fp, delimiter=",", quotechar='"')

        lines = []

        for row in reader:
            lines.append(row)

        return lines

def write2csv(text,labels):

    with open("results.csv", 'w') as writer:
        csvWriter = csv.writer(writer, delimiter=',')
        for i in range(0, len(text)):
            data = [text[i].replace(",", "")]
            for label in labels[i]:
                data.append(label)
            csvWriter.writerow(data)

def getData():
    descriptions = read("Data/steam/steam_description_data.csv")
    #games = read("Data/steam/steam.csv")
    tags = read("Data/steam/steamspy_tag_data.csv")

    text = []
    labels = []

    tag_pos = []

    for tag in tags[0]:
        if(tag=="appid"):
            continue
        tag_pos.append(tag)

    counter = 0
    for description in descriptions:
        if(counter>len(descriptions)):
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

    return labels
    #return results

# print(text[0])
# print(labels[0])

