class TaskHandler:
    def __init__(self, tasks):
        self.tasks = tasks
    
    def getTasks(self):
        for task in self.tasks:
            if task['mode'] == "NEW-VID-TWEE":
                yield NewVidTweet