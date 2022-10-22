from dataclasses import dataclass, field
from datetime import datetime, timedelta


@dataclass
class Chat:
    id: int
    check_in_time: datetime = field(init=False)
    time_delta: timedelta = field(init=False)

    def __post_init__(self):
        self.check_in_time = datetime.now()
        self.time_delta = timedelta()

    def calc_delta(self):
        self.time_delta = datetime.now() - self.check_in_time

    def check_in(self):
        self.check_in_time = datetime.now()

    def __eq__(self, other):
        if other.id == self.id:
            return True
        return False


class Container:
    members: list = []

    def get(self, chat_id: int) -> Chat:
        for mem in self.members:
            if chat_id == mem.id:
                return mem

    def update(self, chat: Chat):
        for mem in self.members:
            if mem.id == chat.id:
                return
        self.members.append(chat)


def literal_days(days: int):
    if 10 <= days <= 20:
        return 'дней'
    elif days % 10 == 0:
        return 'дней'
    elif days % 10 == 1:
        return 'день'
    elif days % 10 == 2:
        return 'дня'
    elif days % 10 == 3:
        return 'дня'
    elif days % 10 == 4:
        return 'дня'
    else:
        return 'дней'
