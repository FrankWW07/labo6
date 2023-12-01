import time
import random
import threading
from eventos import EventManager # Importamos la clase EventManager del archivo eventos.py

class RealTimeDataManager:
  def __init__(self):
    self.data = {"temperatura": 25.0, "humedad": 60.0}
    self.event_manager = EventManager()
    # variable para controlar la ejecución del programa
    self.running = True

  def start_real_time_updates(self):
    while self.running:
      # el bucle se ejecutará mientras running sea True
      time.sleep(3)
      self.generate_real_time_data()
      # Notificar al EventManager que los datos han cambiado
      self.event_manager.notify('datos_actualizados', self.data)

  def generate_real_time_data(self):
      self.data["temperatura"] += random.uniform(-1.0, 1.0)
      self.data["humedad"] += random.uniform(-2.0, 2.0)

  def stop_updates(self):
    # cambia el estado de running para detener el bucle
    self.running = False


# Creamos una instancia de RealTimeDataManager
real_time_data_manager = RealTimeDataManager()

# Función de callback para imprimir los datos actualizados
def imprimir_datos_actualizados(data):
 print("Datos en tiempo real actualizados:")
 print("{"f"'Temperatura' (°C): {data['temperatura']}, 'Humedad' (%): {data['humedad']}"+"}")
 print("-----------")

# Suscribimos el callback al EventManager para el evento 'datos_actualizados'
real_time_data_manager.event_manager.subscribe('datos_actualizados', imprimir_datos_actualizados)

# Actualizaciones en tiempo real en segundo plano
update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
update_thread.start()

try:
  while True:
    time.sleep(1)
except KeyboardInterrupt:
  # llama a la función para detener las actualizaciones
  real_time_data_manager.stop_updates()
  print("\nPrograma terminado.")
