import random
import PySimpleGUI as sg


class GeradorSenha:
    def __init__(self):
        # Layout
        sg.theme('Topanga')
        layout = [
            [sg.Text('Gerador de senha segura!', size=(25, 1))],
            [sg.Text('Quantidade de caracteres'),
             sg.Combo(values=list(range(30)),
             key='total_caracteres', default_value=8, size=(3, 1))],
            [sg.Output(size=(32, 5))],
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
