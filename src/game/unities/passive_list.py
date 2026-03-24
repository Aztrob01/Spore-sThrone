from core.skill_engines import PassiveEngine


def gobpsv(user):
        if user.context.get_hitted:
            if user.context.aggressor not in user.context.allies:
                user.context.aggressor.CURRENT_HP -= int(user.COMBAT_PROFILE.STRENGHT * 0.2)
                user.context.passive_times_used += 1
def d01psv(user):
        pass

def w01psv(user):
        pass

def m01psv(user):
        pass


passive_list = {
    'd01': PassiveEngine('Angarde', d01psv),
    'w01': PassiveEngine('w01psv', w01psv),
    'm01': PassiveEngine('m01psv', m01psv),
    'Goblin': PassiveEngine('Contra Attack', gobpsv)
}