import os
import re
import setuptools

NAME = 'deco_helper'

meta_pattern = re.compile(r'__(\w+?)__\s*=\s*(.*)')


def set_metadata():
    meta = {}
    module_path = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(module_path, NAME, '__init__.py')) as meta_f:
        for line in meta_f:
            m = meta_pattern.match(line)
            if m:
                k, v = m.groups()
                meta.update({k: v.strip("\'")})

    return meta


metadata = set_metadata()

setuptools.setup(name=NAME,
                 version=metadata['version'],
                 author=metadata['author'],
                 author_email=metadata['contact'],
                 url=metadata['url'],
                 packages=setuptools.find_packages(exclude=['test*']),
                 # package_dir={'': 'package_dir'},
                 py_modules=['helpers'],
                 platforms=['any'],
                 install_requires=[],
                 python_requires='>=3.6',
                 description='Decorator Helper',
                 license='MIT'
                 )
