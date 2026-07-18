class Brain:
    def __init__(self):
        self.default = { 'agressivity': 0, 'inteligence': 0, 'conditions': { } }
        
        self.user = None
        self.agressivity = 0
        self.inteligence = 0
        self.conditions  = { }

    def load_default(self, user):
        self.user = user
        self.agressivity, self.inteligence = user['origin'].data['brain']['default']
        self.conditions = user.data['brain']['conditions']

    def limit(self, pers_limits=False, new_limits=[10, 10]):
        if pers_limits:
            pass #! not ready yet
        else:
            self.agressivity = min(10, self.agressivity)
            self.inteligence = min(10, self.inteligence)

    def verify_condition(self, condition):
        if self.conditions.get(condition, False) is False:
            return False
        
        from new.root.op_keys import op_keys

        atr, ope, val = self.conditions.get(condition)[0]
        return op_keys[ope](atr, val)

    def apply_math(self, math):
        from new.root.op_keys import op_keys

        atr, ope, val = math
        if atr == 'agressivity':
            self.agressivity = op_keys[ope](self.agressivity, val)
        else:
            self.inteligence = op_keys[ope](self.inteligence, val)

    def apply_conditions(self):
        for conds in self.conditions:
            if self.verify_condition(conds):
                self.apply(self.conditios[conds][1])

    def apply_status(self):
        status = self.user['profile'].data['status']

        for sts in status:
            if sts.main.get('brain', False) is not False:
                for items in sts.main['brain']:
                    self.apply_math(items)

    def sort_skill(self):
        import random, math
        
        skill = []
        for sk in self.user.main['profile'].data['skills']:
            if sk.can_use:
                skill.append(sk)

        prob = [[0.05, 0.1, 0.2, 0.6], [0.05, 0.2, 0.7], [0.15, 0.8], [0.95]]
        prob = prob[len(skill) - 1]

        # euclidean sort
        skill.sort(key=lambda x : math.dist((x.main['brain'][0], x.main['brain'][1]), (self.agressivity, self.inteligence)), reverse=True)
        
        selected = None
        rand = random.uniform(0, 1)
        for num, chances in enumerate(prob):
            if chances <= rand:
                selected = skill[num]
                print('Selected skill:', selected.main['name'])
        
        if selected is None:
            selected = self.user.main['origin'].data['skilltree']['default']['fallback']
            print('Fallback skill:', selected.main['name'])

        return selected
    

    def think(self):
        
        skills = self.user.main['profile'].data['skills']
        
    
        self.apply_conditions()
        self.apply_status()
        self.limit()
        self.sort_skill()


