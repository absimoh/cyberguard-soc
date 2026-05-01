# CyberGuard SOC Platform

CyberGuard is a simple cybersecurity project that detects common attacks and displays them in a dashboard.

## Features

- SQL Injection detection  
- Brute Force attack detection  
- Real-time dashboard  
- Attack visualization (charts)  
- Data storage using SQLite  

## Technologies Used

- Backend: FastAPI (Python)  
- Frontend: React (Vite)  
- Database: SQLite  

## How to Run

### Backend

cd backend  
uvicorn app.main:app --reload  

### Frontend

cd frontend  
npm install  
npm run dev  

## API Endpoints

- POST /logs → send logs for detection  
- GET /alerts → view detected alerts  

## Purpose

This project is built for learning cybersecurity (Blue Team) and understanding how a simple SIEM system works.

