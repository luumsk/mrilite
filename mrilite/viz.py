import matplotlib.pyplot as plt
import numpy as np
from .volume import MRIVolume

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

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(img, cmap=cmap, origin="lower")
    ax.axis("off")
    ax.set_title(f"Slice {idx} (axis={axis})")
    return fig, ax

def show_overlay(
    volume: MRIVolume,
    seg: MRIVolume,
    axis: int = 2,
    index: int | None = None,
    alpha: float = 0.3,
):
    """Display an MRI slice with a segmentation mask overlay."""
    seg_data = seg.data if isinstance(seg, MRIVolume) else seg

    img, idx = _get_slice(volume.data, axis, index)
    mask, _ = _get_slice(seg_data > 0, axis, index)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(img, cmap="gray", origin="lower")

    rgba = np.zeros(mask.shape + (4,))
    rgba[mask] = [1, 0, 0, alpha]

    ax.imshow(rgba, origin="lower")
    ax.axis("off")
    ax.set_title(f"Slice {idx} (axis={axis})")
    return fig, ax


def show_slice_with_mask(
    volume: MRIVolume,
    seg: MRIVolume,
    axis: int = 2,
    index: int | None = None,
):
    """Display MRI slice and segmentation mask side by side."""
    seg_data = seg.data if isinstance(seg, MRIVolume) else seg

    img, idx = _get_slice(volume.data, axis, index)
    mask, _ = _get_slice(seg_data > 0, axis, index)

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].imshow(img, cmap="gray", origin="lower")
    axes[0].axis("off")
    axes[0].set_title(f"MRI Slice {idx} (axis={axis})")

    axes[1].imshow(mask, cmap="gray", origin="lower")
    axes[1].axis("off")
    axes[1].set_title(f"Segmentation Mask {idx} (axis={axis})")

    return fig, axes

def show_modalities(
    volumes: dict[str, MRIVolume],
    axis: int = 2,
    index: int | None = None,
    cmap="gray"
):
    """Display slices from multiple MRI modalities side by side."""
    n_modalities = len(volumes)
    fig, axes = plt.subplots(1, n_modalities, figsize=(5 * n_modalities, 5))

    for i, (modality, volume) in enumerate(volumes.items()):
        img, idx = _get_slice(volume.data, axis, index)

        axes[i].imshow(img, cmap=cmap, origin="lower")
        axes[i].axis("off")
        axes[i].set_title(f"{modality} Slice {idx} (axis={axis})")

    return fig, axes