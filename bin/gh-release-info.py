import logging

from requests.compat import urljoin
import click
import click_log

# Import before importing any "internal" modules so that logging is configured
# consistently for all modules
logger = click_log.basic_config()
logger.setLevel(logging.INFO)

from gh_release_info_lib.commands import list_releases
import gh_release_info_lib


@click.group()
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
    list_releases(repository, verbose=verbose)


if __name__ == "__main__":
    cli(obj=dict())
