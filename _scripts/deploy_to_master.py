"""
deploy_to_master.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

from .increment_version import *
from izzy.io import Git


# Increment version; print out string
version = increment_version()
print('package version: {}\n'.format(version))

# Connect to git repository, tag, add files, commit, push
git = Git()
git.tag('v' + version)
git.add('-A')
git.commit(input('Commit message: '))
git.push(remote='origin', branch='master', options='--tags')

# TODO this merge broke the ability to run pypi deployment on travis-ci
