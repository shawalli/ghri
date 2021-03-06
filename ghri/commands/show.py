import logging

from github import Github

from ghri.output import print_wrapped
from ghri.schema import ReleaseSchema
import ghri

logger = logging.getLogger(__name__)


def show_release(repository, key, key_type, json_output=False):
    g = Github(
        base_url=ghri.GITHUB_API_ENDPOINT,
        login_or_token=ghri.GITHUB_TOKEN
    )

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

    release_structured = ReleaseSchema().dump(release)
    ReleaseSchema.print_long(release_structured.data, logger)

    if json_output:
        return release_structured.data
    else:
        return True
