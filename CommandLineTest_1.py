import pytest
import subprocess

class CommandLineUtility:
    def __init__(self, cmd_name):
        self.cmd_name = cmd_name

    def run_command(self, options=None):
        if options is None:
            options = []
        command = [self.cmd_name] + options
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result

    def validate_command_name(self):
        return 5 <= len(self.cmd_name) <= 9

    def validate_options(self, options):
        if len(options) > 3:
            return False
        for option in options:
            if not option.startswith('-'):
                return False
            if '--' in option and len(option.split('=')) > 2:
                return False
            if any(char in option for char in '!@#$%^&*()+=[]{}|;:",<>?/'):
                return False
        return True

@pytest.fixture
def utility():
    return CommandLineUtility("testcmd")

def test_command_name_length(utility):
    assert utility.validate_command_name() == True

def test_command_with_no_options(utility):
    result = utility.run_command()
    assert result.returncode == 0
    assert "success" in result.stdout

def test_command_with_valid_options(utility):
    options = ["--option1", "--option2=value2", "-o"]
    assert utility.validate_options(options) == True
    result = utility.run_command(options)
    assert result.returncode == 0
    assert "success" in result.stdout
    assert "Value of option2 set successfully." in result.stdout

def test_command_with_invalid_options(utility):
    options = ["--option1", "--option2=value2", "-o", "--option3"]
    assert utility.validate_options(options) == False
    result = utility.run_command(options)
    assert result.returncode == 1
    assert "fail" in result.stdout

def test_command_with_special_characters(utility):
    options = ["--option1!", "--option2=value2@"]
    assert utility.validate_options(options) == False
    result = utility.run_command(options)
    assert result.returncode == 1
    assert "fail" in result.stdout

def test_command_with_too_many_options(utility):
    options = ["--option1", "--option2", "--option3", "--option4"]
    assert utility.validate_options(options) == False
    result = utility.run_command(options)
    assert result.returncode == 1
    assert "fail" in result.stdout