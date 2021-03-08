def format_duration(seconds):
    years = seconds // 31536000
    days = (seconds - (years*31536000)) // 86400
    hours = (seconds - (years*31536000) - (days*86400)) // 3600
    minutes = (seconds - (years*31536000) - (days*86400) - (hours*3600)) // 60
    secs = seconds - (years*31536000) - (days*86400) - (hours*3600) - (minutes*60)
    if not seconds:
        return "now"
    else:
        words = ["year", "day", "hour", "minute", "second"]
        lst = []
        cnt = 0
        for i in [years, days, hours, minutes, secs]:
            if i == 1:
                lst.append("{} {}".format(i, words[cnt]))
            elif i > 1:
                lst.append("{} {}s".format(i, words[cnt]))
            cnt += 1
        return ", ".join([i for i in lst if i])[::-1].replace(",", "dna ", 1)[::-1]


if __name__ == '__main__':
    print(format_duration(0))
    print(format_duration(62))
    print(format_duration(120))
    print(format_duration(3600))
    print(format_duration(36600002))