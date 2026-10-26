# Project-2.1 code
In deze github pagina bevind zich alle code gebruikt voor de geautomatiseerde interferometer metingen.
<br><br>
Voor gebruik van deze code zijn volgende stappen vereist:
<br><br>
&ensp; 1- Compile de arduino code op een Arduino Uno Minima.

&ensp; 2- Connect de hardware volgens volgende instructies:

    Lichtsensor:
      Out -> Arduino pin_A0, Ground

    Motor-driver:
      VIO, Ground -> Arduino 5V, Ground
      Ms1 -> Arduino 3.3V
      En -> Arduino pin_8
      Step -> Arduino pin_9
      Dir -> Arduino pin_10
      VM, Ground -> 12V DC power, Ground
      A1,A2,B1,B2 -> Motor coils

&ensp; <img width="397" height="333" alt="image" src="https://github.com/user-attachments/assets/171fed75-26d3-4a39-b1fa-7c531ae43a5d" />

&ensp; 3- Connect de Arduino aan de computer via usb.

&ensp; 4- Achterhaal de naam van de gebruikte usb-port in instellingen.

&ensp; 5- Verander in Main.py op line 17 port naar de naam van de gebruikte usb-port.

&ensp; 6- Run Main.py.
