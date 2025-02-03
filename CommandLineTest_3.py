

class CommandLine():

    # control attribute
    mark_command_check_pass = False
    # list_command_check = []

    mark_options_check_pass = False

    # constructor - initializing variables
    def __init__(self, command, options):
        self.validate_command(command)
        self._command = command

        self.validate_options(options)
        self._options = options

    def validate_command(self, command):
        if not isinstance(command, str):
            raise TypeError("Command must be an string")
        if len(command) < 5 or len(command) > 9:
            raise ValueError("Сommand must be between 5 and 9")
        if any(char in command for char in '!@#$%^&*()+=[]{}|;:",<>?/'):
            raise ValueError("Сommand must be between 5 and 9")
        self.mark_command_check_pass = True

    def validate_options(self, options):
        if len(options.split()) == 1:
            if not isinstance(options, str):
                raise TypeError("Options must be an string")
            if not options.startswith('-'):
                raise ValueError("Options must be starts with '-' ")
        elif len(options.split()) > 1:
                if len(options.split()) > 3:
                    raise ValueError("Max count of options = 3")

        self.mark_options_check_pass = True


    def print_details_success_command(self):
        print("name : " + self.name)
        print("options : " + str(self.options))


    def result_success_command(self):
        if self.mark_command_check_pass and self.mark_options_check_pass:
            success_command = f"<{self._command}> success"
            command_status = 0
            return success_command, command_status
        else:
            no_success_command = f"<{self._command}> fail"
            command_status = 1
            return no_success_command,command_status

first_command = CommandLine("ewfwef", "-ff")
res_first_command = first_command.result_success_command()

second_command = CommandLine(1, "-ff")
print(second_command.result_success_command())