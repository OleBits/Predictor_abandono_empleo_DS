# pipeline.py
import os
import pickle
from sklearn.preprocessing import LabelEncoder

# Obtener la ruta del modelo relativa a la ubicación de pipeline.py
ruta_model = os.path.join(os.path.dirname(__file__), '../SRC/notebooks/model\RandomForestClassifier_1.pkl')

# Cargar el modelo previamente entrenado utilizando pickle
modelo = pickle.load(open(ruta_model, 'rb'))
from sklearn.preprocessing import LabelEncoder

# ... Código para cargar el modelo previamente entrenado ...

# Lista de características categóricas
categorias = ['gender', 'relevent_experience', 'enrolled_university', 'education_level', 'major_discipline']

# Inicializar el LabelEncoder
label_encoder = LabelEncoder()

def predecir(datos):
    # Preprocesamiento de datos categóricos
    datos_categoricos = [datos[c] for c in categorias]
    datos_categoricos_codificados = label_encoder.fit_transform(datos_categoricos)

    # Preprocesamiento de datos numéricos
    city_development_index = datos['city_development_index']
    experiencia = datos['experiencia']

    # Concatenar todas las características para la predicción
    datos_preprocesados = [city_development_index] + list(datos_categoricos_codificados) + [experiencia]

    # Realizar la predicción utilizando el modelo cargado previamente
    resultado_prediccion = modelo.predict([datos_preprocesados])

    # Retornar el resultado de la predicción
    return resultado_prediccion[0]
