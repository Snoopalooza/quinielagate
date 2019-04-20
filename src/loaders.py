import csv

def loadTeams():
    with open('../data/equiposLiga.csv') as csv_file:
        result = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        first = True
        for row in csv_reader:
            if first == True:
                first = False
            else:
                item = int(row[0])
                result.append(item)
                
        print('All teams loaded.')
        return result