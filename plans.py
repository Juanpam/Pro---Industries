import csv
import math as m
def readData(filePath):
    demand = []
    daysMonth = []
    with open(filePath,newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            demand.append(int(row[0]))
            daysMonth.append(int(row[1]))
    return (demand,daysMonth)

def pRate(anual,op,daysYear):
	return float(anual)/(op*daysYear)

def planZero(demandMonth, daysMonth, anual, daysYear, opLastYear, invCost, delUnitCost, opCost, opFireCost, salaryHour, workTimeDay, opInitial):
	rate = round(pRate(anual, opLastYear, daysYear),0)
	opNeed = [m.ceil(demandMonth[i]/(daysMonth[i]*rate)) for i in range(len(daysMonth))]
	opUnits = [round(daysMonth[i]*rate) for i in range(len(daysMonth))]
	opAvailable = [opInitial] + opNeed[:-1]
	contrated = [opNeed[i]-opAvailable[i] if opNeed[i]>opAvailable[i] else 0 for i in range(len(opNeed)) ]
	contratedCost = [opCost*c for c in contrated]
	fired = [opAvailable[i] - opNeed[i] if opAvailable[i]>opNeed[i] else 0 for i in range(len(opNeed)) ]
	firedCost = [opFireCost * f for f in fired]
	totalSalary = [opNeed[i]*daysMonth[i]*salaryHour*workTimeDay for i in range(len(opNeed))]
	unityProduced = demandMonth[:]
	netInv = [0 for i in opNeed]
	strCost = netInv[:]
	delCost = netInv[:]
	opUsed = opNeed[:]
	totalCost = [contratedCost[i]+firedCost[i]+totalSalary[i] for i in range(len(contratedCost))]
	unityProduced = demandMonth[:]

	return [daysMonth,opUnits,demandMonth,opNeed,opAvailable,contrated,contratedCost,fired,firedCost,opUsed,totalSalary,unityProduced,netInv,strCost,delCost,totalCost]

def opConstant(demandMonth,daysMonth,rate):
	return m.ceil(sum(demandMonth)/(sum(daysMonth)*rate))

def opAcumulate(demandMonth,daysMonth,rate):
	daysAc = [sum(daysMonth[:i+1]) for i in range(len(daysMonth))]
	demandAc = [sum(demandMonth[:i+1]) for i in range(len(demandMonth))]
	#print(daysAc, demandAc)
	opAc = [round(demandAc[i]/(rate*daysAc[i]),0) for i in range(len(daysAc))]
	#print(daysAc, demandAc,opAc)
	return max(opAc)

def planConstant(demandMonth, daysMonth, anual, daysYear, opLastYear, invCost, delUnitCost, opCost, opFireCost, salaryHour, workTimeDay, opInitial):
	rate = round(pRate(anual, opLastYear, daysYear),0)
	opConst = opConstant(demandMonth, daysMonth, rate)
	opNeed = [opConst for i in demandMonth]
	opUnits = [round(daysMonth[i]*rate) for i in range(len(daysMonth))]
	opAvailable = [opInitial] + opNeed[:-1]
	opAvailable = [opInitial] + opNeed[:-1]
	contrated = [opNeed[i]-opAvailable[i] if opNeed[i]>opAvailable[i] else 0 for i in range(len(opNeed)) ]
	contratedCost = [opCost*c for c in contrated]
	fired = [opAvailable[i] - opNeed[i] if opAvailable[i]>opNeed[i] else 0 for i in range(len(opNeed)) ]
	firedCost = [opFireCost * f for f in fired]
	totalSalary = [opNeed[i]*daysMonth[i]*salaryHour*workTimeDay for i in range(len(opNeed))]
	unityProduced = [rate*opNeed[i]*daysMonth[i] for i in range(len(daysMonth))]
	unityProduced[-1]=demandMonth[-1]
	netInv = []
	lastInv=0
	for i in range(len(demandMonth)):
		netInv.append((lastInv + unityProduced[i]) - demandMonth[i])
		lastInv=netInv[-1]
	netInv[-1]=0
	unityProduced[-1] += -netInv[-2] 
	strCost = [invCost * n if n>0 else 0 for n in netInv]
	delCost = [delUnitCost * n if n<0 else 0 for n in netInv]
	opUsed = opNeed[:]
	totalCost = [contratedCost[i]+firedCost[i]+totalSalary[i]+strCost[i]+delCost[i] for i in range(len(contratedCost))]


	return [daysMonth,opUnits,demandMonth,opNeed,opAvailable,contrated,contratedCost,fired,firedCost,opUsed,totalSalary,unityProduced,netInv,strCost,delCost,totalCost]

def planNoFault(demandMonth, daysMonth, anual, daysYear, opLastYear, invCost, delUnitCost, opCost, opFireCost, salaryHour, workTimeDay, opInitial):
	rate = round(pRate(anual, opLastYear, daysYear),0)
	opAc = opAcumulate(demandMonth, daysMonth, rate)
	opNeed = [opAc for i in range(len(daysMonth))]
	opUnits = [round(daysMonth[i]*rate) for i in range(len(daysMonth))]
	opAvailable = [opInitial] + opNeed[:-1]
	contrated = [opNeed[i]-opAvailable[i] if opNeed[i]>opAvailable[i] else 0 for i in range(len(opNeed)) ]
	contratedCost = [opCost*c for c in contrated]
	fired = [opAvailable[i] - opNeed[i] if opAvailable[i]>opNeed[i] else 0 for i in range(len(opNeed)) ]
	firedCost = [opFireCost * f for f in fired]
	totalSalary = [opNeed[i]*daysMonth[i]*salaryHour*workTimeDay for i in range(len(opNeed))]
	unityProduced = [rate*opNeed[i]*daysMonth[i] for i in range(len(daysMonth))]
	unityProduced[-1]=demandMonth[-1]
	netInv = []
	lastInv=0
	for i in range(len(demandMonth)):
		netInv.append((lastInv + unityProduced[i]) - demandMonth[i])
		lastInv=netInv[-1]
	netInv[-1]=0
	unityProduced[-1] += -netInv[-2] 
	strCost = [invCost * n if n>0 else 0 for n in netInv]
	delCost = [delUnitCost * n if n<0 else 0 for n in netInv]
	opUsed = opNeed[:]
	totalCost = [contratedCost[i]+firedCost[i]+totalSalary[i]+strCost[i]+delCost[i] for i in range(len(contratedCost))]

	return [daysMonth,opUnits,demandMonth,opNeed,opAvailable,contrated,contratedCost,fired,firedCost,opUsed,totalSalary,unityProduced,netInv,strCost,delCost,totalCost]


#demandMonth,daysMonth = readData("testPlan.csv")
anual=41383
daysYear=260
opLastYear=40
invCost=5
delUnitCost=15
opCost=450
opFireCost=600
salaryHour=15 
workTimeDay=8 
opInitial=35

#print(planZero(demandMonth, daysMonth, anual, daysYear, opLastYear, invCost, delUnitCost, opCost, opFireCost, salaryHour, workTimeDay, opInitial))
#print(planConstant(demandMonth, daysMonth, anual, daysYear, opLastYear, invCost, delUnitCost, opCost, opFireCost, salaryHour, workTimeDay, opInitial))
#print(planNoFault(demandMonth, daysMonth, anual, daysYear, opLastYear, invCost, delUnitCost, opCost, opFireCost, salaryHour, workTimeDay, opInitial))