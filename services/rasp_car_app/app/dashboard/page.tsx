"use client";

// pages/dashboard.tsx
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

  useEffect(() => {
    // Fetch data from the backend API
    axios
      .get<PhotoresistorData[]>("http://127.0.0.1:8000/photoresistor/?skip=0&limit=10")
      .then((response) => {
        // Transform the data to match the expected format for the Chart
        const transformedData = response.data.map((item) => ({
          name: new Date(item.timestamp).toLocaleString(), // Using timestamp as 'name'
          value: item.voltage,   // Using voltage as 'value'
        }));
        setData(transformedData);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);
    
  return (
    <div className="h-screen w-screen flex flex-col gap-5 py-5 px-40 items-center">
      <MainNavbar />
      <h1 className="font-bold">Dashboard</h1>
      <div className="w-3/4">
        <Chart data={data} />
      </div>
    </div>
  );
}
