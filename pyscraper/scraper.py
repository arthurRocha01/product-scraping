import pyautogui
import pyperclip
from time import sleep
   
class RPAMovement:
    def alert_user(self, message):
        print(f'{message}')
                
    def get_coordinates(self, name):
        self.alert_user('Warning: Você tem 3 segundos para marcar o ponto desejado...',)
        sleep(3)
        x, y = pyautogui.position()
        self.alert_user(f'{name}: {x}, {y}.')
        return x, y

class Scraper:
    def __init__(self, quantity_products, wait_time):
        self.quantity_products = quantity_products
        self.wait_time = wait_time
        
        self.rpa_movement = RPAMovement()
        NAMES =  ['skip_start', 'skip_up', 'skip_down', 'name_field']
        self.FIELD = {}
        for name in NAMES:
            coordinates = self.rpa_movement.get_coordinates(name)
            self.FIELD[name] = coordinates
  
        # Prepara o ambiente
        pyautogui.hotkey('ctrl', 'e')
        self.skipar('skip_start')
        
    def skipar(self, skip):
        pyautogui.moveTo(self.FIELD[skip])
        sleep(self.wait_time)
        pyautogui.click()
        
    def move_to_field(self, field):
        pyautogui.moveTo(self.FIELD[field])
        sleep(self.wait_time)
        pyautogui.click(clicks=2)
        sleep(self.wait_time)
        
    def save_text(self, copied_text):
        with open('output.txt', 'w') as file:
            file.write(copied_text + '\n')
        print(f'copied!: {copied_text}')
        print('*****--*****--*****-*****--*****--*****--*****--*****\n\n')
        
    def copy_and_paste(self, ):
        self.move_to_field('name_field')
        pyautogui.hotkey('ctrl', 'c')
        sleep(self.wait_time)
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