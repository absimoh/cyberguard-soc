def detect_sql_injection(text: str):
    patterns = ["' OR '1'='1", "UNION SELECT", "DROP TABLE", "--"]

    for pattern in patterns:
        if pattern.lower() in text.lower():
            return {
                "detected": True,
                "type": "SQL Injection",
                "severity": "High"
            }

    return {"detected": False}