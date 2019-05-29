from Link.DropGroupLinkModule import DropGroupLink
from Link.MathLinkModule import MathLink

def _load_drop_group(drop_group_def):
    return DropGroupLink(drop_group_def['groups'])

def _load_math(math_group_def):
    return MathLink(math_group_def['operation'])

def _load(link_def):
    link_type_switch = {
        'DropGroupLink': _load_drop_group,
        'MathLink': _load_math
    }
    return link_type_switch.get(link_def['type'])(link_def)