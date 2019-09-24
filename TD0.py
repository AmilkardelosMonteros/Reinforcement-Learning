from agent import Agent
from board import TicTacToe


class AgentTD0(Agent):
    '''
        Agente que calcula Vpi con TD0
    '''

    def V(self,s):
        default = self.values.get(s)
        Vs = 0 if default == None else default
        return Vs

    def aux(self,x,y,z):
        self.values[x] = self.V(x) + self.alfa*(y + self.gamma*self.V(z) - self.V(x))
        
    def paso(self):
        estados = [ ]
        rewards =  [ ]
        self.values[self.key] = 0
        reflected = False
        rots = 0
        while True:
            is_done, new_key, reflected, rots ,reward = self.update_dicts(reflected, rots, 'X')
            self.key = self.reset_key() if is_done else new_key
            estados.append(new_key)
            rewards.append(reward)
            if is_done: 
                reflected, rots = self.reset_rr()
                break
            else:
                is_done, new_key, reflected, rots, reward= self.update_dicts(reflected, rots, 'O')
                self.key = self.reset_key() if is_done else new_key
                estados.append(new_key)
                rewards.append(reward)
                if is_done:
                    reflected, rots = self.reset_rr()
                    break
        self.key = self.reset_key()
        estados.append(0)
        rewards.append(0)
        return estados,rewards

    def num_to_matrix(self,num):
        x = self.state_to_matrix(self.base10_to_state(num))
        return x

    
    def actualiza(self,x,y):
        for i in range(len(x)-1):
            St,Rt,St_prima = x[i],y[i],x[i+1]
            self.aux(St,Rt,St_prima)
            
    def TD0(self,n):
        for _ in range(n):
            x,y = self.paso()
            self.actualiza(x,y)
    
        

     
    



