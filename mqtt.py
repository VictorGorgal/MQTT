from time import sleep
from serial import Serial
from paho.mqtt.client import Client
from json import dumps


class ConexaoMqttSerial:
    def __init__(self):
        self.connected = False
        self.running = False
        self.conexao_serial = None

    def serial(self, serial_baudrate, porta_serial):
        conexao_serial = Serial()
        conexao_serial.baudrate = serial_baudrate
        conexao_serial.port = porta_serial
        conexao_serial.xonxoff = True
        conexao_serial.timeout = 0
        self.conexao_serial = conexao_serial

        conexao_serial.open()
        if conexao_serial.is_open:
            print(f'Porta {porta_serial} aberta com sucesso')
        else:
            print('Nao foi possivel abrir a porta serial, o programa sera fechado')
            exit()

    def mqtt(self, url, token, port):
        def on_mqtt_publish(*args):
            print('publicado')

        self.client = Client()
        self.broker, self.topic = url.split('/', 1)
        if not self.connected:
            self.client.username_pw_set(token, password='')
            self.client.on_connect = self.on_mqtt_connect
            self.client.on_publish = on_mqtt_publish
            self.client.connect(self.broker, port=port)
            self.client.loop_start()

            for i in range(3):
                sleep(2)
                if self.connected:
                    break

        if not self.connected:
            print('Erro ao se conectar ao broker')

    def on_mqtt_connect(self, *args):
        if args[3] == 0:
            self.connected = True
        else:
            print('Falha ao conectar')

    def post(self, dados):
        dados = {'temp': dados[0], 'umidade': dados[1], 'nivel_racao': dados[2], 'nivel_agua': dados[3]}
        payload = dumps(dados)

        try:
            self.client.publish('/' + self.topic, payload=payload)
        except Exception as e:
            print('Erro:\n', e)

    def run(self):
        def ler_dados(dados):
            to_return = []
            for i in range(0, 8, 2):
                to_return.append((dados[i] - 48) * 10 + dados[i + 1] - 48)
            return to_return

        self.running = True

        while self.running:  # main loop
            fila = self.conexao_serial.in_waiting
            if fila > 0:
                dados = self.conexao_serial.read(fila)
                self.conexao_serial.reset_input_buffer()

                if len(dados) != 9:
                    print('Utilizar buffer de 9 bytes')
                elif dados[8] != 2:
                    print('caracter de fim de buffer incorreto')
                else:
                    dados = ler_dados(dados)

                    self.post(dados)  # manda as informações para o ubidots

                    sleep(2)


if __name__ == '__main__':
    inst = ConexaoMqttSerial()  # inicializa uma instancia da classe

    inst.serial(serial_baudrate=9600, porta_serial='COM2')  # configura e abre a comunicação serial

    URL = 'industrial.api.ubidots.com/v1.6/devices/xxx'
    TOKEN = 'xxx'
    inst.mqtt(url=URL, token=TOKEN, port=1883)  # inicializa a comunicação mqtt

    inst.run()  # começa o loop principal da classe (ler porta serial e mandar para o ubidots)
    sleep(5)
