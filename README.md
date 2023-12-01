# Dental X-ray Analysis

![Project Status](https://img.shields.io/badge/Status-Under%20Development-red)
![Python application](https://github.com/NexusX12/Dental-X-ray-Analysis/actions/workflows/python-app.yml/badge.svg)
![GitHub Issues](https://img.shields.io/github/issues/NexusX12/Dental-X-ray-Analysis)
![GitHub License](https://img.shields.io/badge/license-MIT-blue)
![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

- [Dependencies](#dependencies)
- [Dataset structure](#dataset-structure)
- [Abstract](#abstract)
- [Introduction](#introduction)
- [Code Basis](#code-basis)
- [Installation](#installation)
- [Usage](#usage)
- [Future Work](#future-work)
- [Authors](#authors)
- [References](#references)
- [Conclusion](#conclusion)
- [License](#license)

## Dependencies

[Download data](https://www.kaggle.com/datasets/imtkaggleteam/dental-radiography/data)

## Dataset structure

The dataset should be arranged in a structured fashion, as the following:

```
unlabeled_images/
	- 0001_jpg.rf.30a42966fb9c51553f6949b70234218d.jpg
	- 0001_jpg.rf.57229a11e925669019e179341e22c97a.jpg
	- 0001_jpg.rf.f94abcb7858bb419a7202ef60ef95bd6.jpg
	- ......
	- 1000_jpg.rf.c9dd4b2cf2f9c945b8d1921990531852.jpg
_annotations.csv
train.py
tooth_segmentation.py
```

## Abstract

This project aims to develop a tool for dental X-ray analysis using computer vision techniques. The primary objective is to segment and identify teeth in panoramic X-ray images, providing a foundation for future applications in dental diagnosis and treatment planning. The project is currently under development, and this document outlines the basis of the code, its underlying ideas, and how to use the tool.

## Introduction

Dental X-rays are essential for diagnosing and treating various dental conditions. Automating the analysis of X-ray images can significantly aid dental professionals in their decision-making processes. This project leverages computer vision, specifically image segmentation, to identify and mark teeth in panoramic X-ray images.

## Code Basis

The project consists of two main scripts:

### Script 1: Dental X-ray Classification

- **Objective**: Train a machine learning model to classify dental conditions based on annotated X-ray images.
- **Implementation**: Utilizes a Random Forest classifier to predict dental conditions (e.g., Fillings, Impacted Tooth, Implant).
- **Usage**:
  - Modify the threshold value in `create_teeth_mask` function for optimal segmentation.
  - Train the model using annotated data in the `_annotations.csv` file.
  - Save the trained model as a pickle file using `train.py`.

### Script 2: Tooth Segmentation and Boundary Drawing

- **Objective**: Segment individual teeth and draw boundaries around them in a given X-ray image.
- **Implementation**: Applies adaptive thresholding and contour detection to identify teeth regions and draw rectangles around them.
- **Usage**:
  - Adjust the `threshold_value` parameter in the `draw_tooth_boundaries` function for optimal segmentation.
  - Provide an input X-ray image to visualize tooth boundaries.

## Installation

To run the scripts, follow these installation steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/NexusX12/Dental-X-ray-Analysis
   ```

2. cd Dental-X-ray-Analysis:
   ```bash
   cd Dental-X-ray-Analysis
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

**Script 1: Dental X-ray Classification**

```bash
 python train.py
```

This script will generate `trained_model.pkl` in current directory.

**Script 2: Tooth Segmentation and Boundary Drawing**

Make sure the `trained_model.pkl` is in the same directory.

```bash
 python tooth_segmentation.py
```

![screenshot 1](/screenshots/screenshot1.png "Output classifying the Dental X-rays")
![screenshot 2](/screenshots/screenshot2.png "Output zoomed-in to the classification")
![screenshot 3](/screenshots/screenshot3.png "Output zoomed 300%")

## Future Work

This project is currently under development, and future work will focus on:

- Refining segmentation techniques for improved accuracy.
- Integrating deep learning approaches for more sophisticated tooth detection.
- Developing a user-friendly interface for easy adoption by dental professionals.

## Authors

- [Tharun Birla](https://github.com/tharunbirla)

## References

1. scikit-learn: Machine Learning in Python. [https://scikit-learn.org/](https://scikit-learn.org/)
2. OpenCV: Open Source Computer Vision Library. [https://opencv.org/](https://opencv.org/)
3. NumPy: The fundamental package for scientific computing with Python. [https://numpy.org/](https://numpy.org/)
4. Pandas: Powerful data structures for data analysis. [https://pandas.pydata.org/](https://pandas.pydata.org/)

## Conclusion

Dental X-ray analysis through computer vision holds great promise for enhancing dental diagnosis and treatment planning. This project provides a foundation for further research and development in this domain.

**Note: This project is under active development, and contributions are welcome. Please check the repository for updates and improvements.**

## License

- The MIT License (MIT) Copyright (c) 2018 École Polytechnique, Université de Montréal
- Dataset - [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
