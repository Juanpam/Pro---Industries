
class machine():
    """
    Machine class used to represent machines, products and raw materials in a production chain.
    """
    def __init__(self, name, duration, disponibility, quantity=1, children=None):
        self.__childrenDuration = []
        self.__updated = False
        self.name = name
        self.duration = duration
        self.disponibility = disponibility
        self.quantity = quantity
        if(not children):
            self.children = []
        else:
            self.children = children
        if(not self.children):
            self.kind = "raw"

    def addChildren(self, machine):
        self.children.append(machine)
        self.__updated = False
        self.kind = "machine"
        return self


    def indexChildren(self, children): #Children is a list of children
        ans = -1
        for i,c in enumerate(children):
            if self.name==c.name:
                ans=i
        return ans

    def calcTreeDuration(self):
        if not self.children: #If there is no children there is no duration
            return []
        else:
            self.__childrenDuration = self.children[:] #At least we have the children in duration
            #print(self.children)
            for i in self.children:
                #print(i)
                grandchildDuration = i.getChildrenDuration()
                #print(i,grandchildDuration)
                for j in grandchildDuration:
                    found = False
                    for l,k in enumerate(self.__childrenDuration):
                        if j.name==k.name:
                            self.__childrenDuration[l] = machine(j.name, k.duration+j.duration, j.disponibility)
                            found = True
                            break
                    if(not found):
                        self.__childrenDuration.append(machine(j.name, j.duration, j.disponibility))
                    #print("lala",self.__childrenDuration)
        self.__childrenDuration.sort(key = lambda x: x.name)
        self.__updated = True

    def getChildrenDuration(self):
        if(not self.__updated): # If tree duration is not updated
            self.calcTreeDuration()
        return self.__childrenDuration

    def getChildDuration(self,child):
        ans = 0 #Return -1 if child isnt in the self tree
        if(child.indexChildren(self.getChildrenDuration()) != -1):
            durations = [o.duration for o in self.getChildrenDuration()]
            ans= (durations[[o.name for o in self.getChildrenDuration()].index(child.name)])
        return ans

    def __repr__(self):
        return str((self.name,self.duration))

    def __str__(self):
        return str((self.name,self.duration))

    def __eq__(self,other):
        return self.name==other.name

    def __ne__(self,other):
        return self.name!=other.name
    def __hash__(self):
        return hash(self.name)

class product(machine):



    def __init__(self, name, demand, priceUnit):
        super().__init__(name, 0, None)
        self.kind = self.kind + "product"
        self.demand = demand
        self.totalTimeDuration = []
        self.priceUnit = priceUnit
        self.rawMaterials = []

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    def addChildren(self, machine):
        super().addChildren(machine)
        if(self.children):
            self.kind = "product"
        return self

    def calcTotalTimeDuration(self):
        self.totalTimeDuration = [a.duration*self.demand for a in self.getChildrenDuration()] 
        return self.totalTimeDuration

    def addRawMaterial(self, rawMaterial, cost):
        if(rawMaterial not in self.rawMaterials):
            self.rawMaterials.append((rawMaterial,cost))

    def getChildTotalDuration(self,child):
        ans = 0 #Return -1 if child isnt in the self tree
        if(child.indexChildren(self.getChildrenDuration())!=-1):
            durations = self.calcTotalTimeDuration()
            ans= (durations[[o.name for o in self.getChildrenDuration()].index(child.name)])
        return ans

    def calcUsedTimePercent(self):
        a = self.calcTotalTimeDuration()
        #The percent of total time used from the total time available
        return [(a[i]/k.disponibility)*100 for i,k in enumerate(self.getChildrenDuration())]

    def getNetProfit(self):
        return self.priceUnit - sum([i[1] for i in self.rawMaterials])



def productsTotalTime(*products):
    names = [[(n.name,n.disponibility) for n in p.getChildrenDuration()] for p in products]
    names = sorted(list(set(sum(names,[]))))
    total = [[p.getChildTotalDuration(machine(name[0],0,name[1])) for name in names] for p in products]
    total = [sum(i) for i in zip(*total)]
    return total

def productsPercTime(*products):
    names = [[(n.name,n.disponibility,n.quantity,n) for n in p.getChildrenDuration()] for p in products]
    names = sorted(list(set(sum(names,[])))) #Get names from machines and eliminate duplicates
    disponibilities = [n[1] for n in names]
    quantity = [n[2] for n in names]
    total = [[p.getChildTotalDuration(machine(name[0],0,name[1])) for name in names] for p in products]
    total = [sum(i) for i in zip(*total)]
    total = [(names[i][3],100*(total[i]/(disponibilities[i]*quantity[i]))) for i in range(len(total))]
    return total

def bottleNeck(*products):
    bottleNeckList = [i for i in productsPercTime(*products) if i[1]>100]
    bottleNeckList = [([p.getChildDuration(b[0]) for p in products], b[1],b[0]) for b in bottleNeckList]
    return bottleNeckList

def profitableTime(*products):
    bn = bottleNeck(*products)[0][0]
    np = [(p,p.getNetProfit()) for p in products]
    return [(np[i][0],np[i][1]/bn[i]) for i in range(len(products))]

def optimalProduct(*products):
    return max(profitableTime(*products),key=lambda x:x[1])[0]

def optimalCombination(*products):
    products = list(products)
    ans = []
    bn =bottleNeck(*products)
    bnmachine = bn[0][2]
    disponibility = bnmachine.disponibility
    opList = sorted(profitableTime(*products), key = lambda x: x[1], reverse=True)
    print(opList)
    while(opList and disponibility>0):
        op=opList[0]
        p=op[0]
        ans.append((p, min((disponibility, p.demand*p.getChildDuration(bnmachine)))))
        opList.remove(op)
        disponibility = disponibility - min(disponibility, p.demand*p.getChildDuration(bnmachine))
        print(opList)
    ans = [a[1] for a in ans]
    ans = [ans[i] // bn[0][0][i] for i in range(len(ans))]
    return ans



# p = product("p", 100, 90)
# q = product("q", 50, 100)
# p.addRawMaterial("mp1", 20)
# p.addRawMaterial("mp2", 20)
# p.addRawMaterial("adicional", 5)
# q.addRawMaterial("mp2", 20)
# q.addRawMaterial("mp3", 20)



# a = machine("a", 15, 2400)
# a2 = machine("a", 10, 2400)
# b = machine("b", 15, 2400)
# b2 = machine("b", 15, 2400)
# c = machine("c", 10, 2400)
# c2 = machine("c", 5, 2400)
# d = machine("d", 10, 2400)
# d2 = machine("d", 5, 2400)

# p.addChildren(d.addChildren(c.addChildren(a)).addChildren(c2.addChildren(b)))
# q.addChildren(d2.addChildren(c2).addChildren(b2.addChildren(a2)))
# print(productsPercTime(p,q))
# print(bottleNeck(p,q),"lala")
# print(profitableTime(p,q))
# print(optimalProduct(p,q))
# print(optimalCombination(p,q))




# p = product("p", 110, 120)
# q = product("q", 90, 110)

# d = machine("d", 20, 2, 2400)
# c = machine("c", 10, 2400)
# b = machine("b", 20, 2400)
# d2 = machine("d", 15, 2, 2400)
# b2 = machine("b", 10, 2400)
# a = machine("a", 10, 2400)

# p.addChildren(d.addChildren(c.addChildren(b)))



# q.addChildren(d2.addChildren(b2.addChildren(a).addChildren(c)))
# print(q.calcUsedTimePercent())

# z = product("z", 10, 400)
# z.addChildren(b)

# print(bottleNeck(p,q))