from collections import Counter


class LogAnalyzer:

    def __init__(self, logs):
        self.logs = logs

    def total_logs(self):
        return len(self.logs)

    def count_levels(self):
        return Counter(log["level"] for log in self.logs)

    def top_ips(self):
        return Counter(log["ip"] for log in self.logs)

    def top_errors(self):
        errors = [
            log["message"]
            for log in self.logs
            if log["level"] == "ERROR"
        ]

        return Counter(errors)

    def hourly_requests(self):
        hours = [
            log["timestamp"][11:13]
            for log in self.logs
        ]

        return Counter(hours)