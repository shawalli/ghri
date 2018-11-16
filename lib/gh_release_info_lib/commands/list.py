import logging

from github import Github

from gh_release_info_lib import GITHUB_API_ENDPOINT, GITHUB_TOKEN
from gh_release_info_lib.output import print_wrapped
from gh_release_info_lib.schema import ReleaseSchema

logger = logging.getLogger(__name__)


def list_releases(repository, verbose=False, json_output=False):
    g = Github(base_url=GITHUB_API_ENDPOINT, login_or_token=GITHUB_TOKEN)

    releases = g.get_repo(repository).get_releases()
    if not releases:
        print_wrapped(
            "No releases found for project.",
            logger=logger,
            level="warning"
        )

        if json_output:
            return {'releases': list()}
    else:
        structured_releases = list()
        for release in releases:
            release_structured = ReleaseSchema().dump(release)
            structured_releases.append(release_structured.data)
            if not verbose:
                ReleaseSchema.print_short(release_structured.data, logger)
            else:
                ReleaseSchema.print_long(release_structured.data, logger)

        if json_output:
            return {'releases': structured_releases}

    return True
