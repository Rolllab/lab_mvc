class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_timetable(self):
        courses = self.model.get_all_courses()
        self.view.display_timetable(courses)

    def add_course(self, course, date):
        self.model.add_course(course, date)