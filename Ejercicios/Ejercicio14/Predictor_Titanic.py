from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn import tree

# Cargamos el dataset
ruta_csv = Path(__file__).resolve().parents[0] / "DataSet_Titanic.csv"

df = pd.read_csv(ruta_csv)

# Guardamos los atributos predictores (todas las etiquetas excepto "Sobreviviente")
datos_predictores = df.drop("Sobreviviente", axis=1)
# Y la etiqueta a predecir ("Sobreviviente")
dato_a_predecir = df["Sobreviviente"]

# Creamos un arbol de decision: cuanto mas profundo sea, mas precision obtendrá
arbol = DecisionTreeClassifier(max_depth=2, random_state=42)
# Entrenamos a la máquina
arbol.fit(datos_predictores, dato_a_predecir)
# Predecimos sobre nuestro set
prediccion = arbol.predict(datos_predictores)

# Comaparamos con las etiquetas reales
print(f"Exactitud: {round(accuracy_score(dato_a_predecir, prediccion)*100, 2)}%")

# Creamos una matriz de confusión
confusion_matrix(dato_a_predecir, prediccion)
# Creamos un gráfico para la matriz de confusión
ConfusionMatrixDisplay.from_estimator(arbol, datos_predictores, dato_a_predecir, cmap=plt.cm.Blues, values_format='.2f')
plt.show()
# Creamos un gráfico para la matriz de confusión normalizada
ConfusionMatrixDisplay.from_estimator(arbol, datos_predictores, dato_a_predecir, cmap=plt.cm.Blues, values_format='.2f', normalize="true")
plt.show()

# Mostramos un árbol gráficamente
plt.figure(figsize=(10,8))
tree.plot_tree(arbol, filled=True, feature_names=datos_predictores.columns)
plt.show()

# Hacemos un grafico con la importancia de las variables
# Creamos las variables x (importancias) e y (columnas)
importancias = arbol.feature_importances_
columnas = datos_predictores.columns
# Creamos el gráfico
sns.barplot(x=columnas, y=importancias)
plt.title("Importancia de las variables")
plt.show()