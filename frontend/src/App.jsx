import { useEffect, useState } from "react";
import axios from "axios";
import { PieChart, Pie, Cell, Tooltip } from "recharts";

function App() {
  const [alerts, setAlerts] = useState([]);

  const fetchAlerts = () => {
    axios.get("http://127.0.0.1:8000/alerts")
      .then(res => setAlerts(res.data))
      .catch(err => console.error(err));
  };

  const getChartData = () => {
    const counts = {};

    alerts.forEach(a => {
      counts[a.alert.type] = (counts[a.alert.type] || 0) + 1;
    });

    return Object.keys(counts).map(key => ({
      name: key,
      value: counts[key]
    }));
  };

  useEffect(() => {
    fetchAlerts();

    const interval = setInterval(() => {
      fetchAlerts();
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div style={{ padding: 30, background: "#0f172a", minHeight: "100vh", color: "white" }}>
      <h1>🚨 CyberGuard SOC Dashboard</h1>

      <p>Total Alerts: {alerts.length}</p>

      <button onClick={fetchAlerts} style={{ marginBottom: 20 }}>
        Refresh
      </button>

      {alerts.length > 0 && (
        <div style={{ marginBottom: 30 }}>
          <h2>Attack Distribution</h2>

          <PieChart width={400} height={300}>
            <Pie
              data={getChartData()}
              dataKey="value"
              nameKey="name"
              cx="50%"
              cy="50%"
              outerRadius={100}
              label
            >
              {getChartData().map((entry, index) => (
                <Cell
                  key={index}
                  fill={
                    entry.name === "Brute Force Attack"
                      ? "red"
                      : entry.name === "SQL Injection"
                      ? "orange"
                      : "yellow"
                  }
                />
              ))}
            </Pie>
            <Tooltip />
          </PieChart>
        </div>
      )}

      {alerts.length === 0 ? (
        <p>No alerts yet</p>
      ) : (
        alerts.slice().reverse().map((item, index) => (
          <div
            key={index}
            style={{
              border:
                item.alert.severity === "Critical"
                  ? "2px solid red"
                  : item.alert.severity === "High"
                  ? "2px solid orange"
                  : "2px solid yellow",
              padding: 15,
              marginBottom: 10,
              borderRadius: 10,
              background: "#1e293b"
            }}
          >
            <h3>⚠️ {item.alert.type}</h3>
            <p>Severity: {item.alert.severity}</p>
            <p>IP: {item.log.ip}</p>
            <p>Path: {item.log.path || "N/A"}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default App;