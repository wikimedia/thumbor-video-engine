# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='wikimedia_thumbor_video_engine',
    version='0.1.1',
    url='https://github.com/wikimedia/thumbor-video-engine',
    license='MIT',
    author='Gilles Dubuc, Wikimedia Foundation',
    description='Thumbor video engine',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'thumbor',
        'wikimedia_thumbor_base_engine'
    ],
    extras_require={
        'tests': [
            'pyvows',
            'coverage',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
