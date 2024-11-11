// pages/dashboard.tsx
import MainNavbar from "@/components/MainNavbar";
import Chart from "@/components/Chart";

const data = [
  { name: 'Jan', value: 50 },
  { name: 'Feb', value: 40 },
  { name: 'Mar', value: 70 },
  { name: 'Apr', value: 60 },
  { name: 'May', value: 90 },
  { name: 'Jun', value: 80 },
];

export default function Dashboard() {
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
