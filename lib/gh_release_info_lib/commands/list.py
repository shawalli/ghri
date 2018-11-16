import logging

from github import Github

from gh_release_info_lib import GITHUB_API_ENDPOINT, GITHUB_TOKEN
from gh_release_info_lib.output import print_wrapped
from gh_release_info_lib.schema import ReleaseSchema

logger = logging.getLogger(__name__)


def list_releases(repository, verbose=False):
    g = Github(base_url=GITHUB_API_ENDPOINT, login_or_token=GITHUB_TOKEN)

    releases = g.get_repo(repository).get_releases()
    if not releases:
        print_wrapped(
            "No releases found for project.", level="warning",
            logger=logger
        )
        return

    for release in releases:
        indent_level = 0

        release_structured = ReleaseSchema().dump(release)
        if not verbose:
            ReleaseSchema.print_short(release_structured.data, logger)
        else:
            ReleaseSchema.print_long(release_structured.data, logger)

    return True
