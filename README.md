# CyberGuard SOC Platform

A simple SIEM-like system built with FastAPI and React.

CyberGuard is a mini Security Operations Center (SOC) platform designed to detect and monitor cyber attacks in real-time.

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
- Visualization: Recharts  

## Running the Project

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
