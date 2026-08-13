<h1 align="center">Hi, I'm Abdullah Shabbir</h1>

<p align="center">
  <strong>IoT & Embedded Systems Engineer</strong><br>
  From schematic and PCB layout to firmware, wireless connectivity, cloud, and dashboards.
</p>

<p align="center">
  Genoa, Italy |
  <a href="mailto:abdullahshabbir2@gmail.com">abdullahshabbir2@gmail.com</a> |
  <a href="https://linkedin.com/in/abdullahshabbir2">LinkedIn</a>
</p>

---

## 💼 About Me

🔧 I'm an <strong>IoT & Embedded Systems Engineer</strong> focused on building connected hardware products end to end.

📡 I specialize in <strong>ESP32, STM32, nRF52, BLE 5.0, GSM/GPRS, LoRa, MQTT, CAN, and RS485/Modbus</strong>.

🧠 I work across <strong>firmware, PCB design, sensor integration, RTOS systems, cloud APIs, and device dashboards</strong>.

🎓 Currently pursuing an <strong>M.Sc. in Internet and Multimedia Engineering</strong> at the University of Genoa, Italy.

🚀 2+ years delivering commercial embedded products across healthcare, smart home, EV, and environmental-monitoring domains.

---

## 🧠 Expertise

- 📦 <strong>Embedded Firmware:</strong> C, C++, ESP-IDF, FreeRTOS, Zephyr OS, bare-metal embedded C
- 🔌 <strong>Microcontrollers:</strong> ESP32, ESP8266, STM32, nRF52840, ARM Cortex-M, Raspberry Pi
- 📶 <strong>Wireless & Protocols:</strong> BLE 5.0, MQTT, GSM/GPRS/LTE, LoRa, CAN, RS485/Modbus, NFC
- 🧩 <strong>PCB Design:</strong> EasyEDA schematic/layout, DRC, Gerbers, fabrication handoff, bring-up, RF-aware layouts
- ☁️ <strong>Cloud & Backend:</strong> Python, FastAPI, Flask, AWS IoT Core, Azure IoT Hub, Home Assistant, ThingsBoard
- 🛠️ <strong>Debug & Simulation:</strong> LTspice, oscilloscope, logic analyzer, JTAG/OpenOCD, PlatformIO

---

## 🚀 Tech Stack

<p>
  <img alt="ESP32" src="https://img.shields.io/badge/ESP32-000000?style=for-the-badge&logo=espressif&logoColor=white">
  <img alt="STM32" src="https://img.shields.io/badge/STM32-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white">
  <img alt="nRF52" src="https://img.shields.io/badge/nRF52-00A9CE?style=for-the-badge&logo=nordicsemiconductor&logoColor=white">
  <img alt="C" src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white">
  <img alt="C++" src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Java" src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white">
  <img alt="FreeRTOS" src="https://img.shields.io/badge/FreeRTOS-8CC84B?style=for-the-badge">
  <img alt="Zephyr OS" src="https://img.shields.io/badge/Zephyr_OS-6A5ACD?style=for-the-badge">
  <img alt="BLE" src="https://img.shields.io/badge/BLE_5.0-0082FC?style=for-the-badge&logo=bluetooth&logoColor=white">
  <img alt="MQTT" src="https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=mqtt&logoColor=white">
  <img alt="LoRa" src="https://img.shields.io/badge/LoRa-00AEEF?style=for-the-badge">
  <img alt="CAN" src="https://img.shields.io/badge/CAN_Bus-FF6600?style=for-the-badge">
  <img alt="AWS IoT" src="https://img.shields.io/badge/AWS_IoT_Core-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white">
  <img alt="Home Assistant" src="https://img.shields.io/badge/Home_Assistant-41BDF5?style=for-the-badge&logo=homeassistant&logoColor=white">
  <img alt="PlatformIO" src="https://img.shields.io/badge/PlatformIO-FF7F00?style=for-the-badge&logo=platformio&logoColor=white">
  <img alt="EasyEDA" src="https://img.shields.io/badge/EasyEDA-1B6CA8?style=for-the-badge">
