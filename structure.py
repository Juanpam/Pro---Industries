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
        if(self.children):
            for i,c in enumerate(self.children):
                c.required = self.required * self.childrenRequired[i]
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


m1=material("Vibes", 1)
b=material("B", 2)
c=material("C", 1)
d=material("D", 1)
e1=material("E", 2)
e2=material("E", 2)
f=material("F", 3)
g=material("G", 2)
d2=material("D", 1)

m1.addChild(b.addChild(d, 2).addChild(e1,2),2).addChild(c.addChild(e2,2).addChild(f.addChild(g,1).addChild(d,2),2),3)
m1.updateTotalDuration()
print(m1.totalDuration)


