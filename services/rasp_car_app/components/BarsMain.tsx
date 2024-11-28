import React from "react";
import {
  ComposedChart,
  Line,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

interface ComposedChartProps {
  data: { name: string; x: number; y: number; z: number }[];
}

const ComposedChartComponent: React.FC<ComposedChartProps> = ({ data }) => {
  return (
    <ResponsiveContainer width="100%" height="100%">
      <ComposedChart
        data={data}
        margin={{
          top: 20,
          right: 20,
          bottom: 20,
          left: 20,
        }}
      >
        {/* Grid and Axes */}
        <CartesianGrid stroke="#f5f5f5" />
        <XAxis dataKey="name" scale="band" tick={false} />
        <YAxis />
        <Tooltip />
        <Legend />

        {/* Bars */}
        <Bar dataKey="x" barSize={10} fill="#630015" />
        <Bar dataKey="y" barSize={10} fill="#b6042a" />
        <Bar dataKey="z" barSize={10} fill="#f50538" />

        {/* Lines */}
        <Line type="monotone" stroke="#630015" />
        <Line type="monotone" stroke="#b6042a" />
        <Line type="monotone" stroke="#f50538" />
      </ComposedChart>
    </ResponsiveContainer>
  );
};

export default ComposedChartComponent;
