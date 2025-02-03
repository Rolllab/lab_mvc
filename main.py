from model import TimeTableModel
from controller import Controller
from view import View



if __name__ == "__main__":
    # Создание экземпляров классов
    model = TimeTableModel()
    view = View()
    controller = Controller(model, view)

    # Добавление заданий
    controller.add_course("HTML", "Feb 01")
    controller.add_course("CSS", "Aug 14")
    controller.add_course("JS", "May 10")
    controller.add_course("Python", "Nov 21")
    controller.show_timetable()
    controller.model.save()
