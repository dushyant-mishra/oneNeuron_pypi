import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "oneNeuron_pypi"
USER_NAME = "dushyant-mishra"

setuptools.setup(
    name=f"{PROJECT_NAME}-{USER_NAME}",
    version="0.0.3",
    author=USER_NAME,
    author_email="dushyant.mishra@gmail.com",
    description="This project is an implementation of a simple perceptron",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "matplotlib==3.5.1",
        "numpy==1.21.5",
        "pandas==1.3.5",
        "joblib==1.1.0",
        "tqdm"
    ] #dependencies   
)