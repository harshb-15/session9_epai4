from Objective1 import Polygon
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
        return f"Maximum Efficiancy Polygon with ratio {round(mx,2)} is {mxp} "

    def __len__(self):
        return len(self.lst)
    
    def __repr__(self):
        return f"Polygon Sequence :- Common Radius: {self.circumradius}, Max Number of Edges: {self.maxedges}, Number of Polygons: {len(self.lst)} "