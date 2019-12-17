"""
deploy_to_master.py
written in Python3
author: C. Lockhart
"""


from izzy.io import Git

import yaml


# Helper function to increment the package version
# noinspection PyShadowingNames
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


# Increment version; print out string
version = increment_version()
print('package version: {}\n'.format(version))

# Connect to git repository, tag, merge (if necessary), add files, commit, push
git = Git()
git.checkout('master')
git.tag('v' + version)
git.merge('dev')
git.add('-A')
git.commit(input('Commit message: '))
git.push(remote='origin', branch='master', options='--tags')
