// components/Chart.tsx
"use client";

import React from 'react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts';

type ChartProps = {
  data: Array<{ name: string; value: number }>;
};

const Chart: React.FC<ChartProps> = ({ data }) => (
  <ResponsiveContainer width="100%" height="100%">
    <LineChart data={data}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="name" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey="value" stroke="#b6042a" name="voltage"/>
    </LineChart>
  </ResponsiveContainer>
);

export default Chart;
