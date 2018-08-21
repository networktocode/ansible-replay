from setuptools import setup, find_packages

setup(
    name='ansible-replay',
    version='0.1.0',
    description='A way to replay Ansible Playbook from an Ansible capture output',
    url='https://github.com/amb1s1/ansible-replay',
    py_modules=['replay'],
    author='David Gomez',
    author_email='amb1s1@gmail.com',
    license='MIT',
    install_requires=['Click'],
    entry_points={
        'console_scripts': [
            'ansible-replay=replay:replay',
        ]
    },
)
