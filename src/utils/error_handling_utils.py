from src.domain.app_exception import AppException


class ErrorHandlingUtils:

    @staticmethod
    def application_error(error_message: str, exception: Exception) -> AppException:
        if isinstance(exception, AppException):
            return AppException(exception.message)
        else:
            return AppException(error_message)
