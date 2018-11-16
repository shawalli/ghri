import logging

from github import Github

from gh_release_info_lib import GITHUB_API_ENDPOINT, GITHUB_TOKEN
from gh_release_info_lib.output import print_wrapped

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
        print_wrapped(
            "* {title} ({tag})".format(title=release.title, tag=release.tag_name),
            logger=logger,
            indent_level=indent_level
        )
        indent_level += 1
        if verbose:
            print_wrapped(
                "- Author: {name} ({email})".format(
                    name=release.author.name,
                    email=release.author.email
                ),
                logger=logger,
                indent_level=indent_level
            )
            print_wrapped(
                "- Created At: {}".format(release.created_at),
                logger=logger,
                indent_level=indent_level
            )
            print_wrapped(
                "- Published At: {}".format(release.published_at),
                logger=logger,
                indent_level=indent_level
            )
            print_wrapped(
                "- Commitish: {}".format(release.target_commitish),
                logger=logger,
                indent_level=indent_level
            )
            print_wrapped(
                "- Draft: {}".format(release.draft),
                logger=logger,
                indent_level=indent_level
            )
            print_wrapped(
                "- Pre-release: {}".format(release.prerelease),
                logger=logger,
                indent_level=indent_level
            )
            print_wrapped(
                "- Description:",
                logger=logger,
                indent_level=indent_level
            )
            print_wrapped(
                release.body,
                logger=logger,
                indent_level=(indent_level + 2)
            )

    return True
