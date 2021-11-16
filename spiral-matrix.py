from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        
        start_Row = 0
        start_Column = 0
        end_Row = len(matrix)
        end_column = len(matrix[0])
        output =[]
        while start_Row < end_Row or start_Column <end_column:
            #right
            if start_Row < end_Row:
                for i in range(start_Column,end_column):
                    output.extend([matrix[start_Row][i]])
            start_Row += 1
            #down
            if start_Column <end_column:
                for i in range(start_Row,end_Row):
                    output.extend([matrix[i][end_column - 1]])
            end_column -= 1
            
            #left
            if start_Row < end_Row:
                for i in range(end_column - 1,start_Column -1, -1):
                    output.extend([matrix[end_Row - 1][i]])
            end_Row -= 1
            
            #up
            if start_Column <end_column:
                for i in range(end_Row - 1,start_Row -1, -1):
                    output.extend([matrix[i][start_Column]])
            start_Column += 1
            
        return output

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        res = []
        x_min = 0; x_max = len(matrix[0]) - 1
        y_min = 0; y_max = len(matrix) - 1
        
        def traverse(matrix, x0, y0, x_i, y_i):
            while x_min <= x0 <= x_max and y_min <= y0 <= y_max:
                res.append(matrix[y0][x0])
                x0 = x0 + x_i
                y0 = y0 + y_i 
                
        x = 0
        y = 0
        while x_min <= x_max and y_min <= y_max:
            #traverse right
            traverse(matrix, x_min, y_min, 1, 0)
            y_min += 1
            #traverse down
            traverse(matrix, x_max, y_min, 0, 1)
            x_max -= 1
            #traverse left
            traverse(matrix, x_max, y_max, -1, 0)
            y_max -= 1
            #traverse up
            traverse(matrix, x_min, y_max, 0, -1)
            x_min += 1
            
        return res
    
    
    
obj1 = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = obj1.spiralOrder(matrix)
print(result)