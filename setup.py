from setuptools import setup, find_packages

setup(
    name="notion_indexer",
    version="0.1.0",
    author="Joe",
    author_email="joseribeiro1017@gmail.com",
    packages=find_packages(),
    description="A simple notion indexer.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/joe-stifler/notion_indexer",
    zip_safe=True,
    license='MIT',
    include_package_data=True,
    install_requires=[
        'pandas',
        'notion-client',
        'scikit-learn',
    ],
)
