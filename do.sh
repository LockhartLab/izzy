git filter-branch -f --env-filter "
    GIT_AUTHOR_NAME='doclockh'
    GIT_AUTHOR_EMAIL='chris@lockhartlab.org'
    GIT_COMMITTER_NAME='doclockh'
    GIT_COMMITTER_EMAIL='chris@lockhartlab.org'
  " HEAD
