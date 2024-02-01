import Adafruit_DHT
import time
from RPLCD.i2c import CharLCD
import datetime
import board
import psutil
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
from mysql.connector import connection, Error
#Zu zeigen das Inhalt in Github übertragen wurde

class Wetterstation:
    
    def __init__(self, id, stationsName, Stadt, Inhaber):
        self.id = id
        self.stationsName = stationsName
        self.Stadt = Stadt
        self.Inhaber = Inhaber
        self.wetterstationsbeobachter = [None]*3
        self.i = 0
        self.temperature = 0
        self.humidity = 0

    def benachrichtige(self):
        sensor = Adafruit_DHT.DHT11
        #Luftfeuchtigkeit, Temperatur
        pin = 18
        humidity, temperature = Adafruit_DHT.read(sensor, pin)
        for self.i in range (len(self.wetterstationsbeobachter)):
            self.wetterstationsbeobachter[self.i].update(temperature, humidity)
       		 print('mein name ist Taee')   

    def add(self, beobachter):
        self.wetterstationsbeobachter[self.i]=beobachter
        self.i = self.i + 1
        
    def getName(self):
        return self.stationsName
    
    def antwort(self, nachricht):
        print(nachricht)
        
    def messen_zeigen(self):
        pin = 18
        lcd = CharLCD('PCF8574', 0x27)
        lcd.cursor_pos = (0,0)
        
        while True:
            #try:
            sensor = Adafruit_DHT.DHT11
            #Luftfeuchtigkeit, Temperatur
            humidity, temperature = Adafruit_DHT.read(sensor, pin)
            
            print(humidity)
            print(temperature) 
            #Wenn Temp. und Luftf. nicht leer ist dann schreibe zu LCD
            if temperature is not None and humidity is not None:
                
                
                lcd.write_string("Temp     = {0:0.1f}C    Humidity = {1:0.1f}%".format(temperature, humidity))
                
                try:
                    zeitStempel = datetime.datetime.now().replace(microsecond=0)
                    con2 = connection.MySQLConnection(user='pi', password='1234', host='localhost', database='wetterKiel')
                    my_cursor = con2.cursor()
                    sql3 = 'INSERT INTO messWerte (timeStamp, temperatur, luftfeuchtigkeit) VALUES (%s, %s, %s)'
                    val = (zeitStempel, temperature, humidity)
                    my_cursor.execute(sql3, val)
                    con2.commit()
                    print("Daten in Datenbank geschrieben")
                    con2.close()

                except Error as exp:
                    print("Verbindung fehlgeschlagen")
                    con2.close()
                
                
            time.sleep(5.0)
            lcd.clear()
                         
        
