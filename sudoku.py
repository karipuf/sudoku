from copy import deepcopy

def ValidSolutions(smat,i,j):
    '''
    Returns valid solutions for row i, col j of a matrix smat
    matrix is zero indexed, values are 1-9
    zero value indicates that this square is still vacant
    '''
    
    # Setup
    possibleSols=[True]*10

    # Across rows and columns
    for tmp in range(9):
        possibleSols[smat[tmp][j]]=False
        possibleSols[smat[i][tmp]]=False
    
    # In the box
    for row in [3*(i/3)+tmp for tmp in range(3)]:
        for col in [3*(j/3)+tmp for tmp in range(3)]:
            possibleSols[smat[row][col]]=False

    return [tmp for tmp in range(1,10) if possibleSols[tmp]]

def SolveSudoku(smat):

    # Search for a single unfilled square
    for i in range(9):
        for j in range(9):

            if smat[i][j]==0:                
                sols=ValidSolutions(smat,i,j)
                if len(sols)==0:
                    # i.e. no feasible solution
                    return -1
                
                for sol in sols:
                    newsmat=deepcopy(smat)
                    newsmat[i][j]=sol
                    res=SolveSudoku(newsmat)
                    if type(res)==int:
                        # Means solution doesn't work
                        # since failed solution returns -1
                        pass
                    else:
                        # Solved!
                        return res

                # No solution found on this branch
                return -1
                    
    # i.e. all elements are present
    # either you provided a completed puzzle
    # or puzzle solved! ;-)
    return smat
        
# Sample solution
smat=[[2,0,0,5,6,9,0,0,4],
[0,0,8,0,0,3,2,6,0],
[0,6,0,0,0,0,0,5,1],
[8,0,3,0,0,4,0,7,0],
[7,0,2,0,0,0,5,0,6],
[0,4,0,2,0,0,8,0,3],
[4,8,0,0,0,0,0,1,0],
[0,5,7,1,0,0,9,0,0],
[1,0,0,8,9,7,0,0,5]]
