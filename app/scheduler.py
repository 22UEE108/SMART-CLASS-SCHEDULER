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
                print(f"⚠ Conflict detected: {self.name} already has {c.subject} at this time.")
                return False
        self.classes.append(class_)
        print(f"✅ Class '{class_.subject}' scheduled for {self.name}")
        return True


class Class:
    def __init__(self, subject, start_time, end_time):
        self.subject = subject
        self.start_time = start_time
        self.end_time = end_time


if __name__ == "__main__":
    # Demo
    alice = Student("Alice", "alice@mail.com")
    bob = Student("Bob", "bob@mail.com")

    class1 = Class("Math", datetime(2025, 9, 6, 10, 0), datetime(2025, 9, 6, 11, 0))
    class2 = Class("Physics", datetime(2025, 9, 6, 10, 30), datetime(2025, 9, 6, 11, 30))
    class3 = Class("Chemistry", datetime(2025, 9, 6, 11, 30), datetime(2025, 9, 6, 12, 30))

    alice.add_class(class1)
    alice.add_class(class2)
    alice.add_class(class3)

    bob.add_class(class2)
    bob.add_class(class3)

    # Print schedules
    print("\n--- Student Schedules ---")
    for student in [alice, bob]:
        print(f"\n{student.name}'s Classes:")
        for c in student.classes:
            print(f"{c.subject} from {c.start_time.strftime('%H:%M')} to {c.end_time.strftime('%H:%M')}")
