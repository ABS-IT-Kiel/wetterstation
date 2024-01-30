from abc import ABC, abstractmethod

class Wetterstationsbeobachter:
	def __init__(self, wetterstation, beoName, beoStandort):
		self.wetterstation = wetterstation
		self.beoName = beoName
		self.beoStandort = beoStandort



	@abstractmethod
	def update(self, temperature, humidity):
		pass

	def getName(self):
		return self.beoName

	def getStandort(self):
		return self.beoStandort
