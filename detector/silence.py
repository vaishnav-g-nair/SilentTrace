from datetime import timedelta


def detect_silence_windows(host_df, silence_minutes):
    """
    Detect periods where no logs were generated for a host.
    Returns a list of silence windows.
    """

    windows = []
    previous_time = None

    # Logs must already be sorted by timestamp
    for _, row in host_df.iterrows():
        if previous_time is not None:
            delta = row["timestamp"] - previous_time

            if delta > timedelta(minutes=silence_minutes):
                windows.append({
                    "start": previous_time,
                    "end": row["timestamp"],
                    "duration": round(delta.total_seconds() / 60, 2)
                })

        previous_time = row["timestamp"]

    return windows
