# 🚨 CyberGuard SOC Platform

CyberGuard is a mini Security Operations Center (SOC) platform designed to detect and monitor cyber attacks in real-time.

## 🔥 Features

- SQL Injection detection
- Brute Force attack detection
- Real-time alerts dashboard
- Attack classification (High / Critical)
- Auto-refreshing frontend
- Persistent storage using SQLite

## 🧠 System Overview

The system works as follows:

1. Logs are sent to the backend API
2. Detection engine analyzes incoming data
3. If a threat is detected, it is stored in the database
4. The frontend dashboard displays alerts in real-time

## 🛠️ Tech Stack

- Backend: FastAPI (Python)
- Frontend: React (Vite)
- Database: SQLite
- Visualization: Recharts

## ▶️ Running the Project

### Backend

```bash
cd backend
uvicorn app.main:app --reload