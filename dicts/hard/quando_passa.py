def quando_passa(tv_schedule, title):
    title_schedule = {}

    for channel, schedule in tv_schedule.items():
        for k, v in schedule.items():
            if title == v:
                title_schedule.setdefault(k, []).append(channel)

    return title_schedule
