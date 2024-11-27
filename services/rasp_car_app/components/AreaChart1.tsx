import React from "react";
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from "recharts";

interface AreaChartProps {
  data: { name: string; temperature: number; pressure: number; altitude: number }[];
  dataKey: string; // Dynamic data key (e.g., "temperature", "pressure", etc.)
  color: string;   // Area color
}

const AreaChartComponent: React.FC<AreaChartProps> = ({ data, dataKey, color }) => {
  return (
    <ResponsiveContainer width="100%" height="100%">
      <AreaChart
        data={data}
        margin={{
          top: 10,
          right: 30,
          left: 0,
          bottom: 0,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Area type="monotone" dataKey={dataKey} stroke={color} fill={color} />
      </AreaChart>
    </ResponsiveContainer>
  );
};

export default AreaChartComponent;
