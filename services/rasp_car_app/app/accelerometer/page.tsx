"use client";

import { useState, useEffect } from "react";
import axios from "axios";
import MainNavbar from "@/components/MainNavbar";
import ComposedChartComponent from  "@/components/Radar";

interface AccelerometerData {
  x: number;
  y: number;
  z: number;
  timestamp: string;
  id: number;
}

export default function Accelerometer() {
  const [data, setData] = useState<{ name: string; x: number; y: number; z: number }[]>([]);
  const [skip, setSkip] = useState(0);
  const [limit, setLimit] = useState(10);
  const [minX, setMinX] = useState<number | undefined>();
  const [minY, setMinY] = useState<number | undefined>();
  const [minZ, setMinZ] = useState<number | undefined>();
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const fetchData = () => {
    const params: any = { skip, limit };
    if (minX !== undefined) params.min_x = minX;
    if (minY !== undefined) params.min_y = minY;
    if (minZ !== undefined) params.min_z = minZ;
    if (startDate) params.start_date = startDate;
    if (endDate) params.end_date = endDate;

    axios
      .get<AccelerometerData[]>("http://127.0.0.1:8000/accelerometer/", { params })
      .then((response) => {
        console.log(response.data); 
        const transformedData = response.data.map((item) => ({
          name: new Date(item.timestamp).toLocaleString(),
          x: item.x,
          y: item.y,
          z: item.z,
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
    }, 10000); // Fetch every 20 seconds
    return () => clearInterval(intervalId);
  }, [skip, limit, minX, minY, minZ]);

  return (
    <div className="h-screen w-screen flex flex-col gap-5 py-5 px-10 items-center">
      <MainNavbar />
      <h1 className="font-bold text-3xl text-center mb-5">Accelerometer</h1>

      <div className="flex h-full w-full gap-10">
        {/* Chart Section: 3/4 of the width */}
        <div className="menu-box flex justify-center items-center w-3/4" style={{ padding: "20px" }}>
          <div style={{ width: "90%", height: "90%" }}>
            <ComposedChartComponent data={data} />
          </div>
        </div>

        {/* Form Section: 1/4 of the width */}
        <div className="menu-box flex justify-center items-center w-1/4" style={{ padding: "20px" }}>
          <form
            onSubmit={handleSubmit}
            className="flex flex-col gap-4"
            style={{ width: "95%", height: "80%" }}
          >
            <div>
              <label className="block font-medium">Skip:</label>
              <input
                type="number"
                value={skip}
                onChange={(e) => setSkip(Number(e.target.value))}
                placeholder="10"
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
              <label>Minimum X:</label>
              <input
                type="number"
                value={minX || ""}
                onChange={(e) => setMinX(e.target.value ? Number(e.target.value) : undefined)}
                placeholder="0"
                className="border rounded px-2 py-1 w-full bg-black text-white"
              />
            </div>
            <div>
              <label>Minimum Y:</label>
              <input
                type="number"
                value={minY || ""}
                onChange={(e) => setMinY(e.target.value ? Number(e.target.value) : undefined)}
                placeholder="0"
                className="border rounded px-2 py-1 w-full bg-black text-white"
              />
            </div>
            <div>
              <label>Minimum Z:</label>
              <input
                type="number"
                value={minZ || ""}
                onChange={(e) => setMinZ(e.target.value ? Number(e.target.value) : undefined)}
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
                placeholder="2024-11-13T23:27:52"
                className="border rounded px-2 py-1 w-full bg-black text-white"
              />
            </div>
            <div>
              <label>End Date:</label>
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
