# AI Cloud and Cloud-Shadow Detection – NRSC (ISRO Challenge)
# Overview
Developed a satellite image processing pipeline using spectral band normalization and rule-based segmentation. Generated GeoTIFF outputs for accurate cloud and cloud-shadow mapping in remote sensing datasets.

This project focuses on detecting clouds and cloud shadows in satellite imagery using image processing and rule-based segmentation techniques. The system processes remote sensing data to generate GeoTIFF outputs for cloud and shadow mapping, which can assist in Earth observation analysis and environmental monitoring.

# Objective

Detect clouds and cloud shadows in satellite imagery.
Process multispectral satellite images using spectral band normalization.
Generate geospatial outputs for further remote sensing analysis.

# Tools & Technologies

Python, OpenCV, Jupyter Notebook, rioxarray, NumPy, GeoTIFF format

# Methodology
1. Data Processing
Loaded satellite imagery using rioxarray.
Extracted relevant spectral bands for analysis.

2. Spectral Band Normalization
Applied normalization techniques to enhance satellite image features.
Improved visibility of cloud and shadow regions.

3. Rule-Based Segmentation
Used thresholding and rule-based segmentation to classify:
  -Cloud pixels
  -Cloud shadow pixels
  -Background regions

4. Cloud and Shadow Detection
Applied image processing operations using OpenCV to refine segmentation results.

5. Output Generation
Generated GeoTIFF files representing detected clouds and shadows.
These outputs can be used in GIS and remote sensing tools.

# Project Workflow

Load satellite image dataset
Preprocess and normalize spectral bands
Apply segmentation rules
Detect cloud and shadow regions
Export results as GeoTIFF files

# Results

Successfully detected cloud and shadow regions from satellite images.
Generated geospatial outputs suitable for remote sensing applications.

# Applications

Satellite image preprocessing
Environmental monitoring
Climate research
Remote sensing data analysis
Future Improvements
Integrate machine learning models for improved segmentation
Use deep learning (CNN/U-Net) for automated cloud detection
Deploy as a cloud-based satellite image analysis tool

# Author
-Vyshnavi Katasani
