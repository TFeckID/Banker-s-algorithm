def add_list(List_a,List_b):
    return list(map(lambda x:x[0]+x[1],list(zip(List_a,List_b))))

def minus_list(List_a,List_b):
    return list(map(lambda x:x[0]-x[1],list(zip(List_a,List_b))))


def compare_list(List_A,List_B):
    flag=0
    for i in range(len(List_A)):
        if List_A[i]>=List_B[i]:
            flag+=1
    return flag==len(List_A)

def SecurityCheck(List_Process,List_Available):
    List_Work=List_Available
    List_WorkAddAllocation=[0,0,0]
    SecurityQueue=[]
    for i in List_Process:
        i.finish=False
    print("Name       Work\t\tNeed\t    Allocation\tWork+Allocation\t  Finish")
    print("          A  B  C      A  B  C        A  B  C        A  B  C")
    for count in range(len(List_Process)):
        for i in List_Process:
            if  i.finish==False and compare_list(List_Work,i.List_need):
                List_WorkAddAllocation=add_list(List_Work,i.List_allocation)
                i.finish=True
                SecurityQueue.append(i.name)
                print(i.name,end='       ')
                print(List_Work,end='    ')
                print(i.List_need, end='      ')
                print(i.List_allocation, end='      ')
                print(List_WorkAddAllocation, end='        ')
                print(i.finish)
                #print(i.name)
                List_Work=List_WorkAddAllocation
                break
    if len(SecurityQueue)==len(List_Process):
        print("安全序列为",end=' ')
        print(SecurityQueue)
        return True
    else:
        return False