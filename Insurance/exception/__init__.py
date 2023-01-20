import os
import sys
class InsuranceException(Exception):
    def __init__(self,err_message:Exception,err_detail:sys):
        super().__init__(err_message)
        self.err_message = InsuranceException.err_message_detail(err_message, err_detail=err_detail)

    @staticmethod
    def err_message_detail(err_message:Exception,err_detail:sys)->str:
        _,_ ,exc_tb = err_detail.exc_info()
        line_no = exc_tb.tb_frame.f_lineno

        file_name = exc_tb.tb_frame.f_code.co_filename

        error_message = f"Error occured python script name [{file_name}]" f"line_number[{exc_tb.tb_lineno}] error message [{error}]"

        return err_message

    def __str__(self):
        return InsuranceException.__name__.__str__()