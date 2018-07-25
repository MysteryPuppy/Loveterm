import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='loveterm',
     description='A terminal package for LDR couples',
     author='lovebirdnest',
     author_email='sadpastelcutie@gmail.com',
     version='0.4',
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/lovebirdsnest/LoveTerm.git",
     scripts=['loveterm','README.md','LICENSE','requirements.txt'],
     packages=setuptools.find_packages(),
     classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ),
 )
