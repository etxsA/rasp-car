import React from "react";
import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

interface AreaChartProps {
  data: { name: string; temperature: number; pressure: number; altitude: number }[];
}

const AreaChartComponent: React.FC<AreaChartProps> = ({ data }) => {
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
        <Area
          type="monotone"
          dataKey="temperature"
          stackId="1"
          stroke="#3d010e"
          fill="#3d010e"
        />
        <Area
          type="monotone"
          dataKey="pressure"
          stackId="1"
          stroke="#b6042a" 
          fill="#b6042a" 
        />
        <Area
          type="monotone"
          dataKey="altitude"
          stackId="1"
          stroke="#f50538"
          fill="#f50538"
        />
      </AreaChart>
    </ResponsiveContainer>
  );
};

export default AreaChartComponent;
