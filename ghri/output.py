from textwrap import wrap
import logging


def set_log_level(level):
    level = level.upper()

    log_level = getattr(logging, level)

    logging.root.setLevel(level)
    for logger in logging.Logger.manager.loggerDict.values():
        if not isinstance(logger, logging.PlaceHolder):
            logger.setLevel(level)


def wrap_text(text, indent_level=0, subsequent_indent=True):
    indent = '  ' * indent_level
    subs_indent = indent
    if subsequent_indent:
        subs_indent = '  ' * (indent_level + 1)

    return wrap(text, width=80, initial_indent=indent,
                subsequent_indent=subs_indent, break_long_words=True,
                break_on_hyphens=True
                )


def print_wrapped(text, logger, level="info", indent_level=0,
                  subsequent_indent=True):
    level = level.lower()

    log_func = getattr(logger, level)

    for split_line in text.split("\n"):
        if split_line == "":
            log_func("")
            continue

        formatted_lines = wrap_text(split_line, indent_level=indent_level,
                                    subsequent_indent=subsequent_indent
                                    )

        for formatted_line in formatted_lines:
            log_func(formatted_line)
