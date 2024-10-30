# errors.py
class InvalidValueError(Exception):
    """Custom exception for invalid input values in the AI processing system."""
    pass  # Raise this exception when invalid data is encountered

class ConfusionError(Exception):
    """Raised when the AI processing system encounters unexpected behavior."""
    pass  # Custom error for AI system failures
