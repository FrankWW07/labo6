# Laboratorio 6
- Estudiante: Frank Wang Wu
- Carné: B57946
  
## Parte I
En este presente ítem del laboratorio se tendrá como motivo el manipular archivos usando métodos como el '`callback`' para editar el código ''`dataManager.py`'' importando el archivo ''`eventos.py`'' para poder ingresar los datos y hacer que notifique los datos actualizados con los datos dadas generados en la función ''`generate_real_time_date()`''.

### 1. archivo ''evento.py''
Este archivo contiene la clase '`EventManager`' que se encarga de manejar eventos y sus suscriptores.

### -- EventManager
### - `init (self)` : 
El constructor inicializa con un diccionario '`subscribers`' para mantener un registro de los eventos juntando sus respectivos suscriptores.
### - `subscribe (self, event, callback)` : 
Este método permite suscribir un callback a un evento. Si el evento no existe en el diccionario '`subscribers`', se crea una entrada para el evento y se agrega el callback a la lista de suscriptores de ese evento.
### - `unsubscribe(self, event, callback)` : 
Permite anular la suscripción de un callback de un evento específico. Si el evento y el callback existen en el diccionario subscribers, se elimina el callback de la lista de suscriptores.
### - `notify(self, event, data=None)` :
Este método notifica a todos los suscriptores de un evento dado. Recorre la lista de suscriptores para ese evento y llama a cada callback, pasándole opcionalmente algunos datos.

### 2. archivo ''dataManager.py''
El archivo crea uns instancia, para poder suscribir esta función de callback al evento '`datos_actualizados`' usando el '`EventManager`' del '`RealTimeDataManager`'. Luego, define una función de callback '`imprimir_datos_actualizados`' para imprimir los datos actualizados de temperatura y humedad (en este caso). Posteriormente, inicia un hilo para ejecutar '`start_real_time_updates`' en el segundo plano. Finalmente, para salirse del bucle se realizará una interrupción con el teclado en la función '`KeyboardInterrupt`' usando 'Ctrl + C' para detener las actualizaciones.

### -- paquetes importados
paquetes '`time`' (funcionalidad con el tiempo), '`random`' (generar números aleatorios), '`thereading`' (para trabajar con hilos así realizar operaciones en paralelo), '`EventManager`'  clase del archivo '`evento.py`'.

### -- clase '`RealTimeDataManager`'
### - `init (self)` 
Constructor que inicializa un diccionario `data` con datos iniciales de temperatura y humedad, así como la instancia de `EventManager`. También se usó un booleano `running` para controlar la ejecución del programa.

### - `start_real_time_updates(self)` :
Este método comienza un bucle que se ejecuta mientras `running` sea `True`. Cada 3 segundos, genera datos aleatorios de temperatura y humedad y notifica a los suscriptores del evento 'datos_actualizados' a través del `EventManager`.

### - `generate_real_time_data(self)` : 
Genera datos aleatorios de temperatura y humedad simulando actualizaciones en tiempo real.

### - `stop_updates(self)` : 
Cambia el estado de `running` a `False`, lo que detiene el bucle de actualización en tiempo real.

## Parte II
### archivo ''calculadora.py''

### -- funciones 
### - `get_user_input()` :
Esta función recopila la entrada del usuario para la calculadora. Solicita dos números y una operación matemática (`+`, `-`, `*`, `/`, o `exit`). Si el usuario ingresa valores que no son números, maneja la excepción y pide al usuario que ingrese valores válidos.

### - `ejecutar_operation (user_input, operation, operations)` :
Esta función realiza la operación matemática seleccionada por el usuario. Toma tres argumentos:

- `user_input`: una tupla con dos números y una operación.
- `operation`: la operación matemática seleccionada por el usuario.
- `operations`: un diccionario que contiene las operaciones matemáticas como funciones lambda (`+`, `-`, `*`, `/`) asociadas a sus respectivas operaciones.

### - `main()` :
La función principal ejecuta un bucle infinito que permite al usuario realizar operaciones matemáticas continuamente. Llama a `get_user_input()` para obtener la entrada del usuario y a `ejecutar_operacion()` para realizar la operación seleccionada. Si el usuario ingresa 'exit', el programa se detiene.
