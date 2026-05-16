import time

def busqueda_secuencial(arreglo, objetivo):
    """Recorre el arreglo elemento por elemento."""
    for i in range(len(arreglo)):
        if arreglo[i] == objetivo:
            return i  # Retorna el índice si lo encuentra
    return -1  # Retorna -1 si no lo encuentra

def busqueda_binaria(arreglo, objetivo):
    """Divide el arreglo a la mitad en cada paso. Requiere datos ordenados."""
    bajo = 0
    alto = len(arreglo) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if arreglo[medio] == objetivo:
            return medio
        elif arreglo[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1

# 1. Crear el arreglo con 1,000,000 de elementos ordenados
limite_elementos = 1000000
arreglo_datos = list(range(1, limite_elementos + 1))

# 2. Solicitar la entrada del usuario
try:
    print(f"--- Buscador de Elementos (Rango: 1 a {limite_elementos}) ---")
    objetivo = int(input("Ingrese el número entero que desea buscar: "))
    
    # === EJECUCIÓN: BÚSQUEDA SECUENCIAL ===
    inicio_sec = time.perf_counter()
    pos_sec = busqueda_secuencial(arreglo_datos, objetivo)
    fin_sec = time.perf_counter()
    tiempo_sec = fin_sec - inicio_sec

    print("\n============================================")
    print("RESULTADO: BÚSQUEDA SECUENCIAL")
    print("============================================")
    if pos_sec != -1:
        print(f"Estado: Número ENCONTRADO")
        print(f"Posición (índice): {pos_sec}")
    else:
        print("Estado: Número NO ENCONTRADO")
    print(f"Tiempo de ejecución: {tiempo_sec:.8f} segundos")

    # === EJECUCIÓN: BÚSQUEDA BINARIA ===
    inicio_bin = time.perf_counter()
    pos_bin = busqueda_binaria(arreglo_datos, objetivo)
    fin_bin = time.perf_counter()
    tiempo_bin = fin_bin - inicio_bin

    print("\n56============================================")
    print("RESULTADO: BÚSQUEDA BINARIA")
    print("============================================")
    if pos_bin != -1:
        print(f"Estado: Número ENCONTRADO")
        print(f"Posición (índice): {pos_bin}")
    else:
        print("Estado: Número NO ENCONTRADO")
    print(f"Tiempo de ejecución: {tiempo_bin:.8f} segundos")
    
    print("\n============================================")

except ValueError:
    print("\n[Error] Por favor, ingrese únicamente números enteros.")
