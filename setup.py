from setuptools import setup, find_packages

setup(
    name="rshanker779_common",
    version="0.1.0",
    author="rshanker779",
    author_email="rshanker779@gmail.com",
    description="Common utilities",
    python_requires=">=3.7",
    install_requires=[
        "black",
        "pre-commit~=2.2",
        "pytest>5.4,<6",
        "pytest-cov~=2.8",
        "snakeviz",
        "wheel>0.33",
    ],
    packages=find_packages(),
    extras_require={"docs": ["sphinx"]},
)
