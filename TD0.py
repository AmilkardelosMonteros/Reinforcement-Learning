from agent import Agent
from board import TicTacToe
def recom(x):
    if x[0]==x[1]==x[2]==1:
        return 1
    elif x[3]==x[4]==x[5]==1:
        return 1
    elif x[6]==x[7]==x[8]==1:
        return 1
    elif x[0]==x[3]==x[6]==1:
        return 1
    elif x[1]==x[4]==x[7]==1:
        return 1
    elif x[2]==x[5]==x[8]==1:
        return 1
    elif x[0]==x[4]==x[8]==1:
        return 1
    elif x[2]==x[4]==x[6]==1:
        return 1
    elif x[0]==x[1]==x[2]==2:
        return -1
    elif x[3]==x[4]==x[5]==2:
        return -1
    elif x[6]==x[7]==x[8]==2:
        return -1
    elif x[0]==x[3]==x[6]==2:
        return -1
    elif x[1]==x[4]==x[7]==2:
        return -1
    elif x[2]==x[5]==x[8]==2:
        return -1
    elif x[0]==x[4]==x[8]==2:
        return -1
    elif x[2]==x[4]==x[6]==2:
        return -1
    else:
        return 0

    def num_to_matrix(self,num):
        x = self.state_to_matrix(self.base10_to_state(num))
        return x
    
    def TD1(self,n):
        self.values[self.key] = 0
        reflected = False
        rots = 0
        for _ in range(n):
            is_done, new_key, reflected, rots = self.update_dicts(reflected, rots, 'X')
            self.key = self.reset_key() if is_done else new_key
            state = self.base10_to_state(new_key)
            default = self.values.get(new_key)
            Vs = 0 if default == None else default
            print(state)
            if is_done:
                Rt = recom(state)
                self.values[new_key] = Vs + self.alfa*(Rt -Vs)
                reflected, rots = self.reset_rr()
            else:
                is_done, new_key, reflected, rots = self.update_dicts(reflected, rots, 'O')
                self.key = self.reset_key() if is_done else new_key
                default = self.values.get(new_key)
                Rt_mas_uno = recom(self.base10_to_state(new_key)) 
                Vs_prima = 0 if default == None else default
                self.values[new_key] = Vs + self.alfa*(Rt_mas_uno + self.gamma*Vs_prima - Vs)
                if is_done:
                    reflected, rots = self.reset_rr()
        self.key = self.reset_key()
    



