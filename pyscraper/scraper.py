import pyautogui
import pyperclip
from time import sleep
   
# Obtêm as coordenadas do campo desejado
class RPAMovement:
    def alert_user(self, message):
        print(f'{message}')
                
    def get_coordinates(self, name):
        self.alert_user('Warning: Você tem 3 segundos para marcar o ponto desejado...')
        sleep(3)
        x, y = pyautogui.position()
        self.alert_user(f'{name}: {x}, {y}.')
        self.alert_user('\n')
        return x, y

class Scraper:
    def __init__(self, quantity_products, wait_time):
        self.quantity_products = quantity_products
        self.wait_time = wait_time
        self.speed_mouse = 0.5
        self.output_file = 'output.txt'
        
        # Nomes dos campos
        NAMES =  ['skip_start', 'skip_up', 'skip_down', 'start_field', 'end_field']
        self.rpa_movement = RPAMovement()
        
        # Estrutura dos valores
        self.FIELD = {}
        
        # Coordenadas dos campos
        for name in NAMES:
            coordinates = self.rpa_movement.get_coordinates(name)
            self.FIELD[name] = coordinates
  
        # Armazena as coordenadas do campo e valores do produto na estrutura
        pyautogui.hotkey('ctrl', 'e')
        self.skipar('skip_start')
        
    # Move o mouse para os campos escolhidos
    def skipar(self, skip):
        sleep(self.wait_time)
        
        pyautogui.moveTo(self.FIELD[skip], duration=self.speed_mouse)
        sleep(self.wait_time)
        pyautogui.click()
        
    # Seleciona o texto dos campos
    def select_field(self, field):
        start_field, end_field = field
        sleep(self.wait_time)
        
        pyautogui.moveTo(self.FIELD[start_field], duration=self.speed_mouse)
        sleep(self.wait_time)
        pyautogui.dragTo(self.FIELD[end_field], button='left')
        
    # Salva o texto no arquivo de saída
    def save_text(self, copied_text):
        sleep(self.wait_time)
        
        with open(self.output_file, 'a') as file:
            file.write(copied_text + '\n')
        print(f'copied!: {copied_text}')
        
    # Copia e cola os textos no arquivo de saída
    def copy_and_paste(self, ):
        self.select_field([ 'start_field', 'end_field' ])
        pyautogui.hotkey('ctrl', 'c')
        
        copied_text = pyperclip.paste()
        self.save_text(copied_text)
        self.skipar('skip_up')
    
    def run(self):
        count = 0
        while True:
            self.copy_and_paste()
            count += 1
            if count == self.quantity_products:
                print('\n\n')
                print('Scraping finalizado!')
                break