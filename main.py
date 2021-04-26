from selenium import webdriver
import time
import random


class cores:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print("Views" + cores.OKGREEN + " ON" + cores.ENDC)

times = int(input("Quantas views voce quer gerar?(Coloque inteiros) : "))

segundos = times * 35
minutos = segundos / 60
horas = minutos / 60

print(cores.OKBLUE + "Demorará, aproximadamente, {} segundos[{:.2f} minutos/{:.2f} horas] para processar as views, deixe o programa aberto.".format(segundos, minutos, horas) + cores.ENDC)

driver = webdriver.Chrome('chromedriver')

videos = [
    'https://www.youtube.com/watch?v=Tdrw6TYvkKs',
    'https://www.youtube.com/watch?v=AOHBksR1KDo',
    'https://www.youtube.com/watch?v=S-fbH141_po',
    'https://www.youtube.com/watch?v=_9sqzdnlTmc'
]

for i in range(times):
    print("Processando etapa {}.".format(i + 1))
    chose = random.randint(0, 2)
    if chose == 0:
        name = 'Giro'
    elif chose == 1:
        name = 'Air DK'
    elif chose == 2:
        name = 'Mj Tech'
    elif chose == 3:
        name = '1st Runes 99'
    sleep_time = random.randint(30, 35)
    print(cores.OKBLUE + "Atual: " + name + " / " + str(sleep_time) + cores.ENDC)
    driver.get(videos[chose])
    time.sleep(sleep_time)

print("Views finalizado -" + cores.FAIL + " OFF" + cores.ENDC)
print(cores.FAIL + "Made by Mjj Records" + cores.ENDC)
driver.quit()
