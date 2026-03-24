class SkillEngine:
    def __init__(self, name, active, rule):
        self.name   = name
        self.active = active
        self.rule   = rule

        self.times_used = 0
        self.last_time_used = 0

    def set(self, user):
        if self.rule is not None:
            self.rule(user)

    def use(self, user, target):
        self.active(user, target) # Use -> SKill or BA -> DoDamage or DoHeal

# ---------------------------------------------

class PassiveEngine:
    def __init__(self, name, passive):
        self.name    = name
        self.passive = passive

    def active(self, user):
        self.passive(user)

# ------------------------------------
    
    #TODO passive.set() para settar as regras da passiva, como os alvos
        #TODO passive.use() para usar a passiva após a aplicação das regras
        # * o mesmo deve servir como regra para as skills que curam aliados
        # * ou possuem condições especificas 
        # skills database

# ---------------------------------------------

def doDamage(amount, target): # simple damage
    target.CURRENT_HP -= amount

def doHeal(amount, target): # simple heal
    target.CURRENT_HP += amount

#TODO COMPOSED DAMAGE
#TODO COMPOSED TARGET

