from selenium import webdriver
from colorama import init, Fore, Style
import time
import os
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Discord Token Loader by OTEMA")

# limpia la consola
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("test")

# Inicializar colorama
init()

def animate_text(text):
    for char in text:
        # Cambia el color de la letra
        print(Fore.RED + char, end='', flush=True)
        time.sleep(0.1)

    # Resetea el color de la letra
    print(Style.RESET_ALL)
clear()
animate_text("This loader has been created by otema")
time.sleep(2)
clear()

# Configuramos el navegador
options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--profile-directory=Default')
options.add_argument("--disable-plugins-discovery")
options.add_argument("--start-maximized")
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)

# Abrimos la página de Discord
driver.get("https://discord.com/login")

# Esperamos a que la página cargue completamente
driver.implicitly_wait(10)

# Pedimos el token al usuario
Style.RESET_ALL
print(Fore.GREEN + "Introduce tu token de Discord: ")
Style.RESET_ALL
token = input()

# Ejecutamos el código JavaScript para iniciar sesión
script = f'''
function login(token) {{
  setInterval(() => {{
    document.body.appendChild(document.createElement('iframe')).contentWindow.localStorage.token = `"${{token}}"`
  }}, 50);
  setTimeout(() => {{
    location.reload();
  }}, 2500);
}}

login('{token}')
'''
driver.execute_script(script)
clear()
print(Fore.BLUE + 'TOKEN SUCCESSFULLY INJECTED')
print(Fore.BLUE + 'Discord: otema#0746')
# Mantenemos la sesión abierta hasta que el usuario la cierre
print(Fore.RED + "Presiona ENTER para cerrar la sesión")
input()

# Cerramos el navegador
driver.quit()
