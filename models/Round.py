class Rounds:
    def __init__(self, name, matchs):
        self.name = name
        self.matchs = matchs

    def serialize(self):
        matchs = []
        for m in self.matchs:
            matchs.append(
                [
                    [m[0][0].serialize(), m[0][1]],
                    [m[1][0].serialize(), m[1][1]]
                ]
            )
        return {
            'name': self.name,
            'matchs': matchs
        }
