import matplotlib.pyplot as plt
import numpy as np
from .io import MRIVolume

def _get_slice(volume: np.ndarray,
               axis: int,
               index: int | None):
    if index is None:
        index = volume.shape[axis] // 2

    if axis == 0:
        return volume[index, :, :], index
    elif axis == 1:
        return volume[:, index, :], index
    else:
        return volume[:, :, index], index

def show_slice(volume: MRIVolume,
               axis: int = 2,
               index: int | None = None,
               cmap="gray"):
    """Display a single MRI slice."""
    img, idx = _get_slice(volume.data, axis, index)

    plt.figure(figsize=(5, 5))
    plt.imshow(img.T, cmap=cmap, origin="lower")
    plt.axis("off")
    plt.title(f"Slice {idx} (axis={axis})")
    plt.show()

def show_slice_with_overlay(
    volume: MRIVolume,
    seg,
    axis: int = 2,
    index: int | None = None,
    alpha: float = 0.3,
):
    """Display MRI slice with segmentation mask overlayed."""
    seg_data = seg.data if isinstance(seg, MRIVolume) else seg

    img, idx = _get_slice(volume.data, axis, index)
    mask, _ = _get_slice(seg_data > 0, axis, index)

    plt.figure(figsize=(5, 5))
    plt.imshow(img, cmap="gray", origin="lower")

    rgba = np.zeros(mask.T.shape + (4,))
    rgba[mask.T] = [1, 0, 0, alpha]

    plt.imshow(rgba, origin="lower")
    plt.axis("off")
    plt.title(f"Slice {idx} (axis={axis})")
    plt.show()