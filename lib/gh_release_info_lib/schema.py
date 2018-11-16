from attrdict import AttrDict
from marshmallow import fields, post_dump, Schema

from gh_release_info_lib.output import print_wrapped


class AuthorSchema(Schema):
    name = fields.Str()
    email = fields.Str()


class ReleaseSchema(Schema):
    title = fields.Str()
    tag_name = fields.Str()
    author = fields.Nested(AuthorSchema)
    created_at = fields.Str()
    published_at = fields.Str()
    target_commitish = fields.Str()
    draft = fields.Str()
    prerelease = fields.Str()
    description = fields.Str(attribute="body")

    @post_dump
    def to_attrdict(self, data):
        return AttrDict(data)

    @staticmethod
    def print_short(data, logger, base_indent_level=0):
        print_wrapped(
            "* {title} ({tag})".format(title=data.title, tag=data.tag_name),
            logger=logger,
            indent_level=base_indent_level
        )

    @staticmethod
    def print_long(data, logger, base_indent_level=0):
        print_wrapped(
            "* {title} ({tag})".format(title=data.title, tag=data.tag_name),
            logger=logger,
            indent_level=base_indent_level
        )
        indent_level = base_indent_level + 1
        print_wrapped(
            "- Author:       {name} ({email})".format(
                name=data.author.name,
                email=data.author.email
            ),
            logger=logger,
            indent_level=indent_level
        )
        print_wrapped(
            "- Created At:   {}".format(data.created_at),
            logger=logger,
            indent_level=indent_level
        )
        print_wrapped(
            "- Published At: {}".format(data.published_at),
            logger=logger,
            indent_level=indent_level
        )
        print_wrapped(
            "- Commitish:    {}".format(data.target_commitish),
            logger=logger,
            indent_level=indent_level
        )
        print_wrapped(
            "- Draft:        {}".format(data.draft),
            logger=logger,
            indent_level=indent_level
        )
        print_wrapped(
            "- Pre-release:  {}".format(data.prerelease),
            logger=logger,
            indent_level=indent_level
        )
        if data.description == "":
            print_wrapped(
                "- Description:  <Empty>",
                logger=logger,
                indent_level=indent_level
            )
        else:
            print_wrapped(
                "- Description:",
                logger=logger,
                indent_level=indent_level
            )
            print_wrapped(
                data.description,
                logger=logger,
                indent_level=(indent_level + 2),
                subsequent_indent=False
            )