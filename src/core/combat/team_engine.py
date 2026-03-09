

class TeamEngine:
    def __init__(self, team):
        self.team = team
    
        self.disponible_unities = []
        self.active_unities     = []
        self.offline_unities    = []
        

        self.active_unities_index = 0
        self.active_unity = None

    def prev(self, jump=0):
        """
            prev function navigate through active unities.
            Jump is used to skip unities; default Jump is zero.
        """
        if self.active_unities_index <= 0:
            self.active_unities_index = len(self.active_unities) - 1
        else:
            self.active_unities_index -= 1
        self.active_unities_index -= jump
        self.active_unity = self.active_unities[self.active_unities_index]

    def define(self):
        import random
        self.disponible_unities = self.team
        if self.active_unities == []:
            for i in range(3):
                j = random.choice(self.disponible_unities)
                if j not in self.active_unities:
                    self.active_unities.append(j) #! change this later
        
        for unities in self.disponible_unities:

            if unities not in self.active_unities:
                if unities not in self.offline_unities:
                    self.offline_unities.append(unities) 

    def next(self, jump=0):
        """
            next function navigate through active unities.
            Jump is used to skip unities; default Jump is zero.
        """
        if self.active_unities_index >= len(self.active_unities) - 1:
            self.active_unities_index = 0
            self.active_unity = self.active_unities[self.active_unities_index]
            return False
        else:
            self.active_unities_index += 1
        self.active_unities_index += jump
        self.active_unity = self.active_unities[self.active_unities_index]

    def reset(self):
        for unities in self.active_unities:
            unities.position = None
            
        self.active_unities_index = 0
        self.active_unities = []
        self.offline_unities = []
        self.active_unity = None
        print('Team successfully reseted')
