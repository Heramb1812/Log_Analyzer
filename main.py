from parser import parse_logs
from analyzer import LogAnalyzer
from report import create_csv, create_json

LOG_FILE = "logs/server.log"


def print_counter(title, counter):
    print(title)

    for key, value in counter.items():
        print(f"{key}: {value}")

    print()


def main():

    logs = parse_logs(LOG_FILE)

    analyzer = LogAnalyzer(logs)

    total = analyzer.total_logs()
    levels = analyzer.count_levels()
    ips = analyzer.top_ips()
    errors = analyzer.top_errors()
    hours = analyzer.hourly_requests()

    print("=" * 50)
    print("LOG ANALYSIS REPORT")
    print("=" * 50)

    print("Total Logs:", total)
    print()

    print_counter("Log Levels", levels)

    print_counter("Top IP Addresses", ips)

    print_counter("Top Errors", errors)

    print_counter("Requests Per Hour", hours)

    create_csv(levels)

    summary = {
        "total_logs": total,
        "log_levels": dict(levels),
        "top_ips": dict(ips),
        "top_errors": dict(errors),
        "requests_per_hour": dict(hours)
    }

    create_json(summary)

    print("Reports saved inside reports/")


if __name__ == "__main__":
    main()