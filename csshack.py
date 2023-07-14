from pymem.process import *
from pymem import *
import keyboard
processo = pymem.Pymem('hl2.exe')
gameModule = module_from_name(processo.process_handle, 'client.dll').lpBaseOfDll
print('Digite "hack" para ver todos os hacks')


def text_with_line(text, linesnumber):
    print('-' * linesnumber)
    print(text)
    print('-' * linesnumber)



def red(text):
    text_red = f'\033[31m{text}\033[m'
    return text_red


while True:
    terminal = str(input('> '))
    if terminal == 'hack':
        text_with_line('|Wallhack|', 10)
        text_with_line('|Smoke   |', 10)
    elif terminal == 'Wallhack':
        print('Digite "ON" para ativar o Wallhack ou "OFF" para desligar o Wallhack.')
        wallhack_on_ou_off = str(input('Wallhack: '))
        if wallhack_on_ou_off == 'ON':
            processo.write_int(gameModule + 0x4C4BA0, 2)
        elif wallhack_on_ou_off == 'OFF':
            processo.write_int(gameModule + 0x4C4BA0, 1)
    elif terminal == 'Smoke':
        print('Digite "ON" para ativar o efeito da smoke ou "OFF" para delisgar o efeito da smoke.')
        efeitodasmoke_on_off = str(input('Smoke: '))
        if efeitodasmoke_on_off == 'ON':
            processo.write_int(gameModule + 0x4F7A40, 1)
        elif efeitodasmoke_on_off == 'OFF':
            processo.write_int(gameModule + 0x4F7A40, 0)
    elif terminal != 'Wallhack' and 'Smoke':
        print(red('Comando incorreto. Tente novamente.'))
    '''elif keyboard.is_pressed('v'):
        processo.write_int(gameModule + 0x4C4BA0, 2)
    elif keyboard.is_pressed('n'):
        processo.write_int(gameModule + 0x4C4BA0, 1)'''
