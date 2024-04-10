# i think the easier way to do this is to just sort the input file, then walk through each line. the line should be
# formatted such that you can ignore any of the date stuff
# but I thought making a date thing to handle the dates properly would be more interesting.

def load():
    with open("inputs/04.txt") as f:
        lines = f.read().strip()
        return lines.split("\n")


class Date:
    def __init__(self, dateline):
        ymd, hm = dateline.split(" ")
        self.year, self.month, self.day = map(int, ymd.split("-"))
        self.hour, self.minute = map(int, hm.split(":"))

    def get_shift_date(self):
        if self.hour == 23:
            return self.get_next_day()
        return self.month, self.day

    def get_next_day(self):
        month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.year % 4 == 0:
            month_lengths[1] = 29
        if self.day < month_lengths[self.month-1]:
            return self.month, self.day+1
        else:
            return self.month+1, 1


class Guard:
    def __init__(self, id_num):
        self.id = id_num
        self.shifts = []
        self.sleep_total = None

    def get_amount_slept(self, all_shifts):
        if self.sleep_total is not None:
            return self.sleep_total
        self.sleep_total = 0
        for s_date in self.shifts:
            shift = all_shifts[s_date]
            self.sleep_total += shift.get_amount_slept()
        return self.sleep_total

    def get_sleepiest_minute(self, shifts):
        minutes = {}
        for s_date in self.shifts:
            shift = shifts[s_date]
            for minute in shift.sleepy_minutes:
                if minute not in minutes.keys():
                    minutes[minute] = 1
                else:
                    minutes[minute] += 1
        max_minute = False
        for minute in minutes:
            if max_minute:
                if minutes[minute] > minutes[max_minute]:
                    max_minute = minute
            else:
                max_minute = minute
        if max_minute:
            return max_minute, minutes[max_minute]
        else:
            return False, 0


class Shift:
    def __init__(self):
        self.starts_and_stops = []
        self.sleepy_minutes = []

    def get_amount_slept(self):
        total = 0
        self.starts_and_stops.sort(key=lambda i: i[0].minute)
        for i in range(0, len(self.starts_and_stops), 2):
            total += self.starts_and_stops[i+1][0].minute - self.starts_and_stops[i][0].minute
            for minute in range(self.starts_and_stops[i][0].minute, self.starts_and_stops[i+1][0].minute):
                self.sleepy_minutes.append(minute)
        return total


def main():
    log_entries = load()
    guards = dict()
    shifts = dict()
    for line in log_entries:
        dateline, data = line.split("]")
        data = data.strip(" ")
        dateline = dateline.strip("[")
        new_date = Date(dateline)
        shift_date = new_date.get_shift_date()
        if "#" in data:
            id_num = data.split(" ")[1].strip("#")
            if id_num not in guards.keys():
                new_guard = Guard(id_num)
                guards[id_num] = new_guard
            guards[id_num].shifts.append(shift_date)
            if shift_date not in shifts:
                shifts[shift_date] = Shift()
        else:
            if shift_date not in shifts:
                shifts[shift_date] = Shift()
            shifts[shift_date].starts_and_stops.append([new_date, data])
    longest_sleeping_guard = guards['743']
    sleepiest_overall_minute = guards['743']
    for g_id in guards:
        guard = guards[g_id]
        if guard.get_amount_slept(shifts) > longest_sleeping_guard.get_amount_slept(shifts):
            longest_sleeping_guard = guard
        if guard.get_sleepiest_minute(shifts)[1] > sleepiest_overall_minute.get_sleepiest_minute(shifts)[1]:
            sleepiest_overall_minute = guard
    print('part 1')
    print(int(longest_sleeping_guard.id) * longest_sleeping_guard.get_sleepiest_minute(shifts)[0])
    print('part 2')
    print(int(sleepiest_overall_minute.id) * sleepiest_overall_minute.get_sleepiest_minute(shifts)[0])


main()
