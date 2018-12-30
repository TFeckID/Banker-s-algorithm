from Function import compare_list
from Function import SecurityCheck

class Process(object):
    def __init__(self,name,List_max,List_allocation,List_Available):
        self.name=name
        self.List_max=List_max
        self.List_allocation=List_allocation
        self.List_need=[0,0,0]
        self.finish=False
        for i in range(3):
            self.List_need[i]=self.List_max[i]-self.List_allocation[i]
            List_Available[i]=List_Available[i]-self.List_allocation[i]


    def request(self,List_request,List_Available,List_Process):
        if compare_list(self.List_need,List_request):
            if compare_list(List_Available,List_request):
                for p in range(3):
                    List_Available[p]-=List_request[p]
                    self.List_allocation[p]+=List_request[p]
                    self.List_need[p]-=List_request[p]
                if SecurityCheck(List_Process,List_Available):
                    return True
                else:
                    for i in range(3):
                        List_Available[i]+=List_request[i]
                        self.List_allocation[i]-=List_request[i]
                        self.List_need[i]+=List_request[i]
                        print("安全性检查不通过")
                        return False
            else:
                print("可分配资源不足")
                return False
        else:
            print("超过最大需求数")
            return False