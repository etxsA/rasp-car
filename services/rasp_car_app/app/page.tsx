import MainNavbar from "@/components/MainNavbar";
import Chart from "@/components/Chart";


const data1 = [
  { name: 'Jan', value: 30 },
  { name: 'Feb', value: 20 },
  { name: 'Mar', value: 50 },
  { name: 'Apr', value: 40 },
  { name: 'May', value: 80 },
  { name: 'Jun', value: 70 },
];

const data2 = [
  { name: 'Jan', value: 60 },
  { name: 'Feb', value: 30 },
  { name: 'Mar', value: 80 },
  { name: 'Apr', value: 50 },
  { name: 'May', value: 40 },
  { name: 'Jun', value: 90 },
];


export default function Home() {
  return (
    <div className="h-screen w-screen flex flex-col flex-nowrap gap-5 py-5 px-40 justify-start items-center" >
      <MainNavbar />
      {/* Contenedor de las dos primeras gráficas */}
      <div className="flex flex-row flex-wrap justify-center items-center gap-1 w-full">
        <div className="w-72 h-72">
          <Chart data={data1} />
        </div>
        <div className="w-72 h-72">
          <Chart data={data2} />
        </div>
        <div className="w-72 h-72">
          <Chart data={data1} />
        </div>
        <div className="w-72 h-72">
          <Chart data={data1} />
        </div>
      </div>

      {/* Status Bar */}
      <div className="w-full min-h-40">
        Hi Hola como estas
      </div>

      {/* Gráfica adicional debajo */}
    
      <h1>HOLI</h1>
    </div>
  );
}
