import pytest
from click.testing import CliRunner

from cared_cli._cli import app, hello


def test_cli_app_no_args():
    """Test the app command without arguments."""
    runner = CliRunner()
    result = runner.invoke(app, prog_name="cared")
    assert result.exit_code == 0
    assert "Usage: cared" in result.output


def test_run_cli_app_unknown_command(monkeypatch, capsys):
    """Test running the app with subcommand.

    This covers the branch "ctx.invoked_subcommand is not None".
    """
    monkeypatch.setattr("sys.argv", ["cared", "hello"])
    with pytest.raises(SystemExit):
        app()
    captured = capsys.readouterr()
    assert "Hello" in captured.out


def test_hello_world():
    """Test the hello command with no arguments."""
    runner = CliRunner()
    result = runner.invoke(hello, [])
    assert result.exit_code == 0
    assert result.output == "Hello, world!\n"
