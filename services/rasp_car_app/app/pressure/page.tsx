"use client";

import { useState, useEffect } from "react";
import axios from "axios";
import MainNavbar from "@/components/MainNavbar";
import AreaChartComponent from "@/components/AreaChart1";

interface SensorData {
  temperature: number;
  pressure: number;
  altitude: number;
  timestamp: string;
  id: number;
}

export default function Dashboard() {
  const [data, setData] = useState<
    { name: string; temperature: number; pressure: number; altitude: number }[]
  >([]);
  const [skip, setSkip] = useState(0);
  const [limit, setLimit] = useState(10);
  const [minTemperature, setMinTemperature] = useState<number | undefined>();
  const [minPressure, setMinPressure] = useState<number | undefined>();
  const [minAltitude, setMinAltitude] = useState<number | undefined>();
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const fetchData = () => {
    const params: any = { skip, limit };
    if (minTemperature !== undefined) params.min_temperature = minTemperature;
    if (minPressure !== undefined) params.min_pressure = minPressure;
    if (minAltitude !== undefined) params.min_altitude = minAltitude;
    if (startDate) params.start_date = startDate;
    if (endDate) params.end_date = endDate;

    axios
      .get<SensorData[]>("http://127.0.0.1:8000/pressure/", { params })
      .then((response) => {
        const transformedData = response.data.map((item) => ({
          name: new Date(item.timestamp).toLocaleString(),
          temperature: item.temperature,
          pressure: item.pressure,
          altitude: item.altitude,
        }));
        setData(transformedData);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  };

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    fetchData();
  };

  useEffect(() => {
    fetchData();
    const intervalId = setInterval(() => {
      fetchData();
    }, 10000);
    return () => clearInterval(intervalId);
  }, [skip, limit, minTemperature, minPressure, minAltitude]);

  return (
    <div className="h-screen w-screen flex flex-col gap-5 py-5 px-10 items-center">
      <MainNavbar />
      <h1 className="font-bold text-3xl text-center mb-5">Sensor Data</h1>

      {/* Full-screen container to split graph and form */}
      <div className="flex h-full w-full gap-10">
        {/* Graph Section: 3/4 of the width */}
        <div
          className="menu-box flex justify-center items-center w-3/4"
          style={{
            padding: "20px",
          }}
        >
          <div style={{ width: "47%", height: "40%" }}>
            <AreaChartComponent data={data} dataKey="temperature" color="#700018" />
          </div>
          <div style={{ width: "47%", height: "40%" }}>
            <AreaChartComponent data={data} dataKey="pressure" color="#b6042a" />
          </div>
          <div style={{ width: "90%", height: "50%" }}>
            <AreaChartComponent data={data} dataKey="altitude" color="#f50538" />
          </div>
        </div>

        {/* Form Section: 1/4 of the width */}
        <div
          className="menu-box flex justify-center items-center w-1/4"
          style={{
            padding: "20px",
          }}
        >
          <form
            onSubmit={handleSubmit}
            className="flex flex-col gap-4"
            style={{
              width: "95%",
              height: "80%",
            }}
          >
            <div>
              <label className="block font-medium">Skip:</label>
              <input
                type="number"
                value={skip}
                onChange={(e) => setSkip(Number(e.target.value))}
                placeholder="0"
                className="border rounded px-2 py-1 w-full bg-black text-white"
              />
            </div>
            <div>
              <label className="block font-medium">Limit:</label>
              <input
                type="number"
                value={limit}
                onChange={(e) => setLimit(Number(e.target.value))}
                placeholder="10"
                className="border rounded px-2 py-1 w-full bg-black text-white"
              />
            </div>
            <div>
              <label>Minimum Temperature:</label>
              <input
                type="number"
                value={minTemperature || ""}
                onChange={(e) =>
                  setMinTemperature(e.target.value ? Number(e.target.value) : undefined)
                }
                placeholder="0"
                className="border rounded px-2 py-1 w-full bg-black text-white"
              />
            </div>
            <div>
              <label>Minimum Pressure:</label>
              <input
                type="number"
                value={minPressure || ""}
                onChange={(e) =>
                  setMinPressure(e.target.value ? Number(e.target.value) : undefined)
                }
                placeholder="0"
                className="border rounded px-2 py-1 w-full bg-black text-white"
              />
            </div>
            <div>
              <label>Minimum Altitude:</label>
              <input
                type="number"
                value={minAltitude || ""}
                onChange={(e) =>
                  setMinAltitude(e.target.value ? Number(e.target.value) : undefined)
                }
                placeholder="0"
                className="border rounded px-2 py-1 w-full bg-black text-white"
              />
            </div>
            <div>
              <label>Start Date:</label>
              <input
                type="text"
                value={startDate}
                onChange={(e) => setStartDate(e.target.value)}
                placeholder="YYYY-MM-DDTHH:MM:SS"
                className="border rounded px-2 py-1 w-full bg-black text-white"
              />
            </div>
            <div>
              <label>End Date:</label>
              <input
                type="text"
                value={endDate}
                onChange={(e) => setEndDate(e.target.value)}
                placeholder="YYYY-MM-DDTHH:MM:SS"
                className="border rounded px-2 py-1 w-full bg-black text-white"
              />
            </div>
            <button
              type="submit"
              className="bg-blue-500 text-white px-4 py-2 rounded"
            >
              Submit
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
