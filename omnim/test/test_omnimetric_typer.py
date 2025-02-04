from typer.testing import CliRunner

from omnim.src.cli.app import app

runner = CliRunner()


class TestOmniMetricCommandLineAppTyper:
    def test_has_default_help_message(self):
        master_output = """Usage: main [OPTIONS]

Options:
  --config-file PATH
  --metrics [lt|df|cfr|mttr]
  --input-file PATH
  --source TEXT
  --fetch TEXT"""

        result = runner.invoke(app, ["main", "--help"])

        assert master_output in result.stdout

    def test_has_default_help_message_without_arguments(self):
        master_output = """Usage: main [OPTIONS]

Options:
  --config-file PATH
  --metrics [lt|df|cfr|mttr]
  --input-file PATH
  --source TEXT
  --fetch TEXT"""

        result = runner.invoke(app)

        assert master_output in result.stdout

    def test_should_raise_error_for_invalid_metric_type(self):
        wrong_metric = "whatever"
        master_output = (
            f"Error: Invalid value for '--metrics': '{wrong_metric}' "
            f"is not one of 'lt', 'df', 'cfr', 'mttr'"
        )

        result = runner.invoke(app, ["main", "--metrics", wrong_metric])

        assert master_output in result.stdout

    def test_should_raise_error_for_invalid_file_path(self):
        wrong_path = "./wrong_file_path.csv"
        master_output = (
            f"Error: Invalid value for '--input-file': "
            f"Path '{wrong_path}' does not exist."
        )

        result = runner.invoke(app, ["--metrics", "lt", "--input-file", wrong_path])

        assert master_output in result.stdout
