
from setuptools import setup, find_packages

setup(
    name="custom_prediction_lib",
    version="0.3.0",
    packages=find_packages(),
    install_requires=[
        "scikit-learn",
        "optuna",
        "bayesian-optimization",
        "numpy",
        "pandas",
        "statsmodels",
        "bokeh",
    ],
    description="A custom prediction library with automated hyperparameter tuning, training utilities, exponential smoothing, and visualisation.",
    author="Your Name",
    author_email="your.email@example.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
