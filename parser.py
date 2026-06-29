import re

LOG_PATTERN = r'(\S+\s+\S+)\s+(INFO|WARNING|ERROR)\s+(.*?)\s+IP=(.*)'


def parse_logs(filename):
    parsed_logs = []

    with open(filename, "r") as file:
        for line in file:
            match = re.match(LOG_PATTERN, line.strip())

            if match:
                timestamp, level, message, ip = match.groups()

                parsed_logs.append({
                    "timestamp": timestamp,
                    "level": level,
                    "message": message,
                    "ip": ip
                })

    return parsed_logs