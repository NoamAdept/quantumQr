from setuptools import setup, find_packages

setup(
    name="quantumqr",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "qrcode[pil]",
        "qrcode-terminal",
        "requests",
        "opencv-python",
        "numpy",
        "pillow",
    ],
    entry_points={
        "console_scripts": [
            "quantumqr=quantumqr:cli",
        ],
    },
    author="Noam Yakar",
    author_email="noamykr@gmail.com",
    description="A powerful command-line QR code generator.",
    url="https://github.com/NoamAdept/quantumqr",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

