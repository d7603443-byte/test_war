import random

class Card:
    def __init__(self):
        self.list_packet = ["2c","3c","4c","5c","6c","7c","8c","9c","10c","jc","qc","kc","ac","2d","3d","4d","5d","6d","7d","8d","9d","10d","jd","qd","kd","ad","2s","3s","4s","5s","6s","7s","8s","9s","10s","js","qs","ks","as","2h","3h","4h","5h","6h","7h","8h","9h","10h","jh","qh","kh","ah"]
           
    def mix(self):
        for i in range(1000):
            random.shuffle(self.list_packet)
        # print(self.list_packet)

    def packets(self):
        player_packet = self.list_packet[:26]
        computer_packet = self.list_packet[26:]
        return player_packet, computer_packet


class Player:
    def __init__(self, name):
        self.name = name
        

    # def show(self):
        
        # = card().packets()
        
class Game:
    def __init__(self,name):
        self.name = name
        pass

    def ply(self):
        self.winer = ""
        list_player, list_computer = Card().packets()
    

        self.guess1 = list_computer.pop()
        self.guess2 = list_player.pop()
    
        
        if self.guess1 > self.guess2:
            list_player.append(self.guess1)
            list_player.append(self.guess2)
            self.winer = self.name
        elif self.guess2 < self.guess1:
            list_computer.append(self.guess1)
            list_computer.append(self.guess2)
            self.winer = "computer"
        else:
            return False
        print ({self.name},":",{self.guess1},". computer:",{self.guess2}, ".  winer:", {self.winer})







    
    


    



# Player("david").p_show()
# a.p_show()
