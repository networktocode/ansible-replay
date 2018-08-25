# Ansible Replay

<a href="https://travis-ci.org/ambv/black"><img alt="Build Status" src="https://travis-ci.org/ambv/black.svg?branch=master"></a>

Replay Ansible capture output.

* Free software: MIT license
* Documentation: (COMING SOON!) https://ansible-replay.readthedocs.org.

# Requirements

click

# Installation

installing Requirements

```
  $ pip install -r requirements.txt
```

```
  $ pip install .
```

ansible-replay is ready to run!

# Running

```
 $ ansible-replay sample.log
```

sample.log is the  that you capture from your ansible-playbook

```
  $ ansible-playbook sample_playbook.yml > sample.log
```

# Screencast

![Alt Text](data/ansible-replay.gif)
