import random

OPCIONES = ("piedra", "papel", "tijera")

def resultado_ronda(usuario: str, pc: str) -> str:
    if usuario == pc:
        return "empate"
    elif (usuario == "piedra" and pc == "tijera") or \
         (usuario == "papel" and pc == "piedra") or \
         (usuario == "tijera" and pc == "papel"):
        return "gana_usuario"
    else:
        return "gana_pc"

def pedir_entero(mensaje: str, minimo: int = 1, maximo: int = 15) -> int:
    while True:
        try:
            n = int(input(mensaje))
            if minimo <= n <= maximo:
                return n
            else:
                print(f"Debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Ingresa un número entero válido.")

def main():
    while True:
        print("\n=== Menú ===")
        print("1) Jugar best-of-N")
        print("2) Salir")
        opcion = input("Elige: ").strip()

        if opcion == "2":
            print("Saliendo... ¡gracias por jugar!")
            break

        elif opcion == "1":
            n = pedir_entero("¿Cuántas rondas? (N impar, 1–15): ")
            if n % 2 == 0:
                print("N debe ser impar. Volviendo al menú…")
                continue

            vict_u = vict_pc = empates = 0
            rondas_ganar = (n // 2) + 1

            for ronda in range(1, n + 1):
                print(f"\n— Ronda {ronda} de {n} —")
                eleccion = input("Elige piedra/papel/tijera: ").lower().strip()

                if eleccion not in OPCIONES:
                    print("Entrada inválida. No cuenta la ronda.")
                    continue

                pc = random.choice(OPCIONES)
                print(f"Tú: {eleccion} | PC: {pc}")

                res = resultado_ronda(eleccion, pc)
                if res == "gana_usuario":
                    vict_u += 1
                    print("¡Punto para ti!")
                elif res == "gana_pc":
                    vict_pc += 1
                    print("Punto para la PC.")
                else:
                    empates += 1
                    print("Empate.")

                if vict_u >= rondas_ganar or vict_pc >= rondas_ganar:
                    print("La mayoría ya está decidida. Terminamos antes.")
                    break

            print("\n== Marcador final ==")
            print(f"Tú: {vict_u} | PC: {vict_pc} | Empates: {empates}")

            if vict_u > vict_pc:
                print("Ganaste el match 👏")
            elif vict_pc > vict_u:
                print("Perdiste el match 🤖")
            else:
                print("Match empatado.")

            if empates > 0:
                pass  # TODO: registrar empates en CSV más adelante

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
