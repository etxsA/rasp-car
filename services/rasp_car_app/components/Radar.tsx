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
        <XAxis dataKey="name" scale="band" />
        <YAxis />
        <Tooltip />
        <Legend />

        {/* Bars */}
        <Bar dataKey="x" barSize={20} fill="#630015" name="X Axis" />
        <Bar dataKey="y" barSize={20} fill="#b6042a" name="Y Axis" />
        <Bar dataKey="z" barSize={20} fill="#f50538" name="Z Axis" />

        {/* Lines */}
        <Line type="monotone" dataKey="x" stroke="#630015" name="X Trend" />
        <Line type="monotone" dataKey="y" stroke="#b6042a" name="Y Trend" />
        <Line type="monotone" dataKey="z" stroke="#f50538" name="Z Trend" />
      </ComposedChart>
    </ResponsiveContainer>
  );
};

export default ComposedChartComponent;
