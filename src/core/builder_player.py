from root.registry import CLASSES
from core.unities.classes.characters import Characters

class PlayerBuilder:
    def __init__(self, data_player):
        self.data_player = data_player

    def generate_team(self):
        team = []

        for nums in self.data_player['party_actives']:
            if f'slot_{nums}' in self.data_player['party_members'] and self.data_player['party_members'][f'slot_{nums}']['type'] in CLASSES:
                hero = Characters(CLASSES[self.data_player['party_members'][f'slot_{nums}']['type']]())
                
                for attributes in hero.profile.attr.received:
                        hero.profile.attr.received[attributes] = self.data_player['party_members'][f'slot_{nums}']['attr']['received'][attributes]
                for keys in hero.profile.history:
                    for n, attributes in enumerate(hero.profile.history[keys]):
                        hero.profile.history[keys][attributes] = self.data_player['party_members'][f'slot_{nums}']['history'][keys][n]
                
                hero.profile.stats['level']['current'], hero.profile.stats['level']['exp'] = self.data_player['party_members'][f'slot_{nums}']['attr']['level']
                team.append(hero)
            else:
                 raise Exception(f"Slot {nums} is empty or the type of character is invalid")
        
        return team