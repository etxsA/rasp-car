"use client";

import { useEffect, useState } from "react";
import MainNavbar from "@/components/MainNavbar";
import mqtt from "mqtt";

export default function DevelopmentPage() {
  const [status, setStatus] = useState("");
  const [lastCommand, setLastCommand] = useState<string>(""); // Track the last command sent
  const [mqttClient, setMqttClient] = useState<mqtt.MqttClient | null>(null);
  const [pressedKeys, setPressedKeys] = useState<Set<string>>(new Set()); // Track currently pressed keys

  useEffect(() => {
    const mqttUrl = "wss://mqtt-dashboard.com:8884/mqtt";
    const options = {
      clientId: `clientId-${Math.random().toString(16).slice(2)}`, // Unique clientId
      keepalive: 60,
      clean: true,
      reconnectPeriod: 1000,
    };

    const client = mqtt.connect(mqttUrl, options);

    client.on("connect", () => {
      console.log("MQTT client connected");
      setMqttClient(client); // Set the client
    });

    client.on("error", (err) => {
      console.error("Connection error: ", err.message);
    });

    client.on("disconnect", () => {
      console.warn("MQTT client disconnected");
    });

    return () => {
      if (client) {
        client.end();
      }
    };
  }, []);

  const handleNavigation = (direction: string) => {
    if (!mqttClient) {
      console.error("MQTT client is not initialized");
      return;
    }

    if (!mqttClient.connected) {
      console.error("MQTT client is not connected");
      return;
    }

    if (lastCommand === direction) {
      return; // Avoid sending duplicate commands
    }

    setStatus(`Moving ${direction}`);
    mqttClient.publish("equipo3/control", direction.toUpperCase());
    setLastCommand(direction); // Update the last command
  };

  const startCounting = (direction: string) => {
    handleNavigation(direction);
  };

  const stopCounting = () => {
    handleNavigation("STOP");
    setLastCommand(""); // Reset last command to allow new commands
  };

  const handleKeyPress = (event: KeyboardEvent) => {
    const keyToCommand: Record<string, string> = {
      w: "FORWARD",
      a: "LEFT",
      s: "BACKWARD",
      d: "RIGHT",
    };

    const command = keyToCommand[event.key.toLowerCase()];

    if (command && !pressedKeys.has(event.key)) {
      setPressedKeys((prevKeys) => new Set(prevKeys).add(event.key)); // Mark key as pressed
      startCounting(command);
    }
    event.preventDefault(); // Prevent default browser behavior for specific keys
  };

  const handleKeyRelease = (event: KeyboardEvent) => {
    const keyToCommand: Record<string, string> = {
      w: "FORWARD",
      a: "LEFT",
      s: "BACKWARD",
      d: "RIGHT",
    };

    if (keyToCommand[event.key.toLowerCase()]) {
      setPressedKeys((prevKeys) => {
        const newKeys = new Set(prevKeys);
        newKeys.delete(event.key); // Mark key as released
        return newKeys;
      });
      stopCounting();
    }
    event.preventDefault(); // Prevent default browser behavior for specific keys
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
  }, [pressedKeys]); // Re-run effect when pressedKeys changes

  return (
    <div className="h-screen w-screen flex flex-col items-center">
      {/* Navigation Bar */}
      <MainNavbar />

      {/* Page Content */}
      <div className="flex flex-col items-center justify-center h-full w-full">
        <h1 className="text-2xl font-bold">MQTT Navigation</h1>
        <p className="text-gray-500 mt-2">
          Control navigation with the buttons below or WASD keys.
        </p>

        <div className="mt-8 grid grid-cols-3 gap-4">
          {/* Buttons with Mouse Events */}
          <div></div>
          <button
            onMouseDown={() => startCounting("FORWARD")}
            onMouseUp={stopCounting}
            className="flex items-center justify-center border-2 border-gray-400 rounded w-20 h-20"
          >
            W
          </button>
          <div></div>

          <button
            onMouseDown={() => startCounting("LEFT")}
            onMouseUp={stopCounting}
            className="flex items-center justify-center border-2 border-gray-400 rounded w-20 h-20"
          >
            A
          </button>
          <div></div>
          <button
            onMouseDown={() => startCounting("RIGHT")}
            onMouseUp={stopCounting}
            className="flex items-center justify-center border-2 border-gray-400 rounded w-20 h-20"
          >
            D
          </button>

          <div></div>
          <button
            onMouseDown={() => startCounting("BACKWARD")}
            onMouseUp={stopCounting}
            className="flex items-center justify-center border-2 border-gray-400 rounded w-20 h-20"
          >
            S
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
