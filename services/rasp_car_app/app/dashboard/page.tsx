"use client";

import { useState, useEffect } from "react";
import axios from "axios";
import MainNavbar from "@/components/MainNavbar";
import Chart from "@/components/Chart";

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

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    fetchData();
  };

  return (
    <div className="h-screen w-screen flex flex-col gap-5 py-5 px-10 items-center">
      <MainNavbar />
      <h1 className="font-bold text-3xl text-center mb-5">PhotoResistor</h1>

      {/* Full-screen container to split graph and form */}
      <div className="flex h-full w-full gap-10">
        {/* Graph Section: 3/4 of the width */}
        <div
          className="menu-box flex justify-center items-center w-3/4"
          style={{
            padding: "20px",
          }}
        >
          <div style={{ width: "90%", height: "90%" }}>
            <Chart data={data} />
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
              display: "flex", // Flex layout to arrange children
              flexDirection: "column", // Arrange elements vertically
              justifyContent: "space-between", // Distribute elements
              width: "95%", // Full width of parent
              height: "80%", // Full height of parent
            }}
          >
            <div>
              <label className="block font-medium">Skip:</label>
              <input
                type="number"
                value={skip}
                onChange={(e) => setSkip(Number(e.target.value))}
                className="border rounded px-2 py-1 w-full bg-black text-white"
              />
            </div>
            <div>
              <label className="block font-medium">Limit:</label>
              <input
                type="number"
                value={limit}
                onChange={(e) => setLimit(Number(e.target.value))}
                className="border rounded px-2 py-1 w-full bg-black text-white"
              />
            </div>
            <div>
              <label>Minimum Voltage:</label>
              <input
                type="number"
                value={minVoltage || ""}
                onChange={(e) =>
                  setMinVoltage(e.target.value ? Number(e.target.value) : undefined)
                }
                className="border rounded px-2 py-1 w-full bg-black text-white"
              />
            </div>
            <div>
              <label>Start Date (format: YYYY-MM-DDTHH:MM:SS):</label>
              <input
                type="text"
                value={startDate}
                onChange={(e) => setStartDate(e.target.value)}
                placeholder="2024-11-13T23:27:52"
                className="border rounded px-2 py-1 w-full bg-black text-white"
              />
            </div>
            <div>
              <label>End Date (format: YYYY-MM-DDTHH:MM:SS):</label>
              <input
                type="text"
                value={endDate}
                onChange={(e) => setEndDate(e.target.value)}
                placeholder="2024-11-14T23:27:52"
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
