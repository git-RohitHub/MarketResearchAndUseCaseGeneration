import sys


def error_message_detail(error_message,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()

    # Extracting file name in which error occoured
    file_name  = exc_tb.tb_frame.f_code.co_filename

    # Extracting line number in which error occured 
    line_number = exc_tb.tb_lineno
    
    error_message = f"Error Occured python script name [{file_name}] line number [{line_number}] error_message [{error_message}]"
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail):
        # Initializing the base class 
        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message,error_detail=error_detail
        )

    def __str__(self):
        return self.error_message

