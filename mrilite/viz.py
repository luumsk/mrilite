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
    plt.imshow(img, cmap=cmap, origin="lower")
    plt.axis("off")
    plt.title(f"Slice {idx} (axis={axis})")
    plt.show()

def show_slice_with_mask_overlay(
    volume: MRIVolume,
    seg: MRIVolume,
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

    rgba = np.zeros(mask.shape + (4,))
    rgba[mask] = [1, 0, 0, alpha]

    plt.imshow(rgba, origin="lower")
    plt.axis("off")
    plt.title(f"Slice {idx} (axis={axis})")
    plt.show()


def show_slice_with_mask_side_by_side(
    volume: MRIVolume,
    seg: MRIVolume,
    axis: int = 2,
    index: int | None = None,
):
    """Display MRI slice and segmentation mask side by side."""
    seg_data = seg.data if isinstance(seg, MRIVolume) else seg

    img, idx = _get_slice(volume.data, axis, index)
    mask, _ = _get_slice(seg_data > 0, axis, index)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap="gray", origin="lower")
    plt.axis("off")
    plt.title(f"MRI Slice {idx} (axis={axis})")

    plt.subplot(1, 2, 2)
    plt.imshow(mask, cmap="gray", origin="lower")
    plt.axis("off")
    plt.title(f"Segmentation Mask {idx} (axis={axis})")

    plt.show()

def show_slice_of_all_modalities(
    volumes: dict[str, MRIVolume],
    axis: int = 2,
    index: int | None = None,
    cmap="gray"
):
    """Display slices from multiple MRI modalities side by side."""
    n_modalities = len(volumes)
    plt.figure(figsize=(5 * n_modalities, 5))

    for i, (modality, volume) in enumerate(volumes.items()):
        img, idx = _get_slice(volume.data, axis, index)

        plt.subplot(1, n_modalities, i + 1)
        plt.imshow(img, cmap=cmap, origin="lower")
        plt.axis("off")
        plt.title(f"{modality} Slice {idx} (axis={axis})")

    plt.show()