# 🤖 MarkyBot Desktop

MarkyBot Desktop es un asistente virtual inteligente que funciona desde tu PC. Utiliza voz, cámara y una IA local para conversar contigo, detectar emociones y reconocerte visualmente. Ideal para interacción sin conexión.

---

## 🧠 Características principales

- 🧍‍♂️ Reconocimiento facial con cámara (usando `face_recognition`)
- 🗣️ Comunicación por voz (entrada y salida)
- 💬 Alternativa por teclado (modo texto)
- 📁 Memoria persistente de conversaciones
- 😃 Detección de emociones en tus mensajes
- 🧠 Conexión a IA local vía [Ollama](https://ollama.com) (ej. LLaMA3, DeepSeek, Mistral)

---

## 📦 Requisitos

### Python:
- Python 3.11 o superior

### Dependencias:
Instala las dependencias desde `requirements.txt` (a crear):

```bash
pip install -r requirements.txt

Para módulos de voz:
pip install pipwin
pipwin install pyaudio


Para reconocimiento facial:
pip install opencv-python dlib-bin face_recognition

⚙️ Estructura del proyecto
MarkyBot-Desktop/
├── bot.py                    # Archivo principal del bot
├── modulos/
│   ├── ia.py                 # Conexión a IA local
│   ├── voz.py                # Hablar y escuchar
│   ├── rostro.py             # Reconocimiento facial
│   ├── emociones.py          # Detección de emociones
│   ├── memoria.py            # Manejo de historial
│   └── usuario.py            # Carga y guarda nombre del usuario
├── datos/
│   ├── usuario.txt
│   ├── modo.txt
│   ├── memoria_conversaciones.json
│   ├── logs/
│   └── rostros/

▶️ ¿Cómo ejecutar?
Asegúrate de que tu servidor Flask de IA esté corriendo (ej: ollama_api.py con Ollama):
ollama run mistral
python ollama_api.py


Luego ejecuta el bot desde consola:
python bot.py

Usa comandos:

modo → cambiar entre voz/teclado

rostro → registrar o reconocer rostro

salir → salir del programa


🧠 Notas adicionales
No requiere conexión a internet si usas IA local

Guarda tu historial de conversación y emociones

Reconoce al usuario por nombre o rostro

Perfecto para pruebas locales de asistentes virtuales


✨ Créditos
Desarrollado por: [MarkMC-byte]
Asistencia técnica: ChatGPT
IA Local: Ollama + modelos como Mistral o LLaMA
Reconocimiento facial: face_recognition
Reconocimiento de voz: speech_recognition + pyttsx3
