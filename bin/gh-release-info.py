import logging

from requests.compat import urljoin
import click
import click_log

# Import before importing any "internal" modules so that logging is configured
# consistently for all modules
logger = click_log.basic_config()

from gh_release_info_lib.commands import list_releases

DEFAULT_GITHUB_API_ENDPOINT = "https://api.github.com"


@click.group()
@click.option("-a", "--api-endpoint",
              metavar="URL",
              default=DEFAULT_GITHUB_API_ENDPOINT,
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
    for key, value in kwargs.items():
        ctx.obj[key] = value


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
@click_log.simple_verbosity_option(logger)
def list(ctx, repository, verbose):
    """List all releases for a GitHub project."""
    endpoint = ctx.obj.get("api_endpoint")
    token = ctx.obj.get("token")

    list_releases(repository, token, endpoint, verbose=verbose)


if __name__ == "__main__":
    cli(obj=dict())
