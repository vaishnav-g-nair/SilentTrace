def build_timeline(window_df):
    events = []
    for _, row in window_df.iterrows():
        events.append(
            f"{row['timestamp']} | {row.get('event_id','')} | {row['message'][:80]}"
        )
    return " || ".join(events[:5])
