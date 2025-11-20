# mrilite

**mrilite** is a lightweight Python toolkit for handling 3D MRI volumes.  
It provides simple and minimal utilities for:

- loading and saving NIfTI files  
- basic preprocessing (z-score normalization)  
- visualizing MRI slices  
- overlaying segmentation masks  

Designed to be small, dependency-light, and easy to reuse across many MRI projects.


## Installation

Using `pip`:
```bash
pip install mrilite
```

Or install locally:

```bash
pip install -e .
```

## Quick Start

```python
from mrilite import load_nifti, zscore, show_slice_with_overlay

vol = load_nifti("t1.nii.gz")
seg = load_nifti("seg.nii.gz")

vol = zscore(vol)

show_slice_with_overlay(vol, seg, axis=2, index=80)
```

## Features

- Minimal and clean API
- Works with any 3D/4D NIfTI MRI
- Transparent segmentation overlay
- Only essential dependencies (`numpy`, `nibabel`, `matplotlib`)

## License

MIT License.