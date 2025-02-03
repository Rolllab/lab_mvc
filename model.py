import json

class TimeTableModel:
    def __init__(self):
        self.schedule = []

    def add_course(self, course, date):
        self.schedule.append({"course": course, "date": date})

    def get_all_courses(self):
        return self.schedule

    def save(self):
        with open('json/CourseJsonFile.json', 'w', encoding='utf-8') as fp:
            json.dump(obj=self.schedule, fp=fp, ensure_ascii= False, indent=4)
