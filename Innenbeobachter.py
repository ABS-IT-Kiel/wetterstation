from Wetterstationsbeobachter import Wetterstationsbeobachter
from Wetterstation import Wetterstation
#afkjsahfkajfhkjsagsa
class Innenbeobachter(Wetterstationsbeobachter):
	def __init__(self, wetterstation, beoName, beoStandort):
		super().__init__(wetterstation, beoName, beoStandort)

	def update(self, temperature, humidity):
		print('Information von der Wetterstation im Haus erhalten \n Temperatur beträgt: '+str(temperature)+'°C')
		self.wetterstation.antwort('Rueckmeldung von ABS-It Boeck')
		self.wetterstation.antwort('Rueckmeldung vom Innenbeobachter')
		
		
		
		
