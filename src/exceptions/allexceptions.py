class NotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ProfileDoesNotExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NotAlistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidCourseCodeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidCourseTitleException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CourseIsFullException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class StudentAlreadyEnrolledException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CourseAlreadyRegisteredException(RuntimeError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NullException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidPasswordLengthException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidEmailPatternException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidNameLengthException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidNameException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidDetailsException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class VerificationFailedException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidGradeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class EmailAlreadyExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class AlreadyExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ErrorRegistering(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidRoleException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class IncorrectPasswordException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidPhoneNumberException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class UserDoesNotExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class JsonifyError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidDateException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidAmountException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ProductNotApprovedException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