</p>

---

## 📂 Projects

#### 🚗 EV Battery Monitoring & Control System

FreeRTOS-based battery telemetry and switching control over CAN bus, with GSM cloud uplink, GPS tracking, RS485/Modbus metering, and safe fail-state handling for battery-side control logic.

`STM32` `FreeRTOS` `CAN` `GSM` `GPS` `RS485` `Modbus` `C`

#### 🌬️ [Smart Air Purifier & Air Quality Monitor](https://github.com/abdullahshabbir2/AirPurifier)

ESP32 purifier firmware that computes a US EPA Air Quality Index on-device from particulate, CO, NO2, temperature, and humidity sensors, then drives the fan to match through hysteresis-damped PWM speed control. Publishes telemetry over both a versioned REST API and a NimBLE GATT service with notifications, provisions WiFi from a phone over BLE, and ships a dependency-free AQI engine covered by 120 host unit tests in CI.

`ESP32` `ESP-IDF` `FreeRTOS` `BLE 5.0` `NimBLE` `REST API` `LEDC PWM` `Unit Testing` `GitHub Actions` `C`

#### 🌱 [Smart IoT Greenhouse System](https://github.com/abdullahshabbir2/Smart_IoT_GreenHouse)

Dual-node ESP32 greenhouse automation system with independent local dashboards, REST APIs, mDNS discovery, NVS persistence, watchdog recovery, CORS support, fan hysteresis, pump scheduling, low-water lockout, and rain-based irrigation protection.

`ESP32` `C++` `PlatformIO` `REST API` `mDNS` `NVS` `Watchdog` `IoT Dashboard`

#### 🚰 [Smart Cistern & Irrigation Controller](https://github.com/abdullahshabbir2/home-assistant-cistern-integration)

Custom Home Assistant integration plus ESP32 firmware for cistern monitoring, relay control, irrigation scheduling, telemetry polling, Zeroconf discovery, coordinator-based updates, and Lovelace dashboard entities.

`ESP32` `Python` `Home Assistant` `Arduino` `REST/JSON` `Lovelace` `Automation`

#### 🔌 [ESP32 + Quectel M95 - MQTT over GSM](https://github.com/abdullahshabbir2/quectelm95_gsm_mqtt)

Bare-metal ESP32 firmware that drives a Quectel M95 GSM modem directly through AT commands. It handles PDP context activation, TCP transport setup, MQTT CONNECT/PUBLISH flow, response validation, and the two-step `QMTPUB` payload prompt sequence.

`ESP32` `C++` `AT Commands` `MQTT` `GSM/GPRS` `UART` `PlatformIO`

#### 🧠 Parkinson's Monitoring System


`nRF52` `BLE 5.0` `Raspberry Pi` `Python` `IMU` `Edge ML`

#### 🛒 [Grocery Warehouse Inventory System](https://github.com/abdullahshabbir2/Grocery-WareHouse)

Java Swing desktop inventory system with MySQL-backed create, read, update, and delete flows for grocery items, plus a Jupyter Notebook component for data-oriented work in the same repository.

`Java` `Swing` `MySQL` `JDBC` `CRUD` `Jupyter Notebook`

---

## 🖨️ PCB Design Highlights

- 📦 Multi-voltage product boards with shared schematics and hardware-selectable power paths
- 📶 NFC layouts with RF keepout zones, impedance-aware routing, and ground-plane control
- 🛰️ Compact GPS + LoRa/GSM tracker PCB design under 30 g
- 🔬 Power-supply and analog signal-path verification with LTspice

---

## 🎓 Education

| Degree | Institution | Year |
| --- | --- | --- |
| M.Sc. Internet and Multimedia Engineering | University of Genoa, Italy | 2024 - Present |
| B.Sc. Computer Engineering, FYP Distinction | COMSATS University Islamabad, Pakistan | 2019 - 2023 |
