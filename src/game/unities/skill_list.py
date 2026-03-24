from core.skill_engines import *

def Pierce(user, target):
    for skills in user.COMBAT_PROFILE.skills:
        if skills.name == 'Pierce':
             skills.times_used += 1
    
    damage = (user.COMBAT_PROFILE.STRENGHT * 0.5) * user.COMBAT_PROFILE.OUTPUT_DAMAGE_MULTIPLIER
    doDamage(damage, target)

def EncourageSet(user):
        for targets in user.COMBAT_PROFILE.targets:
            if targets not in user.COMBAT_PROFILE.allies:
                user.COMBAT_PROFILE.targets.remove(targets)

def Encourage(user, target):
     for skills in user.COMBAT_PROFILE.skills:
          if skills.name == 'Encourage':
            if skills.last_time_used > 1:
                doHeal(10, target)
                target.COMBAT_PROFILE.OUTPUT_DAMAGE_MULTIPLIER += 0.5
                skills.last_time_used = 0
            else:
                doHeal(10, target)
                skills.last_time_used = 0


skill_list = {
    'Pierce': SkillEngine('Pierce', Pierce, None),
    'Encourage': SkillEngine('Encourage', Encourage, EncourageSet),
}