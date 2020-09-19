#place your SODUKU in the "ex" variable. make sure to put a 0 in the emty places at the soduku
#every list in the "ex" variable should represent a row in the SODUKU
ex = [[0,0,0,4,6,0,0,3,0],[9,8,0,0,5,1,6,7,2],[0,1,3,2,8,0,0,0,0],[1,0,0,0,0,3,2,0,4],[0,0,5,1,2,0,3,0,0],[8,0,0,0,4,0,0,5,7],[0,0,0,6,9,0,4,1,0],[4,2,9,0,0,0,0,0,3],[0,6,1,7,0,4,0,0,0]]
def soduku(table):
    



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
    a = (i+1)%3
    b = (j+1)%3
    print(a)
    print(b)
    if a == 0:
        index1.append(i-2)
        index1.append(i)
    if b == 0:
        index2.append(j-2)
        index2.append(j)
    if a == 1:
        index1.append(i-1)
        index1.append(i+1)
    if b == 1:
        index2.append(j-1)
        index2.append(j+1)
    if a == 2:
        index1.append(i)
        index1.append(i+2)
    if b == 2:
        index2.append(j)
        index2.append(j+2)
    print(index1)    
    print(index2)
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
#This is the main function of the program: it returns all the possibilites of (i)
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
    soduku(ex)    
