import sys

def contar_caracteres(ruta_texto):
  try:
    with open(ruta_texto, "r") as archivo:
      texto = archivo.read()
  except FileNotFoundError:
    print(f"archivo texto no encontrado.")
    return

  caracteres_distintos = set(texto.lower())

  palabras = texto.split()
  palabras_distintas = set(palabras)

  return {
    "caracteres_distintos": len(caracteres_distintos),
    "palabras_distintas": len(palabras_distintas),
  }

def main():
  if len(sys.argv) != 2:
    print("ruta del archivo de texto no encontrado")
    return

  ruta_texto = sys.argv[1]

  resultados = contar_caracteres(ruta_texto)

  print(f"El número de caracteres distintos: {resultados['caracteres_distintos']}")
  print(f"El número de palabras distintas es: {resultados['palabras_distintas']}")

if __name__ == "__main__":
  main()
