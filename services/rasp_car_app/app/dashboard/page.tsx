"use client";

import { useState, useEffect } from "react";
import axios from "axios";
import MainNavbar from "@/components/MainNavbar";
import Chart from "@/components/Chart";

// Define a type for your data to help with TypeScript inference
interface PhotoresistorData {
  voltage: number;
  lightLevel: number;
  timestamp: string;
  id: number;
}

export default function Dashboard() {
  const [data, setData] = useState<{ name: string; value: number }[]>([]);
  const [skip, setSkip] = useState(0);
  const [limit, setLimit] = useState(10);
  const [minVoltage, setMinVoltage] = useState<number | undefined>();
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  // Function to fetch data with the given parameters
  const fetchData = () => {
    const params: any = { skip, limit };
    if (minVoltage !== undefined) params.min_voltage = minVoltage;
    if (startDate) params.start_date = startDate;
    if (endDate) params.end_date = endDate;

    axios
      .get<PhotoresistorData[]>("http://127.0.0.1:8000/photoresistor/", { params })
      .then((response) => {
        const transformedData = response.data.map((item) => ({
          name: new Date(item.timestamp).toLocaleString(),
          value: item.voltage,
        }));
        setData(transformedData);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  };

  // Handle form submission
  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    fetchData();
  };

  return (
    <div className="h-screen w-screen flex flex-col gap-5 py-5 px-40 items-center">
      <MainNavbar />
      <h1 className="font-bold">Dashboard</h1>
      
      {/* Form for API parameters */}
      <form onSubmit={handleSubmit} className="flex flex-col gap-4 w-full max-w-md">
        <div>
          <label>Skip:</label>
          <input
            type="number"
            value={skip}
            onChange={(e) => setSkip(Number(e.target.value))}
            className="border rounded px-2 py-1"
          />
        </div>
        <div>
          <label>Limit:</label>
          <input
            type="number"
            value={limit}
            onChange={(e) => setLimit(Number(e.target.value))}
            className="border rounded px-2 py-1"
          />
        </div>
        <div>
          <label>Minimum Voltage:</label>
          <input
            type="number"
            value={minVoltage || ""}
            onChange={(e) => setMinVoltage(e.target.value ? Number(e.target.value) : undefined)}
            className="border rounded px-2 py-1"
          />
        </div>
        <div>
          <label>Start Date (format: YYYY-MM-DDTHH:MM:SS):</label>
          <input
            type="text"
            value={startDate}
            onChange={(e) => setStartDate(e.target.value)}
            placeholder="2024-11-13T23:27:52"
            className="border rounded px-2 py-1"
          />
        </div>
        <div>
          <label>End Date (format: YYYY-MM-DDTHH:MM:SS):</label>
          <input
            type="text"
            value={endDate}
            onChange={(e) => setEndDate(e.target.value)}
            placeholder="2024-11-14T23:27:52"
            className="border rounded px-2 py-1"
          />
        </div>
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
          Submit
        </button>
      </form>

      {/* Chart displaying the fetched data */}
      <div style={{ width: "856px", height: "256px" }} className="mt-5">
        <Chart data={data} />
      </div>
    </div>
  );
}
