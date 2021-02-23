from dataclasses import dataclass


@dataclass
class User:
    token: str
    username: str
    id: int
