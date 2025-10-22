# app.py - Aplicación Flask completa
# Sistema de Seguimiento de Estudiantes en Riesgo

from flask import Flask, render_template

app = Flask(__name__)

# Función para calcular nivel de riesgo
def calcular_riesgo(promedio, ausentismo):
    if promedio < 60 or ausentismo > 10:
        return "ALTO"
    elif promedio < 75 or ausentismo > 5:
        return "MEDIO"
    else:
        return "BAJO"

# Base de datos de estudiantes
estudiantes = [
    {"id": 1, "nombre": "María José García López", "grado": "5to Primaria", 
     "promedio": 85, "ausentismo": 3},
    {"id": 2, "nombre": "Carlos Andrés Pérez Hernández", "grado": "6to Primaria", 
     "promedio": 55, "ausentismo": 12},
    {"id": 3, "nombre": "Ana Lucía Martínez Rodríguez", "grado": "4to Primaria", 
     "promedio": 92, "ausentismo": 1},
    {"id": 4, "nombre": "José Luis Ramírez Santos", "grado": "5to Primaria", 
     "promedio": 68, "ausentismo": 8},
    {"id": 5, "nombre": "Sofía Isabel González Morales", "grado": "6to Primaria", 
     "promedio": 78, "ausentismo": 4},
    {"id": 6, "nombre": "Diego Fernando López Castro", "grado": "4to Primaria", 
     "promedio": 58, "ausentismo": 6}
]

# Calcular nivel de riesgo para cada estudiante
for est in estudiantes:
    est['nivel_riesgo'] = calcular_riesgo(est['promedio'], est['ausentismo'])

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/estudiantes')
def lista_estudiantes():
    return render_template("estudiantes.html", estudiantes=estudiantes)

@app.route('/estudiante/<int:id>')
def detalle(id):
    # Buscar estudiante por ID
    estudiante = next((e for e in estudiantes if e['id'] == id), None)
    if not estudiante:
        return "Estudiante no encontrado", 404
   
    return render_template("detalle.html", estudiante=estudiante)

@app.route('/estadistica')
def estadisticas():
    # Calcular estadísticas
    total = len(estudiantes)
    promedio_general = sum(e['promedio'] for e in estudiantes) / total
    
    riesgo_alto = sum(1 for e in estudiantes if e['nivel_riesgo'] == 'ALTO')
    riesgo_medio = sum(1 for e in estudiantes if e['nivel_riesgo'] == 'MEDIO')
    riesgo_bajo = sum(1 for e in estudiantes if e['nivel_riesgo'] == 'BAJO')
    
    return render_template("estadistica.html", total=total, 
                           promedio_general=promedio_general,  
                            riesgo_alto=riesgo_alto,
                            riesgo_medio=riesgo_medio,
                            riesgo_bajo=riesgo_bajo)

if __name__ == '__main__':
    print("🚀 Iniciando servidor Flask...")
    print("📱 Abre tu navegador en: http://127.0.0.1:5000")
    app.run(debug=True)