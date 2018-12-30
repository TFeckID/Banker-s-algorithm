from Process import Process
from Process import SecurityCheck

List_Available = [10, 5, 7] #系统总资源

#进程集合
List_Process=[Process("P0", [7, 5, 3], [0, 1, 0], List_Available),
              Process("P1", [3, 2, 2], [2, 0, 0], List_Available),
              Process("P2", [9, 0, 2], [3, 0, 2], List_Available),
              Process("P3", [2, 2, 2], [2, 1, 1], List_Available),
              Process("P4", [4, 3, 3], [0, 0, 2], List_Available)]

print("T0时刻：")
if SecurityCheck(List_Process,List_Available):
    print("系统安全",end='\n\n')
    print("P1请求资源[1,0,2]:")
    if List_Process[1].request([1, 0, 2], List_Available, List_Process):
        print("分配成功", end='\n\n')
    else:
        print("分配失败", end='\n\n')
    print("P4请求[1,1,0]:")
    if List_Process[4].request([1, 1, 0], List_Available, List_Process):
        print("分配成功", end='\n\n')
    else:
        print("分配失败", end='\n\n')
    print("P4请求[3,3,0]:")
    if List_Process[4].request([3, 3, 0], List_Available, List_Process):
        print("分配成功", end='\n\n')
    else:
        print("分配失败", end='\n\n')
    print("P0请求[0,2,0]:")
    if List_Process[0].request([0, 2, 0], List_Available, List_Process):
        print("分配成功", end='\n\n')
    else:
        print("分配失败", end='\n\n')
else:
    print("系统不安全",end='\n\n')




