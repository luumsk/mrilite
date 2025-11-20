import nibabel as nib
import numpy as np
from dataclasses import dataclass

@dataclass
class MRIVolume:
    """Basic container for MRI volume and metadata."""
    data: np.ndarray
    affine: np.ndarray | None = None
    header: nib.Nifti1Header | None = None
    voxel_sizes: np.ndarray | None = None
    orientation: np.ndarray | None = None
    axcodes: str | None = None
    path: str | None = None

def load_nifti(path: str) -> MRIVolume:
    """Load a NIfTI file and return an MRIVolume."""
    img = nib.load(path)
    return MRIVolume(
        data=img.get_fdata(dtype=np.float32),
        affine=img.affine,
        header=img.header,
        voxel_sizes=np.array(img.header.get_zooms()),
        orientation=nib.orientations.io_orientation(img.affine),
        axcodes=nib.orientations.aff2axcodes(img.affine),
        path=path,
    )

def save_nifti(volume: MRIVolume, path: str) -> None:
    """Save an MRIVolume to a NIfTI file."""
    img = nib.Nifti1Image(volume.data, volume.affine)
    nib.save(img, path)