import timeit

ex = [[0,0,1,0,0,9,0,0,0],[4,0,9,1,7,0,0,0,2],[0,3,5,0,4,8,1,0,0],[9,0,6,0,0,0,3,7,0],[1,0,0,7,3,6,4,0,9],[3,0,0,9,8,2,0,0,0],[0,0,0,0,2,7,0,0,4],[6,9,4,0,1,3,0,5,7],[0,7,2,0,0,0,0,0,0]]
hard = [[0,0,0,0,7,0,0,4,1],[0,0,0,0,0,9,0,0,0],[3,0,0,5,0,1,0,9,2],[0,0,1,0,8,0,0,6,0],[0,0,0,0,0,7,0,0,0],[0,0,7,6,0,0,0,0,4],[0,9,6,8,0,0,7,0,0],[2,0,0,0,0,5,0,3,0],[0,0,0,0,9,0,0,2,0]]
hard2 = [[6,0,0,0,0,3,0,9,0],[0,5,0,6,0,1,8,0,0],[0,0,0,0,9,7,0,0,1],[3,0,0,0,0,0,0,0,0],[0,0,5,9,0,6,0,4,0],[0,4,0,1,0,0,0,0,0],[8,3,0,0,0,0,9,0,0],[0,0,0,0,2,0,6,0,8],[0,0,9,0,0,0,0,5,3]]
expert = [[6,0,0,7,1,0,0,0,2],[3,0,0,0,0,0,0,9,6],[8,0,0,0,0,0,0,0,5],[0,0,9,0,0,0,0,0,0],[0,0,0,0,0,0,4,2,9],[0,7,0,8,0,0,0,0,0],[0,0,0,0,0,3,0,5,0],[1,3,0,0,0,7,0,0,0],[0,2,0,0,5,4,0,0,0]]
#those are examples i used to check my program. if you want to try it just make a variable with your soduku and change the variable at the __main__ fonction

def soduku(table,i,j,key):
    k=1
    print_table(table)
    #print(i,j)
    if table[i][j]!=0 and k!=0:
        #print('there is already a number')
        #input(str(i)+' , '+str(j))
        if (j+1)!=9 and k!=0:
            soduku(table,i,j+1,1)
        if (j+1)==9 and k!=0:
            soduku(table,i+1,0,1)
        if (i+1)==9 and (j+1)==9 :
            k=0
            return 0      
    if table[i][j]==0 and k!=0:
        #input(str(i)+' , '+str(j))
        poss = possibilities(table,i,j)
        #print(poss)
        if len(poss)==0:
            #print('this is the key' + str(key))
            #print('contraduction')
            return 0
        if len(poss)==1:
            table[i][j]=poss[0]
            #print('this is the key' + str(key))
            #print('there is only one value we use it' + str(table[i][j]))
            if (j+1)!=9 and k!=0:
                soduku(table,i,j+1,1)
            if (j+1)==9 and k!=0:
                soduku(table,i+1,0,1)
            if (i+1)==9 and (j+1)==9 :
                k=0
                return 0
            if k!=0:
                table[i][j] = 0                
        if len(poss)>1:
            #main boocle for    
            for p in poss :
                #print('this is the key' + str(key))
                table[i][j]=p
                #print('changing value' + str(table[i][j]))
                if (j+1)!=9 and k!=0:
                    soduku(table,i,j+1,1)
                if (j+1)==9 and k!=0:
                    soduku(table,i+1,0,1)
                if (i+1)==9 and (j+1)==9 :
                    k=0
                    return 0
            #if there is a contraduction and we finish all the possibilities we reset the value to 0       
            if k!=0:
                table[i][j] = 0        
    if k==0:
        if i==0 and j==0:
            print_table(table)
        return 0    


#fonction that make your table into a matrice
def print_table(table):
    for i in range(len(table)):
        a = ''
        for j in range(len(table[i])):
            a = a + str(table[i][j])+'  '
            if ((j+1)%3)==0:
                a = a+'|' 
        print(a)
        if ((i+1)%3)==0:
            print('______________________________')
#fonction that returns all the numbers in the square near (i,j)
def square(table,i,j):
    index1 = []
    index2 = []
    result = []
    a = (i+4)%3
    b = (j+4)%3
    if a == 0:
        index1.append(i-2)
        index1.append(i)
    if b == 0:
        index2.append(j-2)
        index2.append(j)
    if a == 1:
        index1.append(i)
        index1.append(i+2)      
    if b == 1:
        index2.append(j)
        index2.append(j+2)
    if a == 2:
        index1.append(i-1)
        index1.append(i+1)
    if b == 2:
        index2.append(j-1)
        index2.append(j+1)
 
    for p in range(index1[0],index1[1]+1):
        for t in range(index2[0],index2[1]+1):
            if (p!=i or t!=j) and table[p][t]!=0:
                result.append(table[p][t])
    return result
#fonction that returns all the numbers in the horizontal line that(i,j) in
def hori(table,i,j):
    result = []
    for t in range(9):
        if t!=i:
            if table[t][j]!=0:
                result.append(table[t][j])
    return result            
#fonction that returns all the numbers in the vertical line that(i,j) in
def verti(table,i,j):
    result = []
    for t in range(9):
        if t!=j:
            if table[i][t]!=0:
                result.append(table[i][t])
    return result            
#This is the main function of the program: it returns all the possibilites of (i,j)
def possibilities(table,i,j):
    a = square(table,i,j)
    b = hori(table,i,j)
    c = verti(table,i,j)
    result = list(dict.fromkeys(a + b + c))
    final_result = []
    for i in range(1,10):
        if i not in result:
            final_result.append(i)        
    return final_result


if __name__ == "__main__":
    start = timeit.default_timer()
    soduku(ex,0,0,1)
    #print_table(ex)
    stop = timeit.default_timer()
    print('Time: ', stop - start)      
