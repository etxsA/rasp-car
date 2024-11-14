// component/MainNavbar.tsx
import LinkButton from "./LinkButton";
import Logo from "./Logo";

export default function MainNavbar() {

    return (
        <nav>
            <div className="flex flex-row items-center px-5 py-4 gap-2 \
            bg-[--navColor] border-[0.5px] boder-[#DCDCDC] shadow-[4px_4px_4px_rgba(0,0,0,0.3)] rounded-[8px]">
                {/* Logo Container */}
                <div className="flex flex-row items-center justify-center p-0 gap-8">
                    <Logo style="dark"></Logo>
                    {/* Links Container */}
                    <div className="ml-auto flex gap-4">
                        <LinkButton href="/photoresistor">
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
            </div>
        </nav>
    );
}
