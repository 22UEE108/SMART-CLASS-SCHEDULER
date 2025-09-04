from datetime import datetime

class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.classes = []

    def add_class(self, class_):
        # Conflict detection
        for c in self.classes:
            if (class_.start_time < c.end_time and class_.end_time > c.start_time):
                if "Placement Interview" in class_.subject:
                    # Cannot reschedule interviews
                    print(f"⚠ {self.name} cannot attend {class_.subject} due to conflict with {c.subject}.")
                    return False
                else:
                    print(f"⚠ Conflict: {self.name} already has {c.subject} scheduled.")
                    return False
        self.classes.append(class_)
        print(f"✅ {class_.subject} scheduled for {self.name}")
        return True

class Class:
    def __init__(self, subject, start_time, end_time):
        self.subject = subject
        self.start_time = start_time
        self.end_time = end_time

if __name__ == "__main__":
    # Students
    raman = Student("Raman", "raman@mail.com")
    aditi = Student("Aditi", "aditi@mail.com")

    # Core classes vs Placement Interview (fixed)
    core_class = Class("Digital Electronics", datetime(2025, 9, 6, 10, 0), datetime(2025, 9, 6, 11, 0))
    placement_interview = Class("Placement Interview - Google", datetime(2025, 9, 6, 10, 30), datetime(2025, 9, 6, 11, 30))
    other_class = Class("Signals & Systems", datetime(2025, 9, 6, 11, 30), datetime(2025, 9, 6, 12, 30))

    # Schedule classes
    raman.add_class(core_class)           # ✅ Should schedule
    raman.add_class(placement_interview)  # ⚠ Cannot reschedule
    raman.add_class(other_class)          # ✅ Should schedule

    aditi.add_class(placement_interview)  # ✅ Should schedule
    aditi.add_class(other_class)          # ✅ Should schedule

    # Print schedules
    print("\n--- Student Schedules ---")
    for student in [raman, aditi]:
        print(f"\n{student.name}'s Classes:")
        for c in student.classes:
            print(f"{c.subject} from {c.start_time.strftime('%H:%M')} to {c.end_time.strftime('%H:%M')}")
