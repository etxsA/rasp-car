import MainNavbar from "@/components/MainNavbar";
import Chart from "@/components/Chart";
import SquareIconButton from "@/components/SquareIconButton";


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
        <div className="w-64 h-64">
          <Chart data={data1} />
        </div>
        <div className="w-64 h-64">
          <Chart data={data2} />
        </div>
        <div className="w-64 h-64">
          <Chart data={data1} />
        </div>
        <div className="w-64 h-64">
          <Chart data={data1} />
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
        <SquareIconButton type='refresh' href="/refresh" width={100} height={100} />
        <SquareIconButton type='controller' href="/controller" width={100} height={100} />

      </div>
    </div>
  );
}
