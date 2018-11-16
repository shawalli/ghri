##########################
ghri (GitHub Release Info)
##########################

CLI to display information about a GitHub project's releases.

********************
Installation & Usage
********************

.. code-block:: bash

    pip install ghri

or

.. code-block:: bash

    python setup.py install

The CLI can be run by invoking ``ghri``.

.. code-block:: bash

    Usage: ghri [OPTIONS] COMMAND [ARGS]...

    Display information about GitHub releases.

    Options:
    -a, --api-endpoint URL  GitHub API endpoint; may also be set with
                            GITHUB_API_ENDPOINT environmental variable. Note
                            that GitHub Enterprise API endpoints have a specific
                            format that is slightly different than the
                            traditional GitHub API endpoint.  [default:
                            https://api.github.com]
    -t, --token TOKEN       GitHub access token; may also be set with
                            GITHUB_TOKEN environmental variable.  [required]
    --version               Show the version and exit.
    --help                  Show this message and exit.

    Commands:
    list  List all releases for a GitHub project.
    show  Show information about KEY release.

**********************
Authorship and License
**********************

Written by Shawn Wallis and distributed under the MIT license.