from shared.types import Credential


class Insta:
    def __init__(self, credential: Credential) -> None:
        self.id = credential.id
        self.password = credential.password
