from Link.LinkModule import Link

class DropGroupLink(Link):
    def __init__(self, groups):
        self.groups = groups

    def _process(self, survey):
        survey_groups = survey["questionGroup"]
        for group in self.groups:
            del survey_groups[group]
        return survey
    
    def _dump(self):
        return {'type': 'DropGroupLink', 'groups': self.groups}