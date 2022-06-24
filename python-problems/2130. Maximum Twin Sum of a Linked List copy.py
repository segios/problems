from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        field: List[List[int]] = [ ]
        
        for i in range (3):
            field.append(['-']*3)
            # for j in range (3):
            #     field[i].append('-')

        count = 0
        currMove = 'x'

                 
        def getWinner():
            if field[0][0] == field[0][1] == field[0][2] and field[0][0] != '-' :
                return 'A' if field[0][0] == 'x' else 'B'

            if field[1][0] == field[1][1] == field[1][2] and field[1][0] != '-' :
                return 'A' if field[1][0] == 'x' else 'B'

            if field[2][0] == field[2][1] == field[2][2] and field[2][0] != '-' :
                return 'A' if field[2][0] == 'x' else 'B'
            
            if field[0][0] == field[1][0] == field[2][0] and field[0][0] != '-' :
                return 'A' if field[0][0] == 'x' else 'B'

            if field[0][1] == field[1][1] == field[2][1] and field[0][1] != '-' :
                return 'A' if field[0][1] == 'x' else 'B'

            if field[0][2] == field[1][2] == field[2][2] and field[0][2] != '-' :
                return 'A' if field[0][2] == 'x' else 'B'
                
            if field[0][0] ==field[1][1] ==field[2][2] and field[0][0] != '-' :
                return 'A' if field[0][0] == 'x' else 'B'

            if field[2][0] == field[1][1] == field[0][2] and field[0][2] != '-' :
                return 'A' if field[0][2] == 'x' else 'B'
                    
            return None
                           
        for move in (moves) :
            field[move[0]][move[1]] = currMove
            if currMove == 'x':
                currMove = 'o'
            else :
                currMove = 'x'
            count += 1
            if count > 3:
                winner = getWinner()
                if winner :
                    return winner


            
        if len(moves) == 9:
            return "Draw"               
        return "Pending" 

solution = Solution()

res = solution.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]])
print(res)