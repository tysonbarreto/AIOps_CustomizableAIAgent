import sys

def get_detailed_error_message(message:str, error_detail:sys):
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"{message} | Error: {error_detail} | File: {file_name} | Line: {line_number}"

class AIException(Exception):
    
    def __init__(self, message:str, error_detail:Exception):
        self.error_message = get_detailed_error_message(message=message, error_detail=error_detail)
        super().__init__(self.error_message)
    
    def __str__(self):
        return self.error_message
    
if __name__=="__main__":
    __all__=["AIException"]