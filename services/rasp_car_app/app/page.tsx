"use client";

import axios from "axios";
import { useState, useEffect } from "react";
import MainNavbar from "@/components/MainNavbar";
import Chart from "@/components/Chart";
import ComposedChartComponent from  "@/components/BarsMain";
import AreaChartComponent from "@/components/LineChart";
import AreaChartComponent2 from "@/components/DoubleLineChart";
import SquareIconButton from "@/components/SquareIconButton";


interface PhotoresistorData {
  voltage: number;
  lightLevel: number;
  timestamp: string;
  id: number;
}

interface AccelerometerData {
  x: number;
  y: number;
  z: number;
  timestamp: string;
  id: number;
}

interface DistanceData {
  distance: number;
  timestamp: string;
  id: number;
}

interface pressureData {
  temperature: number;
  pressure: number;
  altitude: number;
  timestamp: string;
  id: number;
}

export default function Home() {
  const [dataPhotoresistor, setDataPhotoresistor] = useState<{ name: string; value: number }[]>([]);
  const [dataAccelerometer, setDataAccelerometer] = useState<{ name: string; x: number; y: number; z: number }[]>([]);
  const [dataDistance, setDataDistance] = useState<{ name: string; value: number }[]>([]);
  const [dataPressure, setDataPressure] = useState<
    { name: string; temperature: number; pressure: number; altitude: number }[]
  >([]);

  const fetchData = async () => {
    try {
      // Make all requests in parallel with a limit parameter
      const [
        photoresistorResponse,
        accelerometerResponse,
        distanceResponse,
        pressureResponse,
      ] = await Promise.all([
        axios.get<PhotoresistorData[]>("http://127.0.0.1:8000/photoresistor/", {
          params: { limit:10 },
        }),
        axios.get<AccelerometerData[]>("http://127.0.0.1:8000/accelerometer/", {
          params: { limit:4 },
        }),
        axios.get<DistanceData[]>("http://127.0.0.1:8000/distance/", {
          params: { limit:10 },
        }),
        axios.get<pressureData[]>("http://127.0.0.1:8000/pressure/", {
          params: { limit:10 },
        }),
      ]);

      setDataPhotoresistor(
        photoresistorResponse.data.map((item) => ({
          name: new Date(item.timestamp).toLocaleString(),
          value: item.voltage
        }))
      );

      setDataAccelerometer(
        accelerometerResponse.data.map((item) => ({
          name: new Date(item.timestamp).toLocaleString(),
          x: item.x,
          y: item.y,
          z: item.z,
        }))
      );

      setDataDistance(
        distanceResponse.data.map((item) => ({
          name: new Date(item.timestamp).toLocaleString(),
          value: item.distance,
        }))
      );

      setDataPressure(
        pressureResponse.data.map((item) => ({
          name: new Date(item.timestamp).toLocaleString(),
          temperature: item.temperature,
          pressure: item.pressure,
          altitude: item.altitude,
        }))
      );

    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  useEffect(() => {
    fetchData(); // Fetch data once on component mount
    const intervalId = setInterval(() => {
      fetchData(); // Fetch periodically if needed
    }, 10000); // Every 10 seconds

    return () => clearInterval(intervalId); // Cleanup interval on component unmount
  }, []);

  return (
    <div className="h-screen w-screen flex flex-col flex-nowrap gap-5 py-5 px-40 justify-start items-center" >
      <MainNavbar />
      {/* Contenedor de las dos primeras gráficas */}
      <div className="flex flex-row flex-wrap justify-center items-center gap-5 w-full min-h-[400px]">
        <div className="w-80 h-80">
          <Chart data={dataPhotoresistor} />
        </div>
        <div className="w-80 h-80">
          <ComposedChartComponent data={dataAccelerometer} />
        </div>
        <div className="w-80 h-80">
          <AreaChartComponent data={dataDistance} />
        </div>
        <div className="w-80 h-80">
          <AreaChartComponent2 data={dataPressure} />
        </div>
      </div>

      {/* Status Bar */}
      <div className="w-full  h-auto menu-box">
        <div className="status">
          <h1 className="bg-gradient-to-r from-white to-[--green] to-100%">
            Current Status
          </h1>
          <p id="name">
            Car Name: Rasp-Car
          </p>
          <p id="connection">
            Connection: Unreachable
          </p>
          <p id="ip">
            IP Addr: 10.10.10.10
          </p>
          <p id="mode">
            Running Mode: Full-IOT
          </p>
        </div>
        <div className="status">
          <h1 className="bg-gradient-to-r from-white to-[--yellow] to-100%">
            MQTT/API
          </h1>
          < p id="api">
            API Server: 10.10.10.10 
          </p>
          <p id="mqtt">
            MQTT Server: 10.10.10.10
          </p>
          <p id="topic">
            Main Topic: defTopic
          </p>
        </div>
        <div className="status">
          <h1 className="bg-gradient-to-r from-white to-[--red] to-100%">
           Motors / Sensors 
          </h1>
          <p id="override">
            Motor Override: None
          </p>
          <h2 className="font-extrabold text-white px-[25%]">
            Timig
          </h2>
          <p id="photoresistor">
            Photoresistor: 5 min
          </p>
          <p id="name">
            Accelerometer: 1 min 
          </p>
          <p id="name">
            Pressure     : 2 min 
          </p>
          <p id="name">
            Ultrasonic   : 20 s
          </p>
        </div>
      </div>
      
      
      {/* Contenedor Botones Fondo*/}
      <div className="mt-10 w-full h h-fit flex md:flex-row flex-wrap md:justify-between items-center sm:flex-col sm:justify-start">
        <SquareIconButton type='info' href="/info" width={100} height={100} />
        <SquareIconButton type='refresh' href="/" width={100} height={100} />
        <SquareIconButton type='controller' href="/controller" width={100} height={100} />

      </div>
    </div>
  );
}
