class material():

    def __init__(self, name, duration, available = 0, required = 0):
        self.name = name
        self.duration = duration
        self.totalDuration = duration
        self.children = []
        self.childrenRequired = [] #children required by parent
        self.available = available
        self.required = required
        self.netRequirement = self.required - self.available
        if(self.netRequirement < 0):
            self.netRequirement = 0

    def addChild(self, child, requiredByParent):
        if(child not in self.children):
            self.children.append(child)
            self.childrenRequired.append(requiredByParent)
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
                indexOffset=(self.totalDuration-self.duration)-c.totalDuration
                partialWeeksChild=c.getRequirementsEachWeek()
                #print(self.name,partialWeeks,partialWeeksChild,indexOffset,self.totalDuration-self.duration)
                for i in range(indexOffset,self.totalDuration-self.duration):
                    partialWeeks[i] = partialWeeks[i] + partialWeeksChild[i-indexOffset] 
                #print(self.name,partialWeeks,partialWeeksChild,indexOffset,self.totalDuration-self.duration)
            partialWeeks = partialWeeks + [[(self.name,self.required)]]  + [[] for i in range(self.duration-1)]
            return partialWeeks
        else:
            #print(self.name, "hoja")
            return [[(self.name,self.required)]]+[[] for i in range(self.totalDuration-1)]



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


m1=material("Vibes", 1, required=50, available=10)
b=material("B", 2 ,15)
c=material("C", 1, 20)
d=material("D", 1, 10)
e1=material("E", 2, 10)
e2=material("E", 2, 10)
f=material("F", 3, 5)
g=material("G", 2, 0)
d2=material("D", 1, 10)

m1.addChild(b.addChild(d, 2).addChild(e1,2),2).addChild(c.addChild(e2,2).addChild(f.addChild(g,1).addChild(d2,2),2),3)
m1.updateTotalDuration()
#print(m1.totalDuration)
#m1.updateRequirements()
#print(d2.totalDuration)
#print(m1.getRequirementsEachWeek())



