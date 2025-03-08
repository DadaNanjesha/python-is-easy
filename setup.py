from setuptools import setup, find_packages

setup(
    name="learn-python-easy",             
    version="1.0.0",                    
    author="Dada Nanjesha Gouda Shanbog",
    description="An interactive Streamlit app to help people learn Python easily",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DadaNanjesha/python-is-easy",  
    packages=find_packages(),            
    include_package_data=True,    
    install_requires=[
        "streamlit",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
