import socket

objetivo = input("Ingresa la IP o dominio a escanear: ")
print(f"Escaneando {objetivo}...")

for puerto in range(1, 1025):  # Solo puertos comunes
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        resultado = s.connect_ex((objetivo, puerto))
        if resultado == 0:
            print(f"Puerto {puerto} está ABIERTO")
        s.close()
    except:
        pass
