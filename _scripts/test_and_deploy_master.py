<<<<<<< HEAD
#!/bin/bash

# Run tests
python -m izzy/tests/test.py || exit



# current commit
commit=$(git log --format="%H" -n 1)
echo "current commit=${commit}"

# checkout git master
#git checkout -qf master
git checkout new
git merge -s ours "$commit"

# configure git
git config --global user.name "travis"
git config --global user.email "travis"

# increment version
version=$(python _scripts/increment_version.py)

# update git tag


# upload to git without triggering TravisCI again
cat version.yml
git add version.yml
git add izzy/_version.py
git add docs/build/*
git add docs/source/api/generated/*
git commit -m "updating docs and version [ci skip]"
git merge master
git push -fq https://doclockh:"${GIT_API_KEY}"@github.com/"${TRAVIS_REPO_SLUG}".git master
=======

from izzy.tests import test

import subprocess
import yaml


# Class to help with git version control
class Git:
    # Initialize version of Git class
    def __init__(self, cwd='.'):
        """
        
        Parameters
        ----------
        cwd
        """
        self.cwd = cwd

    def _execute(self, cmd):
        subprocess.Popen(cmd, cwd=self.cwd, shell=True).wait()

    def add(self, filename):
        """


        Parameters
        ----------
        filename

        Returns
        -------

        """
        self._execute('git add {}'.format(filename))

    def commit(self, message=''):
        self._execute('git commit -m "{}"'.format(message))

    def push(self, remote='origin', branch='master'):
        self._execute('git push {0} {1}'.format(remote, branch))


# Helper function to increment the package version
def increment_version():
    # Read in version
    with open('version.yml', 'r') as f:
        version = yaml.safe_load(f.read())

    # Update patch
    version['patch'] += 1

    # Output version
    with open('version.yml', 'w') as f:
        yaml.safe_dump(version, f)

    # Transform version dict to string
    version = '.'.join([str(version[key]) for key in ['major', 'minor', 'patch']])

    # Write version string to izzy/_version.py
    with open('izzy/_version.py', 'w') as f:
        f.write("__version__ = '{}'\n".format(version))

    # Return
    return version


# Run tests; (script will stop if test fails)
# test()

# Print out version string
# version = increment_version()
# print(version + '\n')

# TODO Update git tag

# Connect to git repository
git = Git()

# Add our files to the repository
files = [
    'version.yml',
    'izzy/_version.py',
    'docs/build/*',
    'docs/source/api/generated/*'
]
for file in files:
    git.add(file)

# Commit
git.commit(input('Commit message: '))

# Push
git.push('origin', 'master')
>>>>>>> 7ad5a27... test
