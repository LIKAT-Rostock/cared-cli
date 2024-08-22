"""
Commands to be run with the duty command runner.

For more see https://pawamoy.github.io/duty/
"""

import webbrowser
from pathlib import Path

from duty import duty, tools

open_browser = tools.lazy(webbrowser.open, name="open_browser")


@duty(aliases=["cov"])
def coverage(ctx) -> None:
    """Run pytest under coverage and create html report."""
    ctx.run(
        "python -m coverage run -p -m pytest".split(" "),
        title="Run pytest under coverage.",
    )
    # Working with duty.tools.coverage does not work, why?
    #   ctx.run(tools.coverage.combine(), title="Combine coverage data.", silent=True)
    ctx.run(
        "python -m coverage combine --quiet".split(" "), title="Combine coverage data."
    )
    ctx.run(
        "python -m coverage html --skip-empty".split(), title="Produce html report."
    )
    html_report = Path(".htmlcov/index.html").absolute().as_uri()
    ctx.run(
        open_browser(html_report, new=2),
        title="Open report in browser.",
    )
