class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._d = {}

    def should_printMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """

        if message in self._d and timestamp - self._d[message] < 10:
            return False
        else:
            self._d[message] = timestamp
            return True

s