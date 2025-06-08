import requests

def responder_ollama(texto):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "mistral",  # cambia esto si estás usando otro modelo
        "prompt": texto,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        respuesta_json = response.json()
        return respuesta_json.get("response", "Lo siento, no pude generar una respuesta.")
    except Exception as e:
        return f"Error al conectar con Ollama: {e}"
