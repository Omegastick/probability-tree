from dataclasses import dataclass
from typing import List, Protocol


class Node(Protocol):
    """
    Protocol defining the interface of a node in a probability tree.
    """

    name: str
    probability: float
    conclusion: float


@dataclass
class LeafNode:
    """
    A leaf node in a probability tree.
    """

    name: str
    probability: float
    conclusion: float


@dataclass
class BranchNode:
    """
    A branch node in a probability tree.
    """

    name: str
    probability: float
    children: List[Node]

    @property
    def conclusion(self) -> float:
        return sum(child.conclusion * child.probability for child in self.children)
