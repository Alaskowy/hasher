class Buffer:
    """Class that handles the saved encrypted words"""

    def __init__(self):
        self._buffer = []

    def add(self, message: dict):
        """Add message to the buffer"""
        if isinstance(message, list):
            for word in message:
                self._buffer.append(word)
        else:
            self._buffer.append(message)

    def add_list(self, messages: list):
        """Add list of messages to the buffer"""
        self._buffer += messages

    def peak(self) -> list:
        """Peek the buffer"""
        return self._buffer
