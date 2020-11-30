from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="vpype-text",
    version="0.1.0",
    description="",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Antoine Beyeler",
    url="",
    license=license,
    packages=["vpype_text"],
    install_requires=[
        'click',
        'vpype',
        'axi @ git+https://github.com/fogleman/axi',
    ],
    entry_points='''
            [vpype.plugins]
            text=vpype_text.vpype_text:vpype_text
        ''',
)
