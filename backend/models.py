from dataclasses import dataclass

@dataclass
class User():
    name: str

@dataclass
class Task():
    id: int
    title: str
    assignee: User


