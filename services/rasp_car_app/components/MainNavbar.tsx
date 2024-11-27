// component/MainNavbar.tsx
import LinkButton from "./LinkButton";
import Logo from "./Logo";

export default function MainNavbar() {

    return (
        <nav>
            <div className="flex flex-row flex-wrap items-center px-5 py-4 gap-2 \
            bg-[--navColor] border-[0.5px] boder-[#DCDCDC] shadow-[4px_4px_4px_rgba(0,0,0,0.3)] rounded-[8px]">
                {/* Logo Container */}
                <div className="flex flex-row items-center justify-center p-0 gap-8">
                    <Logo style="light"></Logo>
                    <h1 className="rasp-car">Rasp-Car</h1>
                </div>

                {/* Links Container */}
                <div className="flex flex-row flex-wrap gap-4 md:justify-center md:items-center sm:items-center sm:justify-start">
                    <LinkButton href="/dashboard?s=photoresistor">
                        Photoresistor
                    </LinkButton> 
                    <LinkButton href="/accelerometer">
                        Accelerometer
                    </LinkButton>
                    <LinkButton href="/distance">
                        Distance
                    </LinkButton>
                    <LinkButton href="/pressure">
                        Pressure
                    </LinkButton>  
                </div>
            </div>
        </nav>
    );
}
