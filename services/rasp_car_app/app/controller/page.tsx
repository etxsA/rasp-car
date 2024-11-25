"use client";

import { useEffect, useState } from "react";
import MainNavbar from "@/components/MainNavbar";

export default function DevelopmentPage() {
  const [status, setStatus] = useState("");
  const [counter, setCounter] = useState(0); // Counter for continuous increment
  const [intervalId, setIntervalId] = useState<NodeJS.Timeout | null>(null);

  const handleNavigation = (direction: string) => {
    setStatus(`Moving ${direction}`);
    console.log(`Moving ${direction}`);
    // Add MQTT publishing logic here if needed
  };

  const startCounting = (direction: string) => {
    // Start incrementing the counter
    handleNavigation(direction);
    if (!intervalId) {
      const id = setInterval(() => {
        setCounter((prev) => prev + 1); // Use functional update for the correct counter value
      }, 100); // Adjust interval for faster/slower increment
      setIntervalId(id);
    }
  };

  const stopCounting = () => {
    // Stop incrementing
    if (intervalId) {
      clearInterval(intervalId);
      setIntervalId(null);
    }
  };

  const handleKeyPress = (event: KeyboardEvent) => {
    switch (event.key) {
      case "ArrowUp":
        startCounting("forward");
        break;
      case "ArrowDown":
        startCounting("backward");
        break;
      case "ArrowLeft":
        startCounting("left");
        break;
      case "ArrowRight":
        startCounting("right");
        break;
      default:
        break;
    }
  };

  const handleKeyRelease = (event: KeyboardEvent) => {
    stopCounting();
  };

  useEffect(() => {
    // Attach keyboard event listeners
    window.addEventListener("keydown", handleKeyPress);
    window.addEventListener("keyup", handleKeyRelease);

    // Cleanup event listeners on component unmount
    return () => {
      window.removeEventListener("keydown", handleKeyPress);
      window.removeEventListener("keyup", handleKeyRelease);
    };
  }, [intervalId]); // Depend on intervalId to ensure proper cleanup

  return (
    <div className="h-screen w-screen flex flex-col items-center">
      {/* Navigation Bar */}
      <MainNavbar />

      {/* Page Content */}
      <div className="flex flex-col items-center justify-center h-full w-full">
        <h1 className="text-2xl font-bold">MQTT Navigation</h1>
        <p className="text-gray-500 mt-2">
          Control navigation with the buttons below or arrow keys. Counter: {counter}
        </p>

        <div className="mt-8 grid grid-cols-3 gap-4">
          {/* Buttons with Mouse Events */}
          <div></div>
          <button
            onMouseDown={() => startCounting("forward")}
            onMouseUp={stopCounting}
            onMouseLeave={stopCounting}
            className="flex items-center justify-center border-2 border-gray-400 rounded w-20 h-20"
          >
            ↑
          </button>
          <div></div>

          <button
            onMouseDown={() => startCounting("left")}
            onMouseUp={stopCounting}
            onMouseLeave={stopCounting}
            className="flex items-center justify-center border-2 border-gray-400 rounded w-20 h-20"
          >
            ←
          </button>
          <div></div>
          <button
            onMouseDown={() => startCounting("right")}
            onMouseUp={stopCounting}
            onMouseLeave={stopCounting}
            className="flex items-center justify-center border-2 border-gray-400 rounded w-20 h-20"
          >
            →
          </button>

          <div></div>
          <button
            onMouseDown={() => startCounting("backward")}
            onMouseUp={stopCounting}
            onMouseLeave={stopCounting}
            className="flex items-center justify-center border-2 border-gray-400 rounded w-20 h-20"
          >
            ↓
          </button>
          <div></div>
        </div>

        {/* Status Message */}
        {status && (
          <div className="mt-5 text-green-500">
            <p>{status}</p>
          </div>
        )}
      </div>
    </div>
  );
}
