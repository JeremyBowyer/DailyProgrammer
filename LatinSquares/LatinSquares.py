
class LatinSquare():
    
    def __init__(self, values):
        
        try:
            self.values = [int(s) for s in values]
        except ValueError as ve:
            raise ValueError("Please enter a list of all numbers or strings that can be coerced to numbers.")
            
            
        self.n = len(self.values)**(1/2)
        
        if not self.n.is_integer():
            raise Exception("Please enter a list of numbers that results in a square grid.")
        else:
            self.n = int(self.n)
            
        self.ncols = len(self.values) / n
        self.rows = [self.values[x:x+n] for x in range(0, len(self.values), n)]
        self.cols = [[row[index] for row in self.rows] for index in range(n)]
        self.vectors = self.rows + self.cols

            
    def checkCols(self):
        return all([len(col) == len(set(col)) for col in self.cols])
    
    def checkRows(self):
        return all([len(row) == len(set(row)) for row in self.rows])
    
    def checkSimilarity(self):
        return all([set(self.vectors[i]) == set(self.vectors[i+1]) for i,e in enumerate(self.vectors) if i < len(self.vectors)-1])
            

myList = [int(num) for num in input("Please enter n x n array of digits, top to bottom, left to right: ").split(' ')]

mySquare = LatinSquare(myList)
all([mySquare.checkCols, mySquare.checkRows, mySquare.checkSimilarity()])