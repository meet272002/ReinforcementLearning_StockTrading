from setuptools import setup, find_packages

setup(
    name='gym_anytrading',
    version='1.0.0',
    packages=find_packages(),
    author='Meet',
    author_email='....',
    license='....',
    install_requires=[
        'gymnasium>=0.29.1',
        'numpy>=1.16.4',
        'pandas>=0.24.2',
        'matplotlib>=3.1.1',
        'seaborn>=0.13.2'
    ],
    package_data={
        'gym_anytrading': ['datasets/data/*']
    }
)
