from setuptools import setup, find_packages

setup(
    name="ldms_sample_dashboard",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "ipywidgets>=7.6.0",
        "matplotlib>=3.4.0",
        "numpy>=1.20.0",
        "pandas>=1.2.0",
        "ipython>=7.0.0",
    ],
    description="A simple IPython widget dashboard with static data",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/ldms_sample_dashboard",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)