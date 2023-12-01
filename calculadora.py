def get_user_input():
  try:
    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese otro numero: "))
    operation = input("Elija una operacion (+, -, *, /) o escriba 'exit' para salir: ")
    return num1, num2, operation
  except ValueError:
    print("Input invalido. Por favor ingrese numeros.")
    return get_user_input()

def ejecutar_operacion(user_input, operations):
  num1, num2, operation = user_input

  if operation in operations:
    result = operations[operation](num1, num2)
  else:
    result = "Operacion invalida"

  print("Resultado:", result)

def main():
  operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "No se puede dividir por cero"
  }

  while True:
    user_input = get_user_input()

    if user_input[2].lower() == 'exit':
        print("Salir.")
        break

    print("\nCalculando...")

    ejecutar_operacion(user_input, operations)

if __name__ == "__main__":
  main()

