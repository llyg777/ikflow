from setuptools import setup

setup(
    name="ikflow",
    version="0.0.0",
    author="Jeremy Morgan",
    author_email="jsmorgan6@gmail.com",
    packages=[],
    scripts=[],
    url="http://pypi.python.org/pypi/ikflow/",
    license="LICENSE.txt",
    description="An awesome package that does something",
    long_description=open("README.md").read(),
    install_requires=["kinpy", "klampt", "torch", "pytorch-lightning", "FrEIA", "tensorboard", "wandb", "black"],
    include_package_data=True,
    package_data={"": ["model_descriptions.yaml"]},
)
