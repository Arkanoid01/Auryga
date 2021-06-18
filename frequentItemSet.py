import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import csvManager

def main():

    labels = csvManager.getData()
    #print(len(labels))

    pd.set_option('display.max_rows', None)
    te = TransactionEncoder()
    te_ary = te.fit(labels).transform(labels)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    results = apriori(df, min_support=0.02,use_colnames=True)

    print(len(results))

    adventure = []
    action = []
    simulation = []
    rpg = []
    strategy = []
    sports = []
    puzzle = []

    for elem in set(results['itemsets']):
        if('adventure' in list(elem)):
            adventure.append(elem)
        if('action' in list(elem)):
            action.append(elem)
        if('simulation' in list(elem)):
            simulation.append(elem)
        if('rpg' in list(elem)):
            rpg.append(elem)
        if('strategy' in list(elem)):
            strategy.append(elem)
        if('sports' in list(elem)):
            sports.append(elem)
        if('puzzle' in list(elem)):
            puzzle.append(elem)



    print("adventure: "+str(len(adventure)))
    print("action: "+str(len(action)))
    print("simulation: " + str(len(simulation)))
    print("rpg: " + str(len(rpg)))
    print("strategy: " + str(len(strategy)))
    print("sport: " + str(len(sports)))
    print("puzzle: " + str(len(puzzle)))


    polishedAction = []
    for elems in action:
        for elem in list(elems):
            if(not elem in polishedAction):
                polishedAction.append(elem)

    print(polishedAction)

main()