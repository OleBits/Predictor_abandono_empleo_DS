from flask import Flask, render_template, request
from pipelines import predecir

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Obtener los datos enviados desde el formulario
        city_development_index = float(request.form['city_development_index'])
        gender = request.form['gender']
        relevent_experience = request.form['relevent_experience']
        enrolled_university = request.form['enrolled_university']
        education_level = request.form['education_level']
        major_discipline = request.form['major_discipline']
        experiencia = float(request.form['experience'])
        company_size = request.form['company_size']
        company_type = request.form['company_type']
        last_new_job = float(request.form['last_new_job'])
        training_hours = int(request.form['training_hours'])

        # Procesar los datos y prepararlos para la predicción
        datos = {
            #'city': None,
            #'order_size': None,
            'city_development_index': city_development_index,
            'gender': gender,
            'relevent_experience': relevent_experience,
            'enrolled_university': enrolled_university,
            'education_level': education_level,
            'major_discipline': major_discipline,
            'experiencia': experiencia,
            #'company_size': company_size,
            #'company_type': company_type,
            #'last_new_job': last_new_job,
            #'training_hours': training_hours
        }

        # Realizar la predicción
        resultado_prediccion = predecir(datos)

        # Pasar el resultado de la predicción a la plantilla resultado.html
        return render_template('resultado.html', resultado=resultado_prediccion)

if __name__ == '__main__':
    app.run(debug=True)
