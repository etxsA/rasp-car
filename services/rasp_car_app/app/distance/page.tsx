"use client";

import { useState, useEffect } from "react";
import axios from "axios";
import MainNavbar from "@/components/MainNavbar";
import AreaChartComponent from "@/components/LineChart";

interface DistanceData {
  distance: number;
  timestamp: string;
  id: number;
}

export default function Dashboard() {
  const [data, setData] = useState<{ name: string; value: number }[]>([]);
  const [skip, setSkip] = useState(0);
  const [limit, setLimit] = useState(100);
  const [minDistance, setMinDistance] = useState<number | undefined>();
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  const fetchData = () => {
    const params: any = { skip, limit };
    if (minDistance !== undefined) params.min_distance = minDistance;
    if (startDate) params.start_date = startDate;
    if (endDate) params.end_date = endDate;

    axios
      .get<DistanceData[]>("http://127.0.0.1:8000/distance/", { params })
      .then((response) => {
        const transformedData = response.data.map((item) => ({
          name: new Date(item.timestamp).toLocaleString(),
          value: item.distance,
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

  // Fetch data on component mount and set up periodic updates
  useEffect(() => {
    fetchData();

    const intervalId = setInterval(() => {
      fetchData();
    }, 10000); // Fetch every 10 seconds

    return () => clearInterval(intervalId);
  }, [skip, limit, minDistance]); // Ensure filters are respected

  return (
    <div className="h-screen w-screen flex flex-col gap-5 py-5 px-10 items-center">
      <MainNavbar />
      <h1 className="font-bold text-3xl text-center mb-5">Distance</h1>

      {/* Full-screen container to split graph and form */}
      <div className="flex h-full w-full gap-10">
        {/* Graph Section */}
        <div
          className="menu-box flex justify-center items-center w-3/4"
          style={{
            padding: "20px",
          }}
        >
          <div style={{ width: "90%", height: "90%" }}>
            <AreaChartComponent data={data} />
          </div>
        </div>

        {/* Form Section */}
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
              display: "flex",
              flexDirection: "column",
              justifyContent: "space-between",
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
              <label>Minimum Distance:</label>
              <input
                type="number"
                value={minDistance || ""}
                onChange={(e) =>
                  setMinDistance(e.target.value ? Number(e.target.value) : undefined)
                }
                placeholder="0"
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
