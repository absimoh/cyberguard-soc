failed_logins = {}

def detect_bruteforce(ip: str, status: str):
    if status != "failed":
        return {"detected": False}

    failed_logins[ip] = failed_logins.get(ip, 0) + 1

    if failed_logins[ip] >= 5:
        return {
            "detected": True,
            "type": "Brute Force Attack",
            "severity": "Critical"
        }

    return {"detected": False}