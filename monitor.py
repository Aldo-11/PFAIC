import os

def check_ransomware(directory):
    suspicious_ext = ['.crypted', '.locked', '.enc']
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in suspicious_ext):
                print(f"Alerta: Archivo sospechoso detectado: {file}")

check_ransomware('./data')