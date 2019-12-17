
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
        print(cmd)
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

    def push(self, remote='origin', branch='master', options=''):
        self._execute('git push {0} {1} {2}'.format(options, remote, branch))

    def tag(self, tag):
        self._execute('git tag {}'.format(tag))

    def which(self):
        self._execute('where git')


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
test()

# Increment version and print out string
version = increment_version()
print(version + '\n')

# Connect to git repository, tag, add files, commit, push
git = Git()
git.tag('v' + version)
git.add('-A')
git.commit(input('Commit message: '))
git.push(remote='origin', branch='master', options='--tags')
