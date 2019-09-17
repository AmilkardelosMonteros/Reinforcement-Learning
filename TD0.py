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


class AgentTD0(Agent):
    '''
        Agente que calcula Vpi con TD0
    '''
    def TD0(self,action,iteraciones):
        self.update_dictionaries(0,'')
        action_X = action
        for x in range(iteraciones):
            is_done, new_state = self.update_dictionaries(action_X, 'X')
            if is_done:
                #Quiere decir que acabo el juego
                self.state = new_state
                state = self.state_to_base10(self.state)
                default = self.values.get(state)
                Vs = 0 if default == None else default
                Rt = recom(self.state)
                self.values[state] = Vs + self.alfa*(Rt -Vs)
                self.state = self.board.reset()
            else:
                #Quiere decir que no acaba el juego, tira O
                self.state = new_state
                Rt = recom(self.state)
                state = self.state_to_base10(self.state)
                default = self.values.get(state)
                Vs = 0 if default == None else default
                action_O = self.select_random_action('O')
                is_done, new_state = self.update_dictionaries(action_O, 'O')
                if is_done:
                     #Quiere decir acaba el juego 
                    Vs_prima = recom(new_state)*0.5
                    self.values[state] = Vs + self.alfa*(Rt + self.gamma*Vs_prima - Vs)
                    self.state = self.board.reset()
                else:
                    #Quiere decir que no acabo el juego, tira X
                    action_X = self.select_random_action('X')

    def num_to_matrix(self,num):
        x = self.state_to_matrix(self.base10_to_state(num))
        return x



player = AgentTD0()
player.TD0(8,1000)
player.TD0(1,1000)
print(player.values)
print(len(player.values))
