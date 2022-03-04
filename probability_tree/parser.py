from probability_tree.node import BranchNode, LeafNode, Node


def parse_dict(input: dict) -> Node:
    """
    Parse a dictionary representing a probability tree and return said tree.
    """
    try:
        if input.get("children") is None:
            return LeafNode(name=input["name"], probability=input["probability"], conclusion=input["conclusion"])
        return BranchNode(
            name=input["name"],
            probability=input["probability"],
            children=[parse_dict(child) for child in input["children"]],
        )
    except KeyError:
        raise ValueError(f"Malformed input: {input}")
