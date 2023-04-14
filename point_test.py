class entity:
    from matplotlib import pyplot as plt
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.type = ''
        self.pointDict = {}
        
    def addPoint(self,x,y,name=None):
        try:
            self.pointDict[name]=[x,y]
        except:
            print("A same name entity is exists.")
        
    def setPoint(self,x,y):
        self.x = x
        self.y = y

    def getPoint(self,name=None):
        if name==None:
            return self.x, self.y
        else:
            return self.pointDict[name]

    def drawPoint(self,name=None):
        if name==None:
            self.plt.plot(self.x,self.y,'d')
        else:
            self.plt.plot(self.pointDict[name])

    def showPlot(self):
        self.plt.show()

        

def test():
    s = entity()
    s.setPoint(1,2)
    s.getPoint()
    s.drawPoint()
    s.showPlot()

    s.addPoint(3,4,'a')
    s.getPoint('a')
    s.drawPoint('a')
    s.showPlot()

if __name__ == '__main__':
    test()
