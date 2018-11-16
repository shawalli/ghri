#!/usr/bin/env python3
import json
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

from ghri.commands import list_releases, show_release
from ghri.output import set_log_level
import ghri


@click.group(cls=DYMGroup)
@click.option("-a", "--api-endpoint",
              metavar="URL",
              default=ghri.GITHUB_API_ENDPOINT,
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
@click.version_option()
@click.pass_context
def cli(ctx, **kwargs):
    """Display information about GitHub releases."""
    ghri.GITHUB_API_ENDPOINT = kwargs["api_endpoint"]
    ghri.GITHUB_TOKEN = kwargs["token"]


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
@click.option("--json", "json_output",
              default=False,
              is_flag=True,
              help=("Format output as JSON.")
              )
@click.pass_context
def list(ctx, repository, verbose, json_output):
    """List all releases for a GitHub project."""
    if json_output:
        set_log_level("error")

    result = list_releases(repository, verbose=verbose, json_output=json_output)
    if json_output is True and result is not False:
        set_log_level("info")
        logger.info(json.dumps(result))
        result = True

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
@click.option("--json", "json_output",
              default=False,
              is_flag=True,
              help=("Format output as JSON.")
              )
@click.pass_context
def show(ctx, repository, key, key_type, json_output):
    """Show information about KEY release."""
    if json_output:
        set_log_level("error")

    result = show_release(repository, key, key_type, json_output=json_output)
    if json_output is True and result is not False:
        set_log_level("info")
        logger.info(json.dumps(result))
        result = True

    exit_cli(result)


def exit_cli(command_result):
    exit_code = 0
    if not command_result:
        exit_code = 1
    sys.exit(exit_code)


if __name__ == "__main__":
    cli(obj=dict())
