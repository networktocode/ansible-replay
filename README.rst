===============================
Ansible Replay
===============================

.. image:: https://img.shields.io/travis/amb1s1/ansible-replay.svg
        :target: https://travis-ci.org/amb1s1/ansible-replay

.. image:: https://img.shields.io/pypi/v/ansible-replay.svg
        :target: https://pypi.python.org/pypi/ansible-replay


Replay Ansible capture output.

* Free software: MIT license
* Documentation: (COMING SOON!) https://ansible-replay.readthedocs.org.

Requirements
------------

click

Installation
------------

installing Requirements

.. code-block:: bash

  $ pip install -r requirements.txt

.. code-block:: bash

  $ pip install .

ansible-replay is ready to run!

Running
-------

.. code-block:: bash

 $ ansible-replay sample.log

sample.log is the  that you capture from your ansible-playbook

.. code-block:: bash

  $ ansible-playbook sample_playbook.yml > sample.log

