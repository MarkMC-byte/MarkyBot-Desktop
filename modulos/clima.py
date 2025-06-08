import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def obtener_clima(ciudad):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&lang=es&units=metric"
    
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()

        if respuesta.status_code == 200:
            temp = datos['main']['temp']
            clima = datos['weather'][0]['description']
            nombre_ciudad = datos['name']
            pais = datos['sys']['country']
            return f"🌤️ El clima en {nombre_ciudad}, {pais} es: {clima} con una temperatura de {temp}°C."
        elif datos.get("message"):
            return f"⚠️ Ciudad no encontrada: {ciudad}"
        else:
            return "⚠️ No se pudo obtener el clima en este momento."
    
    except Exception as e:
        return f"❌ Error al consultar el clima: {e}"
