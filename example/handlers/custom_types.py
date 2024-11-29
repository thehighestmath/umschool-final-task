from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class Question:
    id: int
    text: str
