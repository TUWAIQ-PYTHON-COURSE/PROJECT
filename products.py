
pid = 1
class product:
    
    def __init__(self ,p_name :str, p_price :int , p_des :str,quantity :int):
        global pid
        self.p_id = pid
        self.p_name = p_name 
        self.p_price = p_price
        self.p_des = p_des
        self.quantity = quantity
        pid +=1
    def info(self):
        print(f"           {self.p_id}               {self.p_name}       {self.p_price}RS        {self.p_des}")
    
    def manager_info(self):
        print(f"           {self.p_id}               {self.p_name}       {self.p_price}RS        {self.p_des}        {self.quantity}")



