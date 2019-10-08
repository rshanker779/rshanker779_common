from setuptools import setup, find_packages

setup(
    name="rshanker779_common",
    version="1.0.0",
    author="rshanker779",
    author_email="rshanker779@gmail.com",
    description="Common utilities",
    python_requires=">=3.7",
    install_requires=["black", "pre-commit"],
    packages=find_packages(),
    test_suite="tests.utilities_test",
    extras_require={"snakeviz": ["snakeviz"]},
)
