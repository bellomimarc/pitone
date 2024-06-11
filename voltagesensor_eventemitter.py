import asyncio
import random

from pyventus import EventEmitter, EventLinker, AsyncIOEventEmitter

class VoltageSensor:

    def __init__(self, name: str, low: float, high: float, event_emitter: EventEmitter) -> None:
        # Initialize the VoltageSensor object with the provided parameters
        self._name: str = name
        self._low: float = low
        self._high: float = high
        self._event_emitter: EventEmitter = event_emitter

    async def __call__(self) -> None:
        # Start voltage readings for the sensor
        print(f"Starting voltage readings for: {self._name}")
        print(f"Low: {self._low:.3g}v | High: {self._high:.3g}v\n-----------\n")

        while True:
            # Simulate sensor readings
            voltage: float = random.uniform(0, 5)
            print("\tSensor Reading:", "\033[32m", f"{voltage:.3g}v", "\033[0m")

            # Emit events based on voltage readings
            if voltage < self._low:
                self._event_emitter.emit("LowVoltageEvent", sensor=self._name, voltage=voltage)
            elif voltage > self._high:
                self._event_emitter.emit("HighVoltageEvent", sensor=self._name, voltage=voltage)

            await asyncio.sleep(1)


@EventLinker.on("LowVoltageEvent")
def handle_low_voltage_event(sensor: str, voltage: float):
    print(f"🪫 Turning on eco-mode for '{sensor}'. ({voltage:.3g}v)\n")
    # Perform action for low voltage...


@EventLinker.on("HighVoltageEvent")
async def handle_high_voltage_event(sensor: str, voltage: float):
    print(f"⚡ Starting high-voltage protection for '{sensor}'. ({voltage:.3g}v)\n")
    # Perform action for high voltage...


@EventLinker.on("LowVoltageEvent", "HighVoltageEvent")
def handle_voltage_event(sensor: str, voltage: float):
    print(f"\033[31m\nSensor '{sensor}' out of range.\033[0m (Voltage: {voltage:.3g})")
    # Perform notification for out of range voltage...


async def main():
    # Initialize the sensor and run the sensor readings
    sensor = VoltageSensor(name="PressureSensor", low=0.5, high=3.9, event_emitter=AsyncIOEventEmitter())
    await asyncio.gather(sensor(), )  # Add new sensors inside the 'gather' for multi-device monitoring


asyncio.run(main())