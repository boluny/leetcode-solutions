# leetcode-solutions 

[![Build Status](https://travis-ci.com/boluny/leetcode-solutions.svg?branch=bolun-personal)](https://travis-ci.com/boluny/leetcode-solutions)

## How to contribute 

**One question one file**, name convention is `[question no]-[short url].py`.

Take question 1 for example, URL is (https://leetcode.com/problems/two-sum/)[https://leetcode.com/problems/two-sum/], so name is `1-two-sum.py`.

Remember to write test cases in each file, name convention is `test_xxx`, you can specify whatever name with `xxx`.

Recommended steps to follow:

1. Create new branch: `git checkout master -b [branch_name]`
2. Modify and submit your change. 
3. Checkout to `master` branch and rebase: `git checkout master && git rebase master [branch_name]`
4. Resolve conflicts and push to remote: `git push --set-upstream origin [branch_name]`
5. Raise `Pull Request` on repository page from your branch to master and wait for approval.

## How to run tests

Change directory to the root directory of this repo where you can find `pytest.ini` in the same level and run following command:

```bash
pytest
```

You should find following output:

    $ pytest
    ==================================== test session starts ====================================
    platform win32 -- Python 3.5.2, pytest-4.0.1, py-1.7.0, pluggy-0.8.0
    rootdir: E:\py_proj\leetcode-solutions, inifile: pytest.ini
    collected 1 item

    python\1-two-sum.py .                                                                  [100%]

    ================================= 1 passed in 0.04 seconds ==================================


## Dependent Python package
- pytest


## Expectation

We can work on it continuously and communicate with each other in time.

Thoughts and hints are welcome as comment in code file.

