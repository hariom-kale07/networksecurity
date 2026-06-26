import sys

class NetworkSecurityException(Exception):

    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message

        _, _, exc_tb = error_details.exc_info()

        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.line_number = exc_tb.tb_lineno

    def __str__(self):
        return (
            f"Error occurred in python script "
            f"[{self.file_name}] "
            f"line number [{self.line_number}] "
            f"error message [{self.error_message}]"
        )