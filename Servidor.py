import socket
import threading


def recebermensagem(cliente_):
    while True:
        try:
            mensagem = cliente_.recv(1024).decode()
            print('mensagem do cliente:', mensagem)
        except Exception as e:
            print('Erro ao receber mensagem', e)
            cliente_.close()
            break


if __name__ == '__main__':
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    hostname = socket.gethostname()
    servidor.bind((socket.gethostbyname(hostname), 1226))

    servidor.listen()

    print('Servidor em execução')

    while True:
        cliente, endereco = servidor.accept()

        print('Cliente:', endereco)

        receber = threading.Thread(target=recebermensagem, args=(cliente,))
        receber.start()
