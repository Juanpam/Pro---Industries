class material():

    def __init__(self, name, duration, available = 0, required = 0):
        self.name = name
        self.duration = duration
        self.totalDuration = duration
        self.children = []
        self.childrenRequired = [] #children required by parent
        self.available = available
        self.required = required
        self.parent = None
        self.netRequirement = self.required - self.available
        if(self.netRequirement < 0):
            self.netRequirement = 0

    def addChild(self, child, requiredByParent):
        if(child not in self.children):
            child.parent=self
            self.children.append(child)
            self.childrenRequired.append(requiredByParent)
        return self

    def delChild(self, child):
        if(child in self.children):
            index = self.children.index(child)
            self.children.pop(index)
            self.childrenRequired.pop(index)
        return self

    def updateRequirements(self):
        self.netRequirement = self.required - self.available
        if(self.netRequirement < 0):
            self.netRequirement = 0
        if(self.children):
            for i,c in enumerate(self.children):
                #print(self.required,self.childrenRequired[i],c.name)
                c.required = self.netRequirement * self.childrenRequired[i]
                c.updateRequirements()


    def updateTotalDuration(self):
        if(self.children):
            total = self.duration
            totalChildren = 0
            for i,c in enumerate(self.children):
                c.updateTotalDuration()
                totalChildren = max(totalChildren,c.totalDuration)
            total = total + totalChildren
            self.totalDuration = total
        else:
            self.totalDuration = self.duration

    def getRequirementsEachWeek(self):
        self.updateTotalDuration()
        self.updateRequirements()
        if(self.children):
            partialWeeks = [[] for i in range(self.totalDuration-self.duration)]
            #print(self.name, self.totalDuration,partialWeeks,"padre")
            for c in self.children:
                #indexOffset=(self.totalDuration-self.duration)-c.totalDuration
                partialWeeksChild=c.getRequirementsEachWeek()
                extraQuantity=((c.duration-1)+len(partialWeeksChild))-(self.totalDuration-self.duration)
                extraQuantityForChild = -extraQuantity
                
                extraParent = [[] for i in range(extraQuantity)]
                extraChild = [[] for i in range(extraQuantityForChild)]
                #print(extraQuantity, extraParent, extraQuantityForChild, extraChild)
                #print("antes",partialWeeks)
                partialWeeks = extraParent + partialWeeks
                #print("despues",partialWeeks)
                partialWeeksChild = extraChild + partialWeeksChild
                #print(self.name,partialWeeks,partialWeeksChild,self.totalDuration-self.duration)
                for i in range(len(partialWeeksChild)):
                    partialWeeks[i] = partialWeeks[i] + partialWeeksChild[i] 
                #print(self.name,partialWeeks,partialWeeksChild,self.totalDuration-self.duration)
                if(extraQuantity>0):
                    partialWeeks = partialWeeks[extraQuantity:]
            partialWeeks = partialWeeks +  [[(self.name,self.required,self.available)]]
            return partialWeeks
        else:
            #print(self.name, "hoja")
            return [[] for i in range(self.totalDuration-1)] + [[(self.name,self.required,self.available)]] 

    def getNetRequirementsEachWeek(self):
        requirementsWeek = self.getRequirementsEachWeek()
        netRequirementsWeek = [[] for i in range(len(requirementsWeek))]
        availablesLeft = []
        for i,w in enumerate(requirementsWeek):
            for p in w:
                if p[0] not in [a[0] for a in availablesLeft]:
                    netRequirement = p[1]-p[2]
                    if(netRequirement <0):
                        netRequirement=0
                    availablesLeft.append((p[0], p[2]-(p[1]-netRequirement))) #Here is stored how many availables are still unused
                    #print(availablesLeft)
                    netRequirementsWeek[i].append((p[0],p[1],p[2],netRequirement))
                else:
                    index = [a[0] for a in availablesLeft].index(p[0])
                    netRequirement = p[1]-availablesLeft[index][1]
                    if(netRequirement <0):
                        netRequirement=0
                    availablesLeft[index]=(p[0], availablesLeft[index][1]-(p[1]-netRequirement)) #Here is updated how many availables are still unused
                    #print(availablesLeft)
                    netRequirementsWeek[i].append((p[0],p[1],availablesLeft[index][1],netRequirement))
        return netRequirementsWeek


    def getMaterialsNames(self):
        names = [self.name]
        if(not self.children):
            return names
        else:
            for c in self.children:
                names += c.getMaterialsNames()
                names += [c.name]
            names = list(set(names))
            return names



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


# m1=material("Vibes", 1, required=50, available=10)
# b=material("B", 2 ,15)
# c=material("C", 1, 20)
# d=material("D", 1, 10)
# e1=material("E", 2, 10)
# e2=material("E", 2, 10)
# f=material("F", 3, 5)
# g=material("G", 2, 0)
# d2=material("D", 1, 10)

# m1.addChild(b.addChild(d, 2).addChild(e1,2),2).addChild(c.addChild(e2,2).addChild(f.addChild(g,1).addChild(d2,2),2),3)
# m1.updateTotalDuration()
# #print(m1.totalDuration)
# m1.updateRequirements()
# # print(d2.totalDuration)
# # print(m1.getRequirementsEachWeek())
# print(m1.getNetRequirementsEachWeek())
# print(e1.totalDuration,e1.netRequirement)
# print(e2.totalDuration,e2.netRequirement)
# m1.updateRequirements()
# print(c.netRequirement)
# print(c.parent)



