import sys

def convertir_divisas(valor_clp, tasa_sol, tasa_ars, tasa_usd):

    divisas_convertidas = {
      "Soles": valor_clp * tasa_sol,
      "Pesos Argentinos": valor_clp * tasa_ars,
      "Dólares": valor_clp * tasa_usd,
    }
    return divisas_convertidas

def main():
    try:
      valor_clp = float(sys.argv[4])
      tasa_sol = float(sys.argv[1])
      tasa_ars = float(sys.argv[2])
      tasa_usd = float(sys.argv[3])
    except IndexError:
      print("Debe ingresar 4 argumentos en total.")
      return

    divisas_convertidas = convertir_divisas(valor_clp, tasa_sol, tasa_ars, tasa_usd)

    print(f"Los {valor_clp} pesos equivalen a:")
    for moneda, valor in divisas_convertidas.items():
      print(f"{valor:.1f} {moneda}")

if __name__ == "__main__":
    main()
