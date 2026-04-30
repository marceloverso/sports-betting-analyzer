import os
import gspread
import requests
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env (solo local)
load_dotenv()

# CONFIGURACIÓN DE SECRETOS
API_KEY = os.getenv('SPORTS_API_KEY')
SHEET_ID = os.getenv('GOOGLE_SHEET_ID')
# La ruta al JSON también puede ser una variable de entorno
GOOGLE_CREDS_PATH = os.getenv('GOOGLE_CREDS_PATH')

def conectar_hoja():
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_file(GOOGLE_CREDS_PATH, scopes=scope)
    client = gspread.authorize(creds)
    return client.open_by_key(SHEET_ID).worksheet("Datos")

def obtener_resultado_real(deporte, local, visitante):
    """
    Aquí conectarías con tu API (The Odds API, etc.)
    Usando la variable API_KEY
    """
    url = f"https://api.the-odds-api.com/v4/sports/{deporte}/scores/?apiKey={API_KEY}"
    r = requests.get(url)
    return "Pendiente" # Simulación

def ejecutar_actualizacion():
    try:
        sheet = conectar_hoja()
        registros = sheet.get_all_records()
        
        for i, fila in enumerate(registros, start=2):
            if fila['Estado (Ganada/Perdida)'] == 'Pendiente':
                # Lógica de verificación
                print(f"Verificando: {fila['Local']} vs {fila['Visitante']}")
                # resultado = obtener_resultado_real(...)
                # sheet.update_cell(i, 8, "Ganada") # Ejemplo
                
    except Exception as e:
        print(f"Error en la ejecución: {e}")

if __name__ == "__main__":
    ejecutar_actualizacion()
