import logging
import sys

from requests.compat import urljoin
import click
from click_didyoumean import DYMGroup
import click_log

# Import before importing any "internal" modules so that logging is configured
# consistently for all modules
logger = click_log.basic_config()
logger.setLevel(logging.INFO)

from gh_release_info_lib.commands import list_releases, show_release
import gh_release_info_lib


@click.group(cls=DYMGroup)
@click.option("-a", "--api-endpoint",
              metavar="URL",
              default=gh_release_info_lib.GITHUB_API_ENDPOINT,
              show_default=True,
              envvar="GITHUB_API_ENDPOINT",
              help=("GitHub API endpoint; may also be set with "
                    "GITHUB_API_ENDPOINT environmental variable. Note that "
                    "GitHub Enterprise API endpoints have a specific "
                    "format that is slightly different than the traditional "
                    "GitHub API endpoint.")
              )
@click.option("-t", "--token",
              metavar="TOKEN",
              required=True,
              envvar="GITHUB_TOKEN",
              help=("GitHub access token; may also be set with GITHUB_TOKEN "
                    "environmental variable.")
              )
@click.pass_context
def cli(ctx, **kwargs):
    gh_release_info_lib.GITHUB_API_ENDPOINT = kwargs["api_endpoint"]
    gh_release_info_lib.GITHUB_TOKEN = kwargs["token"]


@cli.command()
@click.option("-r", "--repository",
              metavar="OWNER/PROJECT",
              required=True,
              help="GitHub repository to query."
              )
@click.option("-v", "--verbose",
              default=False,
              is_flag=True,
              help="Display additional information about releases."
              )
@click.pass_context
def list(ctx, repository, verbose):
    """List all releases for a GitHub project."""
    result = list_releases(repository, verbose=verbose)

    exit_cli(result)


@cli.command()
@click.option("-r", "--repository",
              metavar="OWNER/PROJECT",
              required=True,
              help="GitHub repository to query."
              )
@click.argument("key")
@click.option("--key-type",
              type=click.Choice(["title", "tag"]),
              default="title",
              show_default=True,
              help="Type of key with which to query."
              )
@click.pass_context
def show(ctx, repository, key, key_type):
    """Show information about KEY release."""
    result = show_release(repository, key, key_type)

    exit_cli(result)


def exit_cli(command_result):
    exit_code = 0
    if not command_result:
        exit_code = 1
    sys.exit(exit_code)


if __name__ == "__main__":
    cli(obj=dict())
