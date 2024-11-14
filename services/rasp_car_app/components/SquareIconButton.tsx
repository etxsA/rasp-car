// components/SquareIconButton
// Set of all used Icon buttons to be used
import Link from "next/link";

type IconType = 
  | 'controller'
  | 'info'
  | 'refresh'
  | 'edit'
  | 'home'
  | 'menu'
  | 'dropdown'
  | 'filter'
  | 'poweroff'
  | 'restart'
  | 'key';
  

export default function SquareIconButton({type, href,  width, height}: Readonly<{
    type: IconType,
    href: string,
    width?: number,
    height?: number
    }>) {
    const setWidth = width ? width : 50;
    const setHeight =  height ? height: 50;
    const svgWidth = setWidth - 2 * (setWidth / 5);
    const svgHeight = setHeight - 2 * (setHeight / 5);

    let svg: React.ReactNode;

    switch (type) { 
        case 'controller':
            svg = (<svg className="aspect-[30/30]" width={svgWidth} height={svgHeight} viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M26.5257 10C25.6639 7.27004 24.2851 5.79358 22.6135 5.20074C22.1374 5.03186 21.627 5 21.1217 5H20.3561C19.2592 5 18.1892 5.34031 17.2939 5.97403L16.6665 6.41801C16.1792 6.76286 15.597 6.94805 15 6.94805C14.4031 6.94805 13.8209 6.76286 13.3336 6.41804L12.7062 5.97403C11.8108 5.34031 10.7408 5 9.6438 5H8.87821C8.37297 5 7.86261 5.03186 7.38643 5.20074C4.40806 6.25708 2.35936 10.1188 2.50755 18.8783C2.5374 20.6431 2.95037 22.5938 4.54278 23.3553C5.03901 23.5926 5.62083 23.75 6.28338 23.75C7.07841 23.75 7.70975 23.5234 8.19703 23.204C9.33941 22.4553 10.1765 21.2049 11.3891 20.5761C12.119 20.1976 12.9292 20 13.7514 20H16.2486C17.0707 20 17.881 20.1976 18.611 20.5761C19.8235 21.2049 20.6606 22.4553 21.803 23.204C22.2902 23.5234 22.9216 23.75 23.7166 23.75C24.3791 23.75 24.961 23.5926 25.4572 23.3553C27.0496 22.5938 27.4626 20.6431 27.4925 18.8783C27.5165 17.4601 27.4829 16.1703 27.397 15" stroke="#DCDCDC" strokeLinecap="round"/>
            <path d="M9.375 11.25V15M7.5 13.125H11.25" stroke="#DCDCDC" strokeLinecap="round"/>
            <path d="M23.875 12.875C23.875 13.4273 23.4273 13.875 22.875 13.875C22.3227 13.875 21.875 13.4273 21.875 12.875C21.875 12.3227 22.3227 11.875 22.875 11.875C23.4273 11.875 23.875 12.3227 23.875 12.875Z" fill="#DCDCDC"/>
            <path d="M20.125 12.875C20.125 13.4273 19.6773 13.875 19.125 13.875C18.5727 13.875 18.125 13.4273 18.125 12.875C18.125 12.3227 18.5727 11.875 19.125 11.875C19.6773 11.875 20.125 12.3227 20.125 12.875Z" fill="#DCDCDC"/>
            <path d="M21 10C21.5523 10 22 10.4477 22 11C22 11.5523 21.5523 12 21 12C20.4477 12 20 11.5523 20 11C20 10.4477 20.4477 10 21 10Z" fill="#DCDCDC"/>
            <path d="M21 13.75C21.5523 13.75 22 14.1977 22 14.75C22 15.3023 21.5523 15.75 21 15.75C20.4477 15.75 20 15.3023 20 14.75C20 14.1977 20.4477 13.75 21 13.75Z" fill="#DCDCDC"/>
            </svg>);
            break; 
            
        case 'info':
            svg = (<svg className="aspect-[30/30]" width={svgWidth} height={svgHeight} viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M15 21.25V13.75" stroke="#DCDCDC" strokeWidth="1.875" strokeLinecap="round"/>
                <path d="M15 8.75C15.6904 8.75 16.25 9.30964 16.25 10C16.25 10.6904 15.6904 11.25 15 11.25C14.3096 11.25 13.75 10.6904 13.75 10C13.75 9.30964 14.3096 8.75 15 8.75Z" fill="#DCDCDC"/>
                <path d="M8.75 4.17228C10.5886 3.10871 12.7232 2.5 15 2.5C21.9035 2.5 27.5 8.09644 27.5 15C27.5 21.9035 21.9035 27.5 15 27.5C8.09644 27.5 2.5 21.9035 2.5 15C2.5 12.7232 3.10871 10.5886 4.17228 8.75" stroke="#DCDCDC" strokeWidth="1.875" strokeLinecap="round"/>
                </svg>
                );
            break;
        case 'refresh':
            svg = (<svg className="aspect-[30/30]" width={svgWidth} height={svgHeight} viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M13.75 2.5L16.25 4.99431L16.176 5.06842M16.176 5.06842L13.75 7.5M16.176 5.06842C15.7904 5.02324 15.3979 5 15 5C9.47715 5 5 9.47715 5 15C5 18.158 6.46384 20.9741 8.75 22.8067M16.25 22.5001L13.75 24.8885L13.7871 24.9271M13.7871 24.9271C14.1846 24.9752 14.5895 25 15 25C20.5229 25 25 20.5229 25 15C25 11.842 23.5361 9.02594 21.25 7.19329M13.7871 24.9271L16.25 27.5001" stroke="#DCDCDC" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
                );
            break;
        case 'edit':
            svg = (<svg className="aspect-[30/30]" width={svgWidth} height={svgHeight} viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M26.5999 8.00006L14.6749 19.925C13.4874 21.1125 9.96234 21.6625 9.17484 20.875C8.38734 20.0875 8.92484 16.5625 10.1123 15.375L22.0499 3.43753C22.3443 3.11635 22.7006 2.85818 23.0976 2.67855C23.4945 2.49893 23.9238 2.40155 24.3594 2.39238C24.7949 2.38321 25.2279 2.46239 25.632 2.62515C26.0361 2.78791 26.4031 3.03091 26.7108 3.33941C27.0184 3.64791 27.2604 4.01554 27.422 4.42011C27.5836 4.8247 27.6618 5.25783 27.6514 5.69339C27.641 6.12895 27.5424 6.55794 27.3618 6.95438C27.181 7.35081 26.9219 7.70655 26.5999 8.00006Z" stroke="#DCDCDC" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <path d="M13.75 5H7.5C6.17391 5 4.90222 5.52677 3.96454 6.46446C3.02686 7.40215 2.5 8.67391 2.5 10V22.5C2.5 23.8261 3.02686 25.0979 3.96454 26.0355C4.90222 26.9732 6.17391 27.5 7.5 27.5H21.25C24.0125 27.5 25 25.25 25 22.5V16.25" stroke="#DCDCDC" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
                );
            break;
        case 'home':
            svg = (<svg className="aspect-[30/30]" width={svgWidth} height={svgHeight} viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M27.5 27.5H2.5" stroke="#DCDCDC" strokeWidth="2" strokeLinecap="round"/>
                <path d="M2.5 13.75L7.5787 9.6871M27.5 13.75L17.3426 5.62414C15.973 4.52849 14.027 4.52849 12.6574 5.62414L11.68 6.40607" stroke="#DCDCDC" strokeWidth="2" strokeLinecap="round"/>
                <path d="M19.375 6.875V4.375C19.375 4.02982 19.6549 3.75 20 3.75H23.125C23.4701 3.75 23.75 4.02982 23.75 4.375V10.625" stroke="#DCDCDC" strokeWidth="2" strokeLinecap="round"/>
                <path d="M5 27.5V11.875" stroke="#DCDCDC" strokeWidth="2" strokeLinecap="round"/>
                <path d="M25 11.875V16.875M25 27.5V21.875" stroke="#DCDCDC" strokeWidth="2" strokeLinecap="round"/>
                <path d="M18.75 27.5V21.25C18.75 19.4823 18.75 18.5984 18.2009 18.0491C17.6516 17.5 16.7677 17.5 15 17.5C13.2323 17.5 12.3483 17.5 11.7992 18.0491M11.25 27.5V21.25" stroke="#DCDCDC" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                <path d="M17.5 11.875C17.5 13.2557 16.3807 14.375 15 14.375C13.6193 14.375 12.5 13.2557 12.5 11.875C12.5 10.4943 13.6193 9.375 15 9.375C16.3807 9.375 17.5 10.4943 17.5 11.875Z" stroke="#DCDCDC" strokeWidth="2"/>
                </svg>
                )
            break;
        case 'menu':
            svg = (<svg className="aspect-[30/30]" width={svgWidth} height={svgHeight} viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M5 7.5H25M5 15H25M5 22.5H25" stroke="#DCDCDC" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
                );
            break;
        case 'dropdown':
            svg = (<svg  className="aspect-[30/30]" width={svgWidth} height={svgHeight} viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M15.8839 18.3839C15.3958 18.872 14.6042 18.872 14.1161 18.3839L7.86611 12.1339C7.37796 11.6457 7.37796 10.8543 7.86611 10.3661C8.35427 9.87796 9.14572 9.87796 9.63389 10.3661L15 15.7323L20.3661 10.3661C20.8542 9.87796 21.6458 9.87796 22.1339 10.3661C22.622 10.8543 22.622 11.6457 22.1339 12.1339L15.8839 18.3839Z" fill="#DCDCDC"/>
                </svg>
                );
            break; 
        case 'filter':
            svg = (<svg className="aspect-[30/30]" width={svgWidth} height={svgHeight} viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M25 7.00013C25 6.30006 24.9995 5.94976 24.8633 5.68237C24.7435 5.44717 24.5529 5.25609 24.3178 5.13624C24.0504 5 23.6996 5 22.9995 5H6.99951C6.29945 5 5.94976 5 5.68237 5.13624C5.44717 5.25609 5.25609 5.44717 5.13624 5.68237C5 5.94976 5 6.30006 5 7.00013V7.9217C5 8.22744 5 8.38041 5.03454 8.52427C5.06516 8.65182 5.11579 8.77366 5.18432 8.8855C5.2616 9.0116 5.36989 9.11989 5.58594 9.33594L11.9144 15.6644C12.1305 15.8805 12.238 15.988 12.3153 16.1143C12.3839 16.226 12.4352 16.3483 12.4658 16.4759C12.5 16.6183 12.5 16.7694 12.5 17.069V23.0137C12.5 24.0852 12.5 24.6214 12.7256 24.944C12.9228 25.2258 13.2268 25.4138 13.5669 25.464C13.9564 25.5215 14.4359 25.2821 15.3943 24.803L16.3943 24.303C16.7956 24.1024 16.9957 24.0016 17.1424 23.8519C17.272 23.7195 17.3713 23.5606 17.4316 23.3855C17.5 23.1874 17.5 22.9625 17.5 22.5137V17.0782C17.5 16.7725 17.5 16.6198 17.5345 16.4759C17.5651 16.3483 17.6158 16.226 17.6844 16.1143C17.7611 15.9889 17.8684 15.8816 18.0816 15.6684L18.086 15.6644L24.4144 9.33594C24.6305 9.11975 24.738 9.01165 24.8154 8.8855C24.8839 8.77366 24.9353 8.65182 24.9659 8.52427C25 8.38189 25 8.23055 25 7.931V7.00013Z" stroke="#DCDCDC" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
                );
            break;
        case 'poweroff':
            svg = (<svg className="aspect-[30/30]" width={svgWidth} height={svgHeight} viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M15 3V13.5" stroke="#DCDCDC" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"/>
                <path d="M7.80002 6C-0.899978 14.4 4.80002 27 15.3 27C23.7 27 26.7 20.1 26.7 15.6C26.7 11.1 24.3 7.8 22.2 6" stroke="#DCDCDC" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
                );
            break;
        case 'restart':
            svg = (<svg className="aspect-[30/30]" width={svgWidth} height={svgHeight} viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g clip-path="url(#clip0_3754_325)">
                <mask id="mask0_3754_325" style="mask-type:luminance" maskUnits="userSpaceOnUse" x="0" y="0" width="30" height="30">
                <path d="M30 0H0V30H30V0Z" fill="white"/>
                </mask>
                <g mask="url(#mask0_3754_325)">
                <path d="M24.6606 13.661C25.5516 16.9973 24.6884 20.7044 22.0711 23.3216C18.9747 26.418 14.3532 27.0594 10.625 25.2458M22.955 10.0634L22.0711 9.17951C18.1659 5.27428 11.8342 5.27428 7.92893 9.17951C4.28703 12.8214 4.04145 18.5735 7.19218 22.5M22.955 10.0634H17.6516M22.955 10.0634V4.7601" stroke="#DCDCDC" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"/>
                </g>
                </g>
                <defs>
                <clipPath id="clip0_3754_325">
                <rect width="30" height="30" fill="white"/>
                </clipPath>
                </defs>
                </svg>
                );
                break; 
            case 'key':
                svg = (<svg className="aspect-[27/30]" width={svgWidth} height={svgHeight} viewBox="0 0 27 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd" clip-rule="evenodd" d="M18.5708 16.8781C23.2262 16.8781 27 13.0998 27 8.43903C27 3.77828 23.2262 0 18.5708 0C13.9155 0 10.1417 3.77828 10.1417 8.43903C10.1417 10.0903 10.6154 11.6309 11.4342 12.9319L0 24.3794L5.61404 30L8.26309 27.3479L5.29808 24.3794L8.26851 21.4055L11.2335 24.374L13.8826 21.7219L10.9175 18.7534L14.0833 15.584C15.3827 16.4038 16.9215 16.8781 18.5708 16.8781ZM18.5708 13.1274C21.1571 13.1274 23.2537 11.0283 23.2537 8.43903C23.2537 5.84973 21.1571 3.75068 18.5708 3.75068C15.9846 3.75068 13.888 5.84973 13.888 8.43903C13.888 11.0283 15.9846 13.1274 18.5708 13.1274Z" fill="#DCDCDC"/>
                    </svg>
                    );
                break;
        default:
            svg = (<svg width={svgWidth} height={svgHeight} viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M15 21.25V13.75" stroke="#DCDCDC" strokeWidth="1.875" strokeLinecap="round"/>
                <path d="M15 8.75C15.6904 8.75 16.25 9.30964 16.25 10C16.25 10.6904 15.6904 11.25 15 11.25C14.3096 11.25 13.75 10.6904 13.75 10C13.75 9.30964 14.3096 8.75 15 8.75Z" fill="#DCDCDC"/>
                <path d="M8.75 4.17228C10.5886 3.10871 12.7232 2.5 15 2.5C21.9035 2.5 27.5 8.09644 27.5 15C27.5 21.9035 21.9035 27.5 15 27.5C8.09644 27.5 2.5 21.9035 2.5 15C2.5 12.7232 3.10871 10.5886 4.17228 8.75" stroke="#DCDCDC" strokeWidth="1.875" strokeLinecap="round"/>
                </svg>
                );
            break; 

    }

    return (
    <Link href={href} style={{width: setWidth, height: setHeight}} className="square-icon-button">
        {svg}
    </Link>
    );
    
};