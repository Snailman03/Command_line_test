import pytest
import re

from CommandLineClass import CommandLine


@pytest.fixture
def return_command_line_obj():
    input_command_name = input("Input command name = \n")
    input_options_list = input("Input options with space = \n ").split()
    cmd_instance = CommandLine(input_command_name, *input_options_list)

    return cmd_instance


def test_cmd_details(return_command_line_obj):
    current_cmd_obj = return_command_line_obj
    current_cmd_obj.print_command_details()
    assert isinstance(current_cmd_obj, CommandLine)


def test_cmd_details_2():
    cmd_obj_1 = CommandLine("Test1", "-f", "--f")
    cmd_details_2_res = cmd_obj_1.print_command_details()
    assert cmd_details_2_res == "Test1"
    assert isinstance(cmd_obj_1, CommandLine)


def test_cmd_execute():
    cmd_obj_2 = CommandLine("Test2", "-ejfhj")
    actual_cmd_status, actual_cmd_command_text, act_opt_text = cmd_obj_2.result_execute_command()

    expected_text_command = f"<Test2> success"
    expected_status_code = 0
    expected_text_option = f"Value of <-ejfhj > set successfully."
    assert actual_cmd_status == expected_status_code
    assert actual_cmd_command_text == expected_text_command
    assert act_opt_text == expected_text_option
