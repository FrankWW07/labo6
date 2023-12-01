# Laboratorio 6
- Estudiante: Frank Wang Wu
- Carné: B57946
  
## Parte I
En este presente ítem del laboratorio se tendrá como motivo el manipular archivos usando métodos como el 'callback' para editar el código ''dataManager.py'' importando el archivo ''eventos.py'' para poder ingresar los datos y hacer que notifique los datos actualizados con los datos dadas generados en la función ''generate_real_time_date()''.

### 1. archivo ''evento.py''
Este archivo contiene la clase 'EventManager' que se encarga de manejar eventos y sus suscriptores.

### -- EventManager
### - ** `init (self)` **: 
El constructor inicializa con un diccionario 'subscribers' para mantener un registro de los eventos juntando sus respectivos suscriptores.
### - **subscribe (self, event, callback)**: 
Este método permite suscribir un callback a un evento. Si el evento no existe en el diccionario 'subscribers', se crea una entrada para el evento y se agrega el callback a la lista de suscriptores de ese evento.
### - **unsubscribe(self, event, callback)**: 
Permite anular la suscripción de un callback de un evento específico. Si el evento y el callback existen en el diccionario subscribers, se elimina el callback de la lista de suscriptores.
### - **notify(self, event, data=None)**:
Este método notifica a todos los suscriptores de un evento dado. Recorre la lista de suscriptores para ese evento y llama a cada callback, pasándole opcionalmente algunos datos.

### 2. archivo ''dataManager.py''
El archivo crea uns instancia, para poder suscribir esta función de callback al evento 'datos_actualizados' usando el 'EventManager' del 'RealTimeDataManager'. Luego, define una función de callback 'imprimir_datos_actualizados' para imprimir los datos actualizados de temperatura y humedad (en este caso).
