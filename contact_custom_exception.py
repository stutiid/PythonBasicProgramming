class ContactException(Exception):
    exception_type = ('ENTERED_NULL', 'ENTERED_EMPTY', 'INVALID')

    def __init__(self, type_of_exception: object, message):
        self.exception_type = type_of_exception
        self.message = message

    def __str__(self):
        return self.exception_type + " exception occurred dur to " + self.message
