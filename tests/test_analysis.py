import numpy as np
from mrilite.analysis import connected_components


def test_connected_components_two_objects():
    mask = np.zeros((10, 10, 10), dtype=np.uint8)

    mask[1:3, 1:3, 1:3] = 1
    mask[6:8, 6:8, 6:8] = 1

    labeled, n = connected_components(mask)

    assert n == 2
    assert labeled.shape == mask.shape


def test_connected_components_26_connectivity():
    mask = np.zeros((5, 5, 5), dtype=np.uint8)

    mask[2, 2, 2] = 1
    mask[3, 3, 3] = 1  # corner-touch only

    labeled, n = connected_components(mask)

    assert n == 1