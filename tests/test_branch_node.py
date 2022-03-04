from probability_tree import BranchNode, LeafNode


def test_it_should_handle_one_leaf_node():
    node = BranchNode(
        name="root",
        probability=1.0,
        children=[
            LeafNode(
                name="leaf",
                conclusion=1.0,
                probability=1.0,
            ),
        ],
    )

    assert node.conclusion == 1.0


def test_it_handles_multiple_leaf_nodes():
    node = BranchNode(
        name="root",
        probability=1.0,
        children=[
            LeafNode(
                name="leaf1",
                conclusion=1.0,
                probability=0.5,
            ),
            LeafNode(
                name="leaf2",
                conclusion=0.0,
                probability=0.5,
            ),
        ],
    )

    assert node.conclusion == 0.5


def test_it_handles_a_single_branch_child():
    node = BranchNode(
        name="root",
        probability=1.0,
        children=[
            BranchNode(
                name="branch",
                probability=1.0,
                children=[
                    LeafNode(
                        name="leaf1",
                        conclusion=1.0,
                        probability=0.5,
                    ),
                    LeafNode(
                        name="leaf2",
                        conclusion=0.0,
                        probability=0.5,
                    ),
                ],
            ),
        ],
    )

    assert node.conclusion == 0.5


def test_it_handles_multiple_branch_children():
    node = BranchNode(
        name="root",
        probability=1.0,
        children=[
            BranchNode(
                name="branch1",
                probability=0.5,
                children=[
                    LeafNode(
                        name="leaf1",
                        conclusion=1.0,
                        probability=0.5,
                    ),
                    LeafNode(
                        name="leaf2",
                        conclusion=0.5,
                        probability=0.5,
                    ),
                ],
            ),
            BranchNode(
                name="branch2",
                probability=0.5,
                children=[
                    LeafNode(
                        name="leaf3",
                        conclusion=0.5,
                        probability=0.5,
                    ),
                    LeafNode(
                        name="leaf4",
                        conclusion=0.0,
                        probability=0.5,
                    ),
                ],
            ),
        ],
    )

    assert node.conclusion == 0.5
