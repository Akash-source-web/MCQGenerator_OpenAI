from setuptools import find_packages,setup

setup(
    name= 'McqGeneratorLLM',
    version= '0.0.1',
    author='Akash Kundu',
    author_email= 'akundu151@gmail.com',
    install_requires = ["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)