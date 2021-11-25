# MQTT
O trabalho escolar é uma simulação de aplicação de IoT para monitorar uma granja.

Instruções dadas pelo professor:

![image](https://user-images.githubusercontent.com/94933775/143328450-70367451-88f2-4a03-96dc-8b687a3c9918.png)

Dispositivo será simulado utilizando o software RealTerm
https://realterm.sourceforge.io/

Porta serial será emulada utilizando o software VSPE
http://www.eterlogic.com/Downloads.html

O trabalho é uma simulação de aplicação de IoT que utiliza sensores para monitorar uma
granja de criação de aves para corte. Esses animais, quando criados em regime de
confinamento, são sensíveis a temperatura e umidade por isso essas grandezas devem
monitoradas.

Além disso, para que haja um melhor desenvolvimento não deve faltar água e ração
para os animais.

Nesse cenário os sensores de temperatura, umidade, nível do reservatório de ração e
nível do reservatório da água estão ligados em um dispositivo microcontrolado
(Arduino, MSP, ARM e etc) que envia a informação utilizando canal serial para uma
central de monitoramento. No nosso caso o microcontrolador será simulado utilizando
o RealTerm.

A central de monitoramento informa os valores medidos localmente e também os envia para um Broker de IoT onde o proprietário pode acompanhar tais valores online. A central será o computador onde um programa em Python realiza a leitura dos dados na porta serial e os envia para o Broker de IoT utilizando protocolo MQTT.

Iremos utilizar o Ubidots como Broker.

	• Faixa de medida do sensor de temperatura: 0 a 99 graus (apenas valores inteiros)

	• Faixa de medida do sensor de umidade: 0 a 99 graus (apenas valores inteiros)

	• Faixa de medida do sensor de nível reservatório da ração: 0 % a 99 % (apenas valores inteiros)

	• Faixa de medida do sensor de nível do reservatório da água: 0 % a 99 % (apenas valores inteiros)


Características da comunicação serial:

	• Buffer de tamanho fixo igual a 09 bytes

	• Marcador de final do buffer 0x02 hexadecimal

	• As informações devem ser enviadas em Hexadecimal (linha em verde)

	• Exemplo de buffer para:

		o Temperatura = 28 graus

		o Umidade = 87 %

		o Nível do reservatório de água = 50 %

		o Nível do reservatório de ração = 75 %

![image](https://user-images.githubusercontent.com/94933775/143328739-e945cb6d-f09c-4307-ad02-1243a2b841b3.png)

Ao receber o buffer pela comunicação serial o programa em Python deve verificar se o tamanho
e o valor do último byte estão de acordo com a especificação.
Os valores recebidos pela serial devem ser exibidos em uma Dashboard no Ubidots.
