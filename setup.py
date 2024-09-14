from setuptools import setup, find_packages

setup(
    name='csv_viz',
    version='0.1.0',
    description='A CSV visualization tool with Seaborn plots and GUI using PyQt5',
    author='Chandrasekar SUBRAMANI NARAYANA',
    author_email='chandrasekarnarayana@gmail.com',
    url='https://github.com/chandrasekarnarayana/CSV_VIZ',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.3.0',
        'matplotlib>=3.4.0',
        'seaborn>=0.11.2',
        'PyQt5>=5.12',
    ],
    entry_points={
        'console_scripts': [
            'csv_viz=csv_viz.main_window:run_app',
        ],
    },
)
