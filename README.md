# Laboratorio 6
- Estudiante: Frank Wang Wu
- Carné: B57946
  
## Parte I
En este presente ítem del laboratorio se tendrá como motivo el manipular archivos usando métodos como el 'callback' para editar el código ''dataManager.py'' importando el archivo ''eventos.py'' para poder ingresar los datos y hacer que notifique los datos actualizados con los datos dadas generados en la función ''generate_real_time_date()''.

### 1. archivo ''evento.py''
Este archivo contiene la clase 'EventManager' que se encarga de manejar eventos y sus suscriptores.

### - EventManager:
- **init (self)**: El constructor inicializa con un diccionario 'subscribers' para mantener un registro de los eventos juntando sus respectivos suscriptores.
- **subscribe (self, event, callback)**: Este método permite suscribir un callback a un evento. Si el evento no existe en el diccionario 'subscribers', se crea una entrada para el evento y se agrega el callback a la lista de suscriptores de ese evento.
