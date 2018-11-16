import logging

from github import Github

from gh_release_info_lib import GITHUB_API_ENDPOINT, GITHUB_TOKEN
from gh_release_info_lib.output import print_wrapped

logger = logging.getLogger(__name__)


def show_release(repository, key, key_type):
    g = Github(base_url=GITHUB_API_ENDPOINT, login_or_token=GITHUB_TOKEN)

    releases = g.get_repo(repository).get_releases()

    key_attr = "tag_name" if key_type == "tag" else key_type

    found_release = None
    for release in releases:
        value = getattr(release, key_attr)
        if value == key:
            found_release = release
            break

    if found_release is None:
        print_wrapped(
            "Could not find release with {key_type} of '{key}'".format(
                key_type=key_type,
                key=key
            ),
            logger=logger,
            level="error"
        )
        return False

    print_wrapped(
        "{title} ({tag})".format(
            title=found_release.title,
            tag=found_release.tag_name
        ),
        logger=logger
    )
    print_wrapped(
        "- Author: {name} ({email})".format(
            name=found_release.author.name,
            email=found_release.author.email
        ),
        logger=logger
    )
    print_wrapped(
        "- Created At: {}".format(found_release.created_at),
        logger=logger
    )
    print_wrapped(
        "- Published At: {}".format(found_release.published_at),
        logger=logger
    )
    print_wrapped(
        "- Commitish: {}".format(found_release.target_commitish),
        logger=logger
    )
    print_wrapped(
        "- Draft: {}".format(found_release.draft),
        logger=logger
    )
    print_wrapped(
        "- Pre-release: {}".format(found_release.prerelease),
        logger=logger
    )
    print_wrapped(
        "- Description:",
        logger=logger
    )
    print_wrapped(
        found_release.body,
        logger=logger,
        indent_level=2
    )

    return True
