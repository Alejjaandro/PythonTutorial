import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import webbrowser
import datetime
import wikipedia
from cartera_acciones import cartera

# ========== Transformación de texto a voz ==========
def hablar(texto):
    # Inicialización del motor de voz
    motor = pyttsx3.init()
    motor.say(texto)
    motor.runAndWait()

# ========== Transformación de voz a texto ==========
def transformar_voz_en_texto():
    reconocedor = sr.Recognizer()
    
    # Configuración del micrófono
    with sr.Microphone() as origen:
    
        reconocedor.pause_threshold = 1
        print("Escuchando...")
        
        audio = reconocedor.listen(origen)
        
        # Reconocimiento de voz
        try:
            print("Reconociendo...")
            consulta = reconocedor.recognize_google(audio, language='es-ES')
            print(f"Usuario: {consulta}")
            return consulta
            
        except sr.UnknownValueError:
            print("No se ha podido reconocer la voz")
            hablar("No he entendido lo que has dicho, inténtalo de nuevo")
            return "Vuélvelo a intentar"
        
        except sr.RequestError:
            print("Error en la conexión")
            hablar("Error en la conexión")
            return "Vuélvelo a intentar"
        
        except:
            print("Error desconocido")
            hablar("Error desconocido")
            return "Vuélvelo a intentar"
        
# ========== Funcionalidades ==========
def saludo():
    hablar("Hola, ¿en qué puedo ayudarte?")
    
def pedir_dia(): 
    dia = datetime.date.today()
    dia_semana = dia.weekday()
    
    calendario = {0: 'Lunes', 
                  1: 'Martes', 
                  2: 'Miércoles', 
                  3: 'Jueves', 
                  4: 'Viernes', 
                  5: 'Sábado', 
                  6: 'Domingo'}
    
    hablar(f"Hoy es {calendario[dia_semana]}")

def pedir_hora():
    hora = datetime.datetime.now()
    hora = f"{hora.hour}:{hora.minute}"
    
    hablar(f"Son las {hora}")
    
def pedir_precio_accion(accion):
    try: 
        # Buscamos el primer ticker que contenga el nombre de la accion
        coincidencias = [key for key in cartera.keys() if accion in key]
        if len(coincidencias) == 0:
            hablar("No se ha podido encontrar la acción, inténtalo de nuevo")
            return
        
        # Obtenemos el precio de la accion
        accion = coincidencias[0]
        ticker = cartera[accion]
        # Obtenemos el precio de la accion
        accion = yf.Ticker(ticker)
        precio = accion.history(period='1d')['Close'][0]
        return round(precio, 2)
    except:
        hablar("No se ha podido encontrar la acción, inténtalo de nuevo")

def pedir_cosas():
    saludo()
    
    terminar = False
    while not terminar:
        pedido = transformar_voz_en_texto().lower()
        
        if 'youtube' in pedido:
            hablar("¿Qué quieres buscar en YouTube?")
            busqueda = transformar_voz_en_texto()
            pywhatkit.playonyt(busqueda)
            continue
        
        elif 'abrir google' in pedido:
            hablar("Abriendo Google")
            webbrowser.open('https://www.google.com')
            continue
        
        elif "día es hoy" in pedido:
            pedir_dia()
            continue
        
        elif "qué hora es" in pedido:
            pedir_hora()
            continue
        
        elif "busca en wikipedia" in pedido:
            hablar("Buscando en Wikipedia")
            
            # Eliminar la primera frase de la búsqueda
            pedido = pedido.replace("busca en wikipedia", "")
            print(pedido)
            wikipedia.set_lang("es")
            
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("Según Wikipedia")
            hablar(resultado)
            continue
        
        elif "busca en internet" in pedido:
            hablar("Buscando en Google")
            pedido = pedido.replace("busca en internet", "")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue
        
        elif 'precio de las acciones' in pedido:
            # Extraer el nombre de la accion de la consulta
            accion = pedido.split('precio de las acciones de ')[1].lower()
            # Obtener el precio de la accion
            precio = pedir_precio_accion(accion)
            if not precio:
                continue
            
            hablar(f"El precio de las acciones de {accion} es de {precio} dólares")
            continue
               
        elif 'eso es todo' in pedido:
            hablar("Me piro, vampiro")
            break


pedir_cosas()