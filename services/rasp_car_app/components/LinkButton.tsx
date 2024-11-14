//components//LinkButton.tsx
// A simple implementation of button 

import Link from "next/link";
import React from "react";

interface LinkButtonProps {
    href: string, 
    children: React.ReactNode
}

export default function LinkButton ({href, children}: LinkButtonProps) {

    return (<Link href={href} className="linkButton">
        {children}
    </Link>
    ); 
};