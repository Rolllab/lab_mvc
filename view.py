class View:
    @staticmethod
    def display_timetable(courses):
        if not courses:
            print("Нет никаких курсов по расписанию.")
        else:
            for item in courses:
                print(f"Курс: {item['course']}, Дата: {item['date']}")