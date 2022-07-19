import random
import PySimpleGUI as sg


class GeradorSenha:
    def __init__(self):
        # Layout
        sg.theme('Topanga')
        layout = [
            [sg.Text('Gerador de senha segura!')],
            [sg.Text('Quantidade de caracteres', size=(20, 1)),
             sg.Input(key='total_caracteres', size=(20, 1))],
            [sg.Output(size=(43, 5))],
            [sg.Button('Gerar Senha')],
        ]
        # janela
        self.janela = sg.Window('Gerador de Senha', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)

    def gerar_senha(self, valores):
        char_list = '!#$%&"()*+,-./:;<=>?@[]^_`{|}~abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        chars = random.choices(char_list, k=int(valores['total_caracteres']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"nova_senha: {nova_senha}\n")

        print('Arquivo salvo!')


gerador = GeradorSenha()
gerador.Iniciar()
