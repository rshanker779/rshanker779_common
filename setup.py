from setuptools import setup, find_packages

setup(
    name="rshanker779_common",
    version="0.0.1",
    author="rshanker779",
    author_email="rshanker779@gmail.com",
    description="Common utilities",
    python_requires=">=3.7",
    install_requires=["black", "pre-commit", "pytest"],
    packages=find_packages(),
    extras_require={"snakeviz": ["snakeviz"]},
)
