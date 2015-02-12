from setuptools import setup, find_packages

setup(
    name = "anime_recognizer",
    version = "1.0",
    packages = find_packages(),
    install_requires=[
        'numpy',
        'Pillow',
        'scikit-image',
        'cnn_anime',
        'Flask',
        'flask-babel'
    ],
    dependency_links=[
        'git+ssh://git@github.com/alexisvallet/cnn-anime.git#egg=cnn_anime'
    ]
)
