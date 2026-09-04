class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix), len(matrix[0])

        # 1) search over rows
        topR, botR=0,ROWS-1
        while topR<=botR:
            row = (topR+botR) // 2
            
            if matrix[row][-1]<target:
                topR= row+1
            elif matrix[row][0]>target:
                botR=row-1
            else:
                # row is the value we want
                break
 

        # 2) search inside the correct row
        leftC, rightC=0,COLS-1
        while leftC<=rightC:
            col = (leftC+rightC) // 2
            if matrix[row][col]<target:
                leftC= col+1
            elif matrix[row][col]>target:
                rightC=col-1
            else:
                return True
        return False
