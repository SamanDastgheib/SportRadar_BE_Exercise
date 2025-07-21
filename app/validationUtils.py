import re
from datetime import datetime
from app import schema

def is_valid_name(name: str) -> bool:
    if not name:
        return False
    if len(name) < 2 or len(name) > 50:
        return False
    if not re.match(r"^[A-Za-z\s\-]+$", name):
        return False
    return True

def merge_eventResults(results) -> list:
   # merging results with the same event id
    results = list(results)
    sanitized_eventResults = []
    if len(results) % 2 != 0:
        return sanitized_eventResults
    for i in range(0, len(results), 2):
        if results[i].id == results[i+1].id:
            event_result = schema.EventResult(
                id=results[i].id,
                sport=results[i].sport,
                date=results[i].event_date,
                time=datetime.strptime(str(results[i].event_time), "%H:%M:%S").time(),
                team1=results[i].team,
                team2=results[i+1].team,
                day = results[i].day,
            )
            sanitized_eventResults.append(event_result)
    return sanitized_eventResults