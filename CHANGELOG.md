# Changelog

All notable changes to this project will be documented in this file.


## [0.1.2] – 2026-01-03

### Added
- Visualization utilities for 3D MRI data:
  - `show_slice`
  - `show_overlay`
  - `show_slice_with_mask`
  - `show_modalities`
- Minimal but robust test suite for:
  - I/O (`load_nifti`, `save_nifti`)
  - Preprocessing (`zscore`)
  - Analysis (connected components)
  - Visualization (no-crash smoke tests)

### Fixed
- Fixed import behavior so users can use:
  ```python
  from mrilite import load_nifti
  ```