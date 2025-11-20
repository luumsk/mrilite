import numpy as np
from .io import MRIVolume

def zscore(volume: MRIVolume) -> MRIVolume:
    """Apply z-score normalization to MRI intensities."""
    data = volume.data
    mask = np.isfinite(data)

    mean = data[mask].mean()
    std = data[mask].std() + 1e-8

    norm = (data - mean) / std
    return MRIVolume(
        norm,
        affine=volume.affine,
        header=volume.header,
        voxel_sizes=volume.voxel_sizes,
        orientation=volume.orientation,
        axcodes=volume.axcodes,
        path=volume.path,
    )