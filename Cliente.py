import socket
import threading


def enviarmensagem(cliente_):
    while True:
        mensagem = input('Escreva a mensagem: ')
        cliente_.send(mensagem.encode())


if __name__ == '__main__':
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    cliente.connect((input('Insira o IP do Servidor: '), int(input('Insira a porta: '))))
    print('Conectado com o servidor')

    enviar = threading.Thread(target=enviarmensagem, args=(cliente,))
    enviar.start()
