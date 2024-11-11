import Image from "next/image";

// Components
import MainNavbar from "@/components/MainNavbar";

export default function Home() {
  return (
    <div className="h-screen w-screen flex flex-col flex-nowrap gap-5 py-5 px-40 justify-start items-center" >
      <MainNavbar />
    </div>
  );
}
