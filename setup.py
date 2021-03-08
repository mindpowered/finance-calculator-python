import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='mindpowered-financecalculator',
    version='0.0.2',
    author="Mind Powered Corporation",
    author_email="support@mindpowered.dev",
    license="MIT",
    url="https://mindpowered.dev/",
    description="Financial calculations such as Net Present Value, Present Value, Future Value",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['financecalculator'],
    packages=['mindpowered_financecalculator'],
    package_dir={'mindpowered_financecalculator': 'wrappers'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'mindpowered-maglev',
    ],
)
