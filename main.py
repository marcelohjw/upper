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


print(cores.FAIL + "========================================" + cores.ENDC + cores.OKGREEN + " UPPER " + cores.ENDC + cores.FAIL + "======================================================" + cores.ENDC)

times = int(input("Quantas" + cores.OKGREEN + " views" + cores.ENDC + " voce quer gerar?(Coloque inteiros) : "))

videosCombien = int(input("Quantos" + cores.FAIL + " videos" + cores.ENDC + " voce quer dar up?(Coloque inteiros) : "))

if videosCombien == 1:
    which_is = input("Copie e cole a seguir o video para dar um up: ")
    videosDic = {0: which_is}

    segundos = times * 35
    minutos = segundos / 60
    horas = minutos / 60

    print(cores.FAIL + "=====================================================================================================" + cores.ENDC)
    print("Views" + cores.OKGREEN + " ON" + cores.ENDC)

    print(
        cores.OKBLUE + "Demorará, aproximadamente, {} segundos[{:.2f} minutos/{:.2f} horas] para processar as views, deixe o programa aberto.".format(
            segundos, minutos, horas) + cores.ENDC)

    driver = webdriver.Chrome('chromedriver')
    for i in range(times):
        print("Processando etapa {}.".format(i + 1))
        chose = random.randint(0, len(videosDic))
        escolha = chose - 1
        sleep_time = random.randint(30, 40)
        print(cores.OKBLUE + str(sleep_time) + " segundos de aguardo.." + cores.ENDC)
        driver.get(videosDic[0])
        time.sleep(sleep_time)

    print("Views finalizado com sucesso -" + cores.FAIL + " OFF" + cores.ENDC)
    print(cores.FAIL + "Made by Mjj Records" + cores.ENDC)
    driver.quit()
else:
    i = 0
    segundos = times * 35
    minutos = segundos / 60
    horas = minutos / 60
    videosDic = {}
    while i < videosCombien:
        valorVideo = i + 1
        which_is = input("Copie e cole o video " + str(valorVideo) + " a seguir para dar um up: ")
        videosDic[i] = which_is
        i += 1
    print(
        cores.FAIL + "=====================================================================================================" + cores.ENDC)
    print("Views" + cores.OKGREEN + " ON" + cores.ENDC)

    print(
        cores.OKBLUE + "Demorará, aproximadamente, {} segundos[{:.2f} minutos/{:.2f} horas] para processar as views, deixe o programa aberto.".format(
            segundos, minutos, horas) + cores.ENDC)

    driver = webdriver.Chrome('chromedriver')
    for i in range(times):
        print("Processando etapa {}".format(i + 1) + " de " + str(times))
        maxValue = (len(videosDic) - 1)
        chose = random.randint(0, maxValue)
        sleep_time = random.randint(30, 40)
        print(cores.OKBLUE + str(sleep_time) + " segundos de aguardo.." + cores.ENDC)
        driver.get(videosDic[chose])
        time.sleep(sleep_time)

    print("Views " + cores.OKGREEN + "UPPER" + cores.ENDC + " finalizado com sucesso -" + cores.FAIL + " OFF" + cores.ENDC)
    print(cores.FAIL + "Made by Mjj Records" + cores.ENDC)
    driver.quit()
    final_question = input("Deseja repetir o mesmo processo? Sim(s)/Nao(n): ")
    if final_question == "s":
        run = 1
        while run == 1:
            i = 0
            segundos = times * 35
            minutos = segundos / 60
            horas = minutos / 60
            print(
                cores.FAIL + "=====================================================================================================" + cores.ENDC)
            print("Views" + cores.OKGREEN + " ON" + cores.ENDC)

            print(
                cores.OKBLUE + "Demorará, aproximadamente, {} segundos[{:.2f} minutos/{:.2f} horas] para processar as views, deixe o programa aberto.".format(
                    segundos, minutos, horas) + cores.ENDC)

            driver = webdriver.Chrome('chromedriver')
            for i in range(times):
                print("Processando etapa {}".format(i + 1) + " de " + str(times))
                maxValue = (len(videosDic) - 1)
                chose = random.randint(0, maxValue)
                sleep_time = random.randint(30, 35)
                print(cores.OKBLUE + str(sleep_time) + " segundos de aguardo.." + cores.ENDC)
                driver.get(videosDic[chose])
                time.sleep(sleep_time)

            print(
                "Views " + cores.OKGREEN + "UPPER" + cores.ENDC + " finalizado com sucesso -" + cores.FAIL + " OFF" + cores.ENDC)
            print(cores.FAIL + "Made by Mjj Records" + cores.ENDC)
            driver.quit()
            final_question = input("Deseja repetir o mesmo processo? Sim(s)/Nao(n): ")
            if final_question == "s":
                continue
            else:
                run = 0
                print(cores.FAIL + "Volte sempre!" + cores.ENDC)
                break
    else:
        driver.quit()
        print(cores.FAIL + "Volte sempre!" + cores.ENDC)