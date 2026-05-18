import operator

def compare_attributes(param_a, signal, param_b):
    opm = {
    '==': operator.eq,
    '!=': operator.ne,
    '//': operator.floordiv,
    '<=': operator.le,
    '>=': operator.ge,

    'tr': operator.truth,

    '<': operator.lt,
    '-': operator.sub,
    '+': operator.add,
    '/': operator.truediv,
    '*': operator.mul,
    '>': operator.gt,

    'is': operator.is_,
    'is_not': operator.is_not,
    }

    return opm[signal](param_a, param_b)

def get_attributes(target, attribute_key):
    
    map = {
        'history': target.history,
        'static': target.static_stats,
        'action': target.action_stats,
        'main': target.main_stats,

        'status': target.status,
        'targets': target.targets,
        'allies': target.allies,
        'multipliers': target.multipliers,
        'data': target.user_data }
    
    attribute = map.get(attribute_key)
    
    if isinstance(attribute, dict):
        return attribute