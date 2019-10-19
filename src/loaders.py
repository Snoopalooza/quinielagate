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

def loadFeatures():
    with open('../data/jornadasLiga.csv') as csv_file:
        result = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        first = True
        for row in csv_reader:
            if first == True:
                first = False
            else:
                item = [int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5])]
                result.append(item)
        print('All results loaded')
        return result

def loadTarget():
    with open('../data/jornadasLiga.csv') as csv_file:
        result = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        first = True
        for row in csv_reader:
            if first == True:
                first = False
            else:
                result.append(int(row[6]))
        print('All results loaded')
        return result
