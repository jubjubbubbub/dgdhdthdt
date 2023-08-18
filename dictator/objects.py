class Identifier:
    pass


class CharacterName(Identifier):
    def __init__(self, name: str) -> None:
        self.name = name


class GameUsername(Identifier):
    def __init__(self, username: str) -> None:
        self.username = username


class PlayerID(Identifier):
    def __init__(self, id: int) -> None:
        self.id = id


class InvalidUsernameFormat(TypeError):
    pass
