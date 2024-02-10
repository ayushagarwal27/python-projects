from datetime import datetime
from dataclasses import dataclass
import pandas as pd
from tabulate import tabulate


@dataclass
class Habit:
    name: str
    time_since: str
    remaining_days: str
    minutes_saved: float
    money_saved: str


def track_habit(name: str, start: datetime, cost: float, minutes_used: float) -> Habit:
    goal: int = 60
    hourly_wage: int = 30
    time_elapsed: float = (datetime.now() - start).total_seconds()
    hours: float = round(time_elapsed / 60 / 60, 1)
    days: float = round(hours / 24, 2)

    money_saved: float = cost * days
    minutes_used: float = round(days * minutes_used)
    total_money_saved: str = f'$({round(money_saved + (minutes_used / 60 * hourly_wage), 2)})'

    days_to_go = round(goal - days)

    remaining_days = 'Cleared' if days_to_go <= 0 else f'{days_to_go}'
    time_since = f'{days} days' if hours > 72 else f'{hours} hours'

    return Habit(name=name, time_since=time_since, remaining_days=remaining_days, minutes_saved=minutes_used,
                 money_saved=total_money_saved)


def main():
    habits: list[Habit] = [
        track_habit('Coffee', datetime(2024, 2, 9, 6), cost=1, minutes_used=5),
        track_habit('TV', datetime(2024, 2, 5, 6), cost=200, minutes_used=60*2),
    ]

    df = pd.DataFrame(habits)
    print(tabulate(df, headers='keys', tablefmt='psql'))


if __name__ == '__main__':
    main()
