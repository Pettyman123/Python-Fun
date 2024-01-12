matrix =[
    [1 , -2 , 1],
    [1 , 0 , -1],
    [-1 , 2 , 1]
    ]

matrix2 =[
    [2 , 7 , 6],
    [9 , 5 , 1],
    [4 , 3 , 8]
    ]

def is_magic_matrix(l:list):
    temp_list =[]
    #horizantal_sum =[]
    #diagonal_sum =[]
    #vertical_sum =[]
    
    for i in range(3):
        hori_sum = l[i][0] + l[i][1] + l[i][2]
        #horizantal_sum.append(hori_sum)
        temp_list.append(hori_sum)
        verti_sum = l[0][i] + l[1][i] + l[2][i]
       #vertical_sum.append(verti_sum)
        temp_list.append(verti_sum)
    
    
    dia_sum=l[0][0] + l[1][1] + l[2][2]
    #diagonal_sum.append(dia_sum)
    temp_list.append(dia_sum)
    #print("The vertical sum: ", vertical_sum)
    #print("The horizantal sum: ",horizantal_sum)
    #print("The diagonal sum: ",diagonal_sum)
    #print(temp_list)
    temp_set = set(temp_list)
    if len(temp_set)==1:
        print("T") 
    else:
        print("F")

is_magic_matrix(matrix)
is_magic_matrix(matrix2)