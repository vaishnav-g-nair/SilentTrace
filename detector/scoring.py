def confidence_level(score):
    if score >= 90:
        return "HIGH"
    elif score >= 70:
        return "MEDIUM"
    else:
        return "LOW"


def score_silence(window_df, rules):
    """
    Scores a silence window using config-driven rules.
    Returns: score, confidence, evidence
    """

    # -----------------------------
    # Suppression logic (FIRST)
    # -----------------------------
    suppressions = rules.get("suppressions", {})

    for name, rule in suppressions.items():
        keywords = rule.get("keywords", [])
        if keywords:
            pattern = "|".join(keywords)
            if window_df["message"].str.contains(pattern, case=False).any():
                return 0, "SUPPRESSED", [rule["description"]]

    # -----------------------------
    # Base score
    # -----------------------------
    score = 30
    evidence = ["Log silence window detected"]

    triggered_signals = set()
    signals = rules.get("signals", {})

    # -----------------------------
    # Signal detection
    # -----------------------------
    for name, rule in signals.items():

        # Event ID based signal
        if "event_ids" in rule:
            if window_df["event_id"].isin(rule["event_ids"]).any():
                if name not in triggered_signals:
                    score += rule["weight"]
                    triggered_signals.add(name)
                    evidence.append(rule["description"])

        # Keyword based signal
        if "keywords" in rule:
            pattern = "|".join(rule["keywords"])
            if window_df["message"].str.contains(pattern, case=False).any():
                if name not in triggered_signals:
                    score += rule["weight"]
                    triggered_signals.add(name)
                    evidence.append(rule["description"])

        # Field based signal
        if "field" in rule:
            field = rule["field"]
            if field in window_df.columns:
                if window_df[field].astype(bool).any():
                    if name not in triggered_signals:
                        score += rule["weight"]
                        triggered_signals.add(name)
                        evidence.append(rule["description"])

    confidence = confidence_level(score)
    return score, confidence, evidence
