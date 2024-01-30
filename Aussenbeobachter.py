from Wetterstationsbeobachter import Wetterstationsbeobachter

class Aussenbeobachter(Wetterstationsbeobachter):
	def __init__(self, wetterstation, beoName, beoStandort):
		super().__init__(wetterstation, beoName, beoStandort)

	def update(self, temperature, humidity):
		print('Information von der Wetterstation von außen erhalten \n Temperatur beträgt: '+str(temperature)+'°C')
		self.wetterstation.antwort('Rueckmeldung vom Aussenbeobachter')
		
		
		
		

