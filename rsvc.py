class Band:
    """This module is used to calculate the resistance value of resistors given the color values, also it will reverse a given number to its corresponding color code"""
    def __init__(self,band1,band2,band3,band4):
        """This init recieves the color codes of the resistors in order"""
        self.band1 = band1 
        self.band2 = band2 
        self.band3 = band3 
        self.band4 = band4 
        self.color = {'black': 0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'grey':8,'white':9,'gold':5,'silver':10,'none':20}
    def placevalue(self):   
        '''This returns the numerical value of the resistance'''
        bands = [self.band1,self.band2,self.band3,self.band4]
        NewBands =[]
        for band in bands:
            band=self.color[band]
            NewBands.append(band)
        res_value = (NewBands[0]*10 +NewBands[1])*10**(NewBands[2]-1)
        return f'Resistor value in ohms is {res_value} with a tolerance of {NewBands[3]}%'
    def reVerse(self,value,tolerance=None):
        '''This will return the color codes corresponding to a particular resistor value'''
        tolCol = {5:'gold',10:'silver',20:'none'}
        main_band,multiplier = self.splitter(value)
        firstBand = main_band[0]
        secBand =main_band[1]
        thirdBand = len(multiplier)
        bandlist = {'band1':firstBand,'band2':secBand,'band3':thirdBand}
        for keys,i in bandlist.items():
            i = int(i)
            for key,value in self.color.items():
                if i == value:
                    print(f'{keys} = {key}')
        for i,j in tolCol.items():
            if tolerance == i:
                return f'band4 ={j}'
            elif tolerance is None:
                return None
      
    def splitter(self,x):
            x=str(x)
            mb = x[0:2]
            mull = x[2:-1]
            return mb,mull