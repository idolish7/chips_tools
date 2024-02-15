
class Platform:
    def __init__(self, name, launch_year):
        self.name = name
        self.launch_year = launch_year

class Game:
    def __init__(self, title, year, platform):
        self.title = title
        self.year = year
        self.platform = platform

    def add_platform(self, platform=None):
        self.platform.append(platform)