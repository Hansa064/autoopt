from setuptools import setup, find_packages

setup(
    name="AutoOpt",
    version="0.1",
    requires=["hyperopt", "numpy"],
    desciption="Framework to automatically find and optimize the best processing pipeline for a given dataset",
    author="Torben Hansing",
    author_email="torbenhansing@gmail.com",
    url="https://github.com/hansa064/autoopt",
    packages=["autoopt"],
    platforms="any",
    extras_require={
        "plotting": ["matplotlib"],
        "tests": ["pytest"],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
)
