import random
from Fecha import Fecha
import sys
def numRandomGenerator(cant):
	numRandom = ""
	for n in range(cant):
		num = str(random.randint(0,9))
		numRandom = numRandom + num 
	return numRandom

def alphaRandomGenerator(cant):
	alpha = "ABCDEFGHIJKLMNÑOPQRSTUVWXZ"
	alphaRandom = ""
	for n in range(cant):
		posRandom = random.randint(0,len(alpha)-1)
		alphaRandom = alphaRandom + alpha[posRandom]
	return alphaRandom

def alphaNumRandomGenerator(cant):
	alphaNum = "ABCDEFGHIJKLMNÑOPQRSTUVWXZ0123456789"
	alphaNumRandom = ""
	for n in range(cant):
		posRandom = random.randint(0,len(alphaNum)-1)
		alphaNumRandom = alphaNumRandom + alphaNum[posRandom]
	return alphaNumRandom

def vocalRandomGenerator(cant):
	vocal = "AEIOU"
	vocalRandom = ""
	for n in range(cant):
		posRandom = random.randint(0,len(vocal)-1)
		vocalRandom = vocalRandom + vocal[posRandom]
	return vocalRandom

def alphaVocalRandomGenerator(cant):
	alphaVocal = ""
	for n in range(cant):
		seed = int(numRandomGenerator(1))
		if seed % 2 == 0:
			alphaVocalUnit = alphaRandomGenerator(1) + vocalRandomGenerator(1)
		else:
			alphaVocalUnit = vocalRandomGenerator(1) + vocalRandomGenerator(1)
		alphaVocal = alphaVocal + alphaVocalUnit
	return alphaVocal

def randomGenero(cant):
	genero = "HM"
	generoRandom = ""
	for n in range(cant):
		posRandom = random.randint(0,len(genero)-1)
		generoRandom = generoRandom + genero[posRandom]
	return generoRandom

def consonanteRandom(cant):
	consonante = "BCDFGHJKLMNÑPQRSTVWXZ"
	consonanteRandom = ""
	for n in range(cant):
		posRandom = random.randint(0,len(consonante)-1)
		consonanteRandom = consonanteRandom + consonante[posRandom]
	return consonanteRandom

def entidadRandom(cant):
	entidad = ['AS','BC','BS','CC','CS','CH','CL','CM','DF','DG','GT','GR','HG','JC','MC','MN','MS','NT','NL','OC','PL','QT','QR','SP','SL','SR','TC','TL','TS','VZ','YN','ZS']
	entidadRandom = ""
	for n in range(cant):
		posRandom = random.randint(0,len(entidad)-1)
		entidadRandom = entidadRandom + entidad[posRandom]
	return entidadRandom


def randomRFC():
	randomRFC = alphaRandomGenerator(4) + numRandomGenerator(6) + alphaNumRandomGenerator(3)
	return randomRFC


def randomCURP():
	fecha = Fecha('00','00','00')
	randomCURP = alphaVocalRandomGenerator(1) + alphaRandomGenerator(2) + fecha.getDateRandomyymmdd() + randomGenero(1) + entidadRandom(1) + consonanteRandom(3) + alphaNumRandomGenerator(2)
	return randomCURP

def main():
	params = sys.argv
	for param in params:
		if param == "--rfc":
			print(randomRFC())
		elif param == "--curp":
			print(randomCURP())

main()