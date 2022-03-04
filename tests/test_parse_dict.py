from probability_tree import BranchNode, LeafNode, parse_dict


def test_it_parses_leaf_node():
    tree = parse_dict({"name": "leaf", "probability": 1.0, "conclusion": 1.0})
    assert tree == LeafNode(name="leaf", probability=1.0, conclusion=1.0)


def test_it_parses_simple_tree():
    tree = parse_dict(
        {
            "name": "root",
            "probability": 1.0,
            "children": [
                {"name": "leaf1", "probability": 0.5, "conclusion": 1.0},
                {"name": "leaf2", "probability": 0.5, "conclusion": 0.0},
            ],
        }
    )
    assert tree == BranchNode(
        name="root",
        probability=1.0,
        children=[
            LeafNode(name="leaf1", probability=0.5, conclusion=1.0),
            LeafNode(name="leaf2", probability=0.5, conclusion=0.0),
        ],
    )


def test_it_parses_complex_tree():
    tree = parse_dict(
        {
            "name": "root",
            "probability": 1.0,
            "children": [
                {
                    "name": "branch1",
                    "probability": 0.5,
                    "children": [
                        {"name": "leaf1", "probability": 0.5, "conclusion": 0.5},
                        {"name": "leaf2", "probability": 0.5, "conclusion": 0.0},
                    ],
                },
                {
                    "name": "branch2",
                    "probability": 0.5,
                    "children": [
                        {"name": "leaf1", "probability": 0.5, "conclusion": 1.0},
                        {"name": "leaf2", "probability": 0.5, "conclusion": 0.5},
                    ],
                },
            ],
        }
    )
    assert tree == BranchNode(
        name="root",
        probability=1.0,
        children=[
            BranchNode(
                name="branch1",
                probability=0.5,
                children=[
                    LeafNode(name="leaf1", probability=0.5, conclusion=0.5),
                    LeafNode(name="leaf2", probability=0.5, conclusion=0.0),
                ],
            ),
            BranchNode(
                name="branch2",
                probability=0.5,
                children=[
                    LeafNode(name="leaf1", probability=0.5, conclusion=1.0),
                    LeafNode(name="leaf2", probability=0.5, conclusion=0.5),
                ],
            ),
        ],
    )
