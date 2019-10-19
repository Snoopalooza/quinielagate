import pandas as pd
from sklearn import tree
from loaders import loadTeams
from loaders import loadFeatures
from loaders import loadTarget
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

# Load features carga todos los resultados de los partidos
# en formato [ID local, ID visitante, resultado (1, 0, -1)]


pima = pd.read_csv("../data/jornadasLiga.csv", header=0)
col_names = ['ID Local', 'ID Visitante', 'Gol Local', 'Gol Visitante', 'Num Partido']
X = pima[col_names]
y = pima.Resultado

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

classif = tree.DecisionTreeClassifier()
# Mezclamos y agitamos todo
classif.fit(X_train, y_train)

#predecimos
y_pred = classif.predict(X_test)

print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))

