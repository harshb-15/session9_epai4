import math
class Polygon:
    def __init__(self, edges, radius):
        if edges<3:
            raise TypeError("Number of Edges should be more than 2")
        self.vertices=round(edges,2)
        self.circumradius=round(radius,2)
        self.intAngle=round(((self.vertices-2)*180)/self.vertices,2)
        self.edgeLength=round(2*self.circumradius*math.sin(math.pi/self.vertices),2)
        self.apothem=round(self.circumradius*math.cos(math.pi/self.vertices),2)
        self.area=round((self.vertices*self.edgeLength*self.apothem)/2,2)
        self.perimeter=round(self.vertices*self.edgeLength,2)
    def __repr__(self):
        return f"Regular Convex Polygon : Sides = {self.vertices}, Radius = {self.circumradius}, Angle = {self.intAngle}, Side Length = {self.edgeLength}, Apothem = {self.apothem}, Area = {self.area}, Perimeter = {self.perimeter}"
    def __eq__(self,other):
        if self.vertices==other.vertices and self.circumradius==other.circumradius:
            return True
        else:
            return False
    def __gt__(self,other):
        if self.vertices>other.vertices:
            return True
        else:
            return False
    
class Polygon_Sequence:
    def __init__(self,edges, radius):
        self.circumradius=radius
        self.maxedges=edges
        self.lst=[Polygon(t,self.circumradius) for t in range(3,edges+1)]
    
    def __getitem__(self,s):
        if isinstance(s,int):
            return self.lst[s]
        else:
            return self.lst[s]
            
    def getMaxEPoly(self):
        mx=-1
        mxp=-1
        for i in self.lst:
            ratio=i.area/i.perimeter
            if ratio>=mx:
                mxp=i
                mx=ratio
        return f"Maximum Efficiancy Polygon with ratio {round(mx,2)}:- {mxp} "

    def __len__(self):
        return len(self.lst)
    
    def __repr__(self):
        return f"Polygon Sequence :- Common Radius: {self.circumradius}, Max Number of Edges: {self.maxedges} "
        
            
            
