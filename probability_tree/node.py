from dataclasses import dataclass
from typing import List, Protocol


class Node(Protocol):
    """
    Protocol defining the interface of a node in a probability tree.
    """

    name: str
    probability: float

    @property
    def conclusion(self) -> float:
        ...


@dataclass
class LeafNode:
    """
    A leaf node in a probability tree.
    """

    name: str
    conclusion: float
    probability: float = 1.0


@dataclass
class BranchNode:
    """
    A branch node in a probability tree.
    """

    name: str
    children: List[Node]
    probability: float = 1.0

    @property
    def conclusion(self) -> float:
        return sum(child.conclusion * child.probability for child in self.children)
