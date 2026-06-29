import pandas as pd
import json
import os


def create_csv(levels):

    os.makedirs("reports", exist_ok=True)

    df = pd.DataFrame(
        levels.items(),
        columns=["Log Level", "Count"]
    )

    df.to_csv("reports/report.csv", index=False)


def create_json(summary):

    os.makedirs("reports", exist_ok=True)

    with open("reports/report.json", "w") as file:
        json.dump(summary, file, indent=4)