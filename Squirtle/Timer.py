#타이머 기능
class Timer:
    def __init__(self):
        self.NowRunning = False
        self.NowPause = False
        self.Hour = 0
        self.Min = 0
        self.Percent = 0.00

timer = Timer()