
import logging

class CustomError (Exception):
    def __init__(self, message, code=500):
        self.message = message
        self.code = code
        super().__init__(self.message, self.code)

    def raise_error():
        raise CustomError("This is a custom error")
    
    def raise_error_with_message(message):
        raise CustomError(message)

try:
    CustomError.raise_error()
except CustomError as e:
    print(e)
    logging.exception(e)

print("--------------------")
print("--------------------")

try:
    raise Exception("This is a generic exception", 999)
except Exception as e:
    print(e)
    logging.exception(e)