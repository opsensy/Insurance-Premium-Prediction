from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os,sys

def test_logger_and_exception():
    try:
        logging.info(
            """
            Starting the Test logger and Exception
            
            """
        )
        result = 3/0
        print(result)
        logging.info(
            """
            Ending point of the Test logger and Exception
            
            """
        )
    except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(e, sys)

if __name__ == "__main__":
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)