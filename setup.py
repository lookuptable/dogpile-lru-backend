from setuptools import setup


install_requires = [
    "dogpile.cache",
    "lru-dict"
]

tests_require = [
    "pytest"
]

setup(
    install_requires=install_requires,
    test_suite="tests",
    tests_require=tests_require
)
