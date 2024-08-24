# encoding: utf-8
import click
import logging

import ckan.model as model

from typing import Any, Mapping

from ckan.plugins import toolkit


log = logging.getLogger(__name__)


_banner = """
****** Welcome to the FMLD shell ******

This session has some variables pre-populated:
  - app (FMLD Application object)
  - config (FMLD config dictionary)
  - model (FMLD model module to access the Database)
  - toolkit (FMLD toolkit module)
    """


def ipython(namespace: Mapping[str, Any], banner: str) -> None:
    import IPython
    from traitlets.config.loader import Config

    c = Config()
    setattr(c.TerminalInteractiveShell, "banner2", banner)

    IPython.start_ipython([], user_ns=namespace, config=c)


def python(namespace: Mapping[str, Any], banner: str) -> None:
    import code
    code.interact(banner=banner, local=namespace)


@click.command()
@click.help_option("-h", "--help")
@click.pass_context
def shell(ctx: click.Context):
    """Run an interactive IPython shell with the context of the
    FMLD instance.

    It will try to use IPython, if not installed it will callback
    to the default Python's shell.
    """

    namespace = {
        "app": ctx.obj.app._wsgi_app,
        "model": model,
        "config": ctx.obj.config,
        "toolkit": toolkit,
    }

    try:
        ipython(namespace, _banner)
    except ImportError:
        log.debug("`ipython` library is missing. Using default python shell.")
        python(namespace, _banner)
