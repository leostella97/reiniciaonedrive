import os
import time
import getpass

# Obtém o nome de usuário do sistema
username = getpass.getuser()

# Define o caminho para o executável do OneDrive
onedrive_path = f"C:\\Users\\{username}\\AppData\\Local\\Microsoft\\OneDrive\\OneDrive.exe"

# Encerra o processo do OneDrive
os.system("TASKKILL /F /IM OneDrive.exe")

# Aguarda 10 segundos antes de abrir o OneDrive novamente
time.sleep(10)

# Abre o OneDrive novamente
os.startfile(onedrive_path)
