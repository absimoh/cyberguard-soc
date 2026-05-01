from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.detectors.bruteforce import detect_bruteforce
from app.database import engine, SessionLocal
from app.models import Base, Alert

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CyberGuard SOC")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.get("/")
def home():
    return {"message": "CyberGuard SOC is running"}


@app.post("/logs")
def receive_log(log: dict):
    db = SessionLocal()

    detection_sql = detect_sql_injection(str(log))
    detection_brute = detect_bruteforce(log.get("ip"), log.get("status"))

    detection = detection_sql if detection_sql["detected"] else detection_brute

    if detection["detected"]:
        existing = db.query(Alert).filter(
            Alert.ip == log.get("ip"),
            Alert.type == detection["type"]
        ).first()

        if not existing:
            alert = Alert(
                ip=log.get("ip"),
                type=detection["type"],
                severity=detection["severity"],
                data=str(log)
            )

            db.add(alert)
            db.commit()

    db.close()

    return {
        "status": "received",
        "detection": detection
    }


@app.get("/alerts")
def get_alerts():
    db = SessionLocal()
    alerts = db.query(Alert).all()
    db.close()

    return [
        {
            "log": {
                "ip": alert.ip,
                "path": "N/A",
                "data": alert.data
            },
            "alert": {
                "type": alert.type,
                "severity": alert.severity
            }
        }
        for alert in alerts
    ]