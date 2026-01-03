"""
Minimal smoke tests for mrilite.viz.

These tests only verify that visualization functions run without crashing.
They do NOT check visual correctness.
"""

import numpy as np


def test_viz_functions_no_crash():
    """Smoke test: visualization functions should run without errors."""
    # Force headless backend BEFORE importing matplotlib.pyplot
    import matplotlib

    matplotlib.use("Agg")

    import matplotlib.pyplot as plt

    from mrilite.volume import MRIVolume
    from mrilite.viz import (
        show_slice,
        show_overlay,
        show_slice_with_mask,
        show_modalities,
    )

    # Dummy MRI data
    data = np.random.rand(10, 12, 8).astype(np.float32)
    mask = (data > 0.6).astype(np.uint8)

    volume = MRIVolume(
        data=data,
        affine=np.eye(4),
        header=None,
        voxel_sizes=np.array([1.0, 1.0, 1.0]),
        orientation=None,
        axcodes=None,
        path=None,
    )

    seg_volume = MRIVolume(
        data=mask,
        affine=np.eye(4),
        header=None,
        voxel_sizes=np.array([1.0, 1.0, 1.0]),
        orientation=None,
        axcodes=None,
        path=None,
    )

    # show_slice
    fig, ax = show_slice(volume, axis=2, index=3)
    plt.close(fig)

    # show_overlay
    fig, ax = show_overlay(volume, seg_volume, axis=2, index=3)
    plt.close(fig)

    # show_slice_with_mask (your highlighted function)
    fig, axes = show_slice_with_mask(volume, seg_volume, axis=2, index=3)
    plt.close(fig)

    # show_modalities
    fig, axes = show_modalities(
        {"T1": volume, "FLAIR": volume},
        axis=2,
        index=3,
    )
    plt.close(fig)