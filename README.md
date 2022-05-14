# MQTT
Simulation of IoT application to monitor a farm.

Instructions given by the teacher:

![image](https://user-images.githubusercontent.com/94933775/143328450-70367451-88f2-4a03-96dc-8b687a3c9918.png)

Serial device will be simulated using RealTerm software: https://realterm.sourceforge.io/

Serial port will be emulated using VSPE software: http://www.eterlogic.com/Downloads.html

The project is a simulation of an IoT application that uses sensors to monitor a poultry farm. These animals, when raised in a confinement, are sensitive to temperature and humidity, so these quantities must monitored.

In addition, for a better development, there should be no lack of water and food for the animals.

In this scenario, the temperature, humidity, feed reservoir level and
water reservoir level are connected in a microcontroller 
(Arduino, MSP, ARM, etc.) that sends the information using a serial port to a
monitoring center. In our case the microcontroller will be simulated using
the RealTerm.

The monitoring center reports the measured values locally and also sends them to an IoT Broker where the owner can track these values online. The central will be the computer where a Python program reads the data on the serial port and sends it to the IoT Broker using the MQTT protocol.

We will use Ubidots as a Broker.

	• Temperature sensor measurement range: 0 to 99 degrees (integer values only)

	• Humidity sensor measurement range: 0 to 99 degrees (integer values only)

	• Measuring range of the feed reservoir level sensor: 0 % to 99 % (integer values only)

	• Measuring range of the water tank level sensor: 0 % to 99 % (integer values only)

Serial communication features:

	• Fixed size buffer equal to 09 bytes

	• End-of-buffer marker 0x02 hexadecimal

	• Information must be sent in Hexadecimal (green line)

	• Buffer example for:

		o Temperature = 28 degrees

		o Humidity = 87%

		o Water tank level = 50%

		o Feed reservoir level = 75%

![image](https://user-images.githubusercontent.com/94933775/143328739-e945cb6d-f09c-4307-ad02-1243a2b841b3.png)

Ao receber o buffer pela comunicação serial o programa em Python deve verificar se o tamanho
e o valor do último byte estão de acordo com a especificação.
Os valores recebidos pela serial devem ser exibidos em uma Dashboard no Ubidots.
