from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import pyautogui
import time
import urllib

#função para pesquisar se tem vaga até retornar uma vaga
def achar_vaga():

    #entrar no corridas e caminhadas
    navegador.get("https://associado.appai.org.br/caminhadas-e-corridas")

    #esperar carregar a pagina
    while len(navegador.find_elements(By.ID, 'inscrever')) < 1:
        time.sleep (1)

    #clicar no vizualizar agendas 5 vezes
    pyautogui.click(1410,951,duration=0.1)
    pyautogui.click(1410,896,duration=0.1)
    pyautogui.click(1410,842,duration=0.1)
    pyautogui.click(1410,791,duration=0.1)
    pyautogui.click(1410,736,duration=0.1)

    #define o texto que precisa ser encontrado
    vaga = "Inscrição Aberta"
    #vaga = "Inscrições Encerradas"

    #resultado da busca:
    if vaga in navegador.page_source:
        
        #avisa no terminal
        print("Achei uma vaga estou enviando um aviso no Whatsapp!")

        #abre o wpp ja enviando a msg
        navegador.get(f'https://web.whatsapp.com/send?phone{telefone}&text={texto}')
        while len(navegador.find_elements(By.ID, 'side')) < 1:
            time.sleep (1)

        #espera carregar o menu
        time.sleep(1)
        #localiza e escreve o telefone na busca
        navegador.find_element('xpath' , '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(telefone)
        #seleciona o contato e clica pra abrir a conversa
        pyautogui.click(907,372,duration=0.5)
        pyautogui.click(1146,966,duration=0.5)
        time.sleep(1)

        #clicar em enviar
        pyautogui.click(1719,1000,duration=0.5)
        time.sleep (10)

        #repetir a função
        achar_vaga()


    #repete a função se nao achar
    else:
       achar_vaga()

#pedindo os inputs de login
print('Vamos começar o passo a passo!')
mensagem = "Achei uma vaga! Corre pra se inscrever!"
texto = urllib.parse.quote(mensagem)
telefone = input('Digite o número do whatsapp (NÃO PODE SER O SEU) para receber o aviso (nesse formato: 5521999999999): ')
matricula = input("Digite sua matricula APPAI (nesse formato: 00000000-00): ")
senha = input("Digite sua senha: ")
input('Dados coletados, vou abrir uma janela do chrome para você escanear o QR code do Whatsapp, em seguida farei login no portal da appai e começarei a busca pela vaga em qualquer corrida disponível e caso encontre te mandarei mensagem no número que me informou! Aperte enter para iniciar!')

#limpando a tela
os.system('cls')

#baixar o webdriver e criar o navegador
service = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=service)

#fechando a msg e maximizando a janela
pyautogui.click(922,116,duration=0.1)
pyautogui.click(875,25,duration=0.1)

#pedindo ao usuario para aguardar
print('Estou buscando uma vaga na corrida, por favor aguarde.')
print('Quando encontrar vou avisar!')
print('Para interromper a busca feche o navegador e o terminal!')

#entrar no wpp
navegador.get('https://web.whatsapp.com/')
#aguardando login no wpp
while len(navegador.find_elements(By.ID, 'side')) < 1:
    time.sleep (1)


#entrar no portal
navegador.get("https://segurancaapi.appai.org.br/Account/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3DClient_ID_PA%26redirect_uri%3Dhttps%253A%252F%252Fassociado.appai.org.br%252Fcallback%26response_type%3Did_token%2520token%26scope%3Dopenid%2520roles%2520email%2520profile%26state%3Da84ded8be1b4462eb4f62f5d906ff84c%26nonce%3Dbadfb2aa72c54b53b6169900da0b8584")
#inserir matricula
navegador.find_element('xpath' , '//*[@id="UserName"]').send_keys(matricula)
#inserir senha
navegador.find_element('xpath' , '//*[@id="password-field"]').send_keys(senha)
#clicar em acessar
navegador.find_element('xpath' , '//*[@id="btnLogin"]').click()

while len(navegador.find_elements(By.ID, 'menuBeneficios')) < 1:
    time.sleep (1)

#iniciar função de achar a vaga
achar_vaga()


#finalizar com o enter
input("pressione enter para finalizar...")