import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mp3_playlist",
    version="0.1",
    author="Fernando de Francisco (@ferdef)",
    author_email="fdfdev@outlook.com",
    keywords="mp3 m3u playlist",
    description="A small mp3 playlist generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ferdef/mp3_playlist",
    license="GNU GPLv3",
    packages=setuptools.find_packages(),
    classifiers=[]
)
