from icalendar import Calendar, Event


def main():
    cal = Calendar.from_string(open('basic.ics', 'rb').read())

if __name__ == '__main__':
    main()
