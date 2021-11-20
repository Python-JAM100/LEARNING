## Example Chapter 8_3
```bash
from time import sleep

class Clock(object):
    """Digital clock"""

    def __init__(self, hour=0, minute=0, second=0):
        """initialize method

        :param hour: hour
        :param minute: minute
        :param second: second
        """
        self._hour = hour
        self._minute = minute
        self._second = second
        # called value will replace 0 when Class is called

    def run(self):
        """run method"""
        self._second += 1
        if self._second == 60:  # when second equal to 60
            self._second = 0    # second replace and then
            self._minute += 1   # minute plus 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """display time"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        # every result show 1 time, then will wait 1 second before show the next result
        clock.run()


if __name__ == '__main__':
    main()
```

## Output Chapter 8_3
```
23:59:58
23:59:59
00:00:00
00:00:01
00:00:02
00:00:03
00:00:04
```