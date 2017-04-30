import matplotlib.pyplot as plt
from scipy.optimize import minimize
import numpy as np
import csv
import random

"""
Module for the pronostics definitions and calculations
"""

def readData(filePath):
	data = []
	with open(filePath,newline="") as f:
		reader = csv.reader(f)
		for row in reader:
			data.append(float(row[0]))
	return data

def calcPronostic(data, weeks=12, alpha = random.triangular()):
	data = [float(x) for x in data]
	pronostic = [np.mean(data[:weeks])]
	#print(pronostic)
	for i in range(weeks,len(data)):
		#print(pronostic[(i-weeks)],data[i])
		pronostic.append( pronostic[(i-weeks)] + (alpha*(data[i]-pronostic[(i-weeks)])))
	return pronostic

def calcError(data, weeks=12, alpha = random.triangular()):
	pronostics=calcPronostic(data,weeks,alpha)
	return [(data[i]-pronostics[(i-weeks)]) for i in range(weeks,len(data))]

def calcAbsError(data, weeks=12, alpha = random.triangular()):
	return [abs(x) for x in calcError(data, weeks, alpha)]

def MAD(data, weeks=12, alpha = random.triangular()):
	return np.mean(calcAbsError(data, weeks, alpha))

def calcSqrError(data, weeks=12, alpha = random.triangular()):
	return [x**2 for x in calcAbsError(data, weeks, alpha)]

def MAPE(data, weeks=12, alpha = random.triangular()):
	absError = calcAbsError(data, weeks, alpha)
	return [absError[(i-weeks)]/data[i] for i in range(weeks,len(data))]

def ECM(data, weeks=12, alpha = random.triangular()):
	return np.mean(calcSqrError(data, weeks, alpha))

def meanMAPE(data, weeks=12, alpha = random.triangular()):
	return np.mean(MAPE(data, weeks, alpha))

def stdDeviation(data, weeks=12, alpha = random.triangular()):
	return np.sqrt(ECM(data, weeks, alpha))

def CVD(data, weeks=12, alpha = random.triangular()):
	return calcPronostic(data, weeks, alpha)[-1]/stdDeviation(data, weeks, alpha)

def findOptimalAlpha(data, weeks=12, alpha = random.triangular()):
	func = lambda x : MAD(data, weeks, alpha = x)
	return (minimize(func, [alpha]).x)



# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2*np.pi*t)
# plt.plot(t, s)
# data=readData('csvTest.csv')
# pronostic=calcPronostic(data,alpha=findOptimalAlpha(data))
# data=data[12:]
# l1,=plt.plot(np.arange(12,12+len(data),1),data,label="Datos históricos")
# l2,=plt.plot(np.arange(12,12+len(pronostic),1),pronostic,label="Pronóstico")
# plt.legend(handles=[l1, l2])
# plt.xlabel('Semanas')
# plt.ylabel('Demanda')
# plt.title('Pronostico de demanda vs datos reales')
# plt.grid(True)
# plt.savefig("test.png")
# plt.show()

