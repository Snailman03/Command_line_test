import pytest
import re


class CommandLine:

    def __init__(self, command_name, *options):

        self.mark_command_name_check = False
        self.mark_command_options_check = False

        self.command_name = command_name
        self.validate_command_name()

        if len(options) <= 3:
            self.list_options = list(options)
        else:
            raise ValueError("The number of options must be from 0 to 3")

        self.validate_options()

    def validate_command_name(self):
        if not isinstance(self.command_name, str):
            raise TypeError("Command must be an string")

        if len(self.command_name) < 5 or len(self.command_name) > 9:
            raise ValueError("Command must be between 5 and 9")

        if any(char in self.command_name for char in '!@#$%^&*()+=[]{}|;:",<>?/'):
            raise ValueError("Command have not content any symbols")

        self.mark_command_name_check = True

    def validate_options(self):

        for option in self.list_options:
            if not isinstance(option, str):
                raise TypeError("Options must be an string")
            if not option.startswith('-'):
                raise ValueError("Options must be starts with '-' or '--' ")

        self.mark_command_options_check = True

    def print_command_details(self):
        print("\ncurrent command name : \n" + self.command_name)
        for option in self.list_options:
            print("option : " + option)

        return self.command_name

    def result_execute_command(self):

        if self.mark_command_name_check and self.mark_command_options_check:
            success_command_text = f"<{self.command_name}> success"
            print(success_command_text)

            success_options_text = ""
            for option in self.list_options:
                print(f"Value of <{option}> set successfully.")
                success_options_text = option + " "
                success_options_text_2 = f"Value of <{success_options_text}> set successfully."
            command_status = 0
            success_options_text_2 = f"Value of <{success_options_text}> set successfully."
            return command_status, success_command_text, success_options_text_2
        else:
            no_success_command_text = f"<{self.command_name}> fail"
            print("")
            print(no_success_command_text)
            command_status = 1
            return command_status, no_success_command_text




