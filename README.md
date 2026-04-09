<h1 align="center">👋 Hi, I'm Abdullah Shabbir</h1>
<h3 align="center">IoT & Embedded Systems Engineer — From schematic to cloud, I own the full stack.</h3>

<p align="center">
  📍 Genoa, Italy &nbsp;|&nbsp;
  ✉️ abdullahshabbir2@gmail.com &nbsp;|&nbsp;
  <a href="https://linkedin.com/in/abdullah-shabbir960373196">LinkedIn</a>
</p>

---

## 💼 About Me

- 🔧 I build end-to-end embedded products — schematic and PCB layout through firmware to cloud backend.
- 📡 I specialise in **low-power wearables**, **real-time RTOS systems**, and **wireless stacks** (BLE 5.0, LoRa, MQTT, CAN, GSM).
- 🧠 I own the full toolchain: **C/C++ firmware**, **EasyEDA PCB design**, **LTspice simulation**, **Python backends**, and **AWS IoT**.
- 🎓 Currently pursuing an **M.Sc. in Internet & Multimedia Engineering** at the University of Genoa, Italy.
- 💼 2+ years delivering 10+ commercial embedded products across healthcare, smart home, EV, and environmental-monitoring domains.

---

## 🧠 Expertise

- **🔲 Microcontrollers:** ESP32, ESP8266, STM32 (F1/F4), nRF52840 (Nordic), ARM Cortex-M, Raspberry Pi
- **⚙️ RTOS & Firmware:** FreeRTOS, Zephyr OS, ESP-IDF, bare-metal C — deterministic scheduling with sub-10 ms task jitter
- **📡 Wireless & Protocols:** BLE 5.0 (ACK-based, chunked transfer), LoRa, MQTT, GSM/LTE, CAN (ISO 11898), RS485/Modbus, NFC, OPC-UA
- **🖥️ PCB Design:** 8+ custom boards in EasyEDA — schematic → layout → DRC → Gerber → fabrication → bring-up; RF antenna placement, EMC best practices
- **☁️ Cloud & IoT Platforms:** AWS IoT Core, Azure IoT Hub, ThingsBoard, OpenRemote, Home Assistant
- **🐍 Backend:** Python (FastAPI/Flask), AWS Lambda, MQTT brokers, OTA pipelines
- **🔬 Simulation & Debug:** LTspice, oscilloscope, logic analyser, JTAG/OpenOCD

---

## 🚀 Tech Stack

**Microcontrollers & RTOS**

![ESP32](https://img.shields.io/badge/ESP32-000000?style=for-the-badge&logo=espressif&logoColor=white)
![STM32](https://img.shields.io/badge/STM32-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white)
![nRF52](https://img.shields.io/badge/nRF52840-00A9CE?style=for-the-badge&logo=nordicsemiconductor&logoColor=white)
![FreeRTOS](https://img.shields.io/badge/FreeRTOS-8CC84B?style=for-the-badge)
![Zephyr](https://img.shields.io/badge/Zephyr_OS-6A5ACD?style=for-the-badge)

**Languages**

![C](https://img.shields.io/badge/C-Expert-00599C?style=for-the-badge&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-Proficient-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Python](https://img.shields.io/badge/Python-Proficient-3776AB?style=for-the-badge&logo=python&logoColor=white)

**Wireless & Protocols**

![BLE](https://img.shields.io/badge/BLE_5.0-0082FC?style=for-the-badge&logo=bluetooth&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=mqtt&logoColor=white)
![LoRa](https://img.shields.io/badge/LoRa-00AEEF?style=for-the-badge)
![CAN](https://img.shields.io/badge/CAN_Bus-FF6600?style=for-the-badge)
![GSM](https://img.shields.io/badge/GSM%2FLTE-4CAF50?style=for-the-badge)
![RS485](https://img.shields.io/badge/RS485%2FModbus-555555?style=for-the-badge)

**Cloud & Tools**

![AWS IoT](https://img.shields.io/badge/AWS_IoT_Core-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Azure IoT](https://img.shields.io/badge/Azure_IoT_Hub-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Home Assistant](https://img.shields.io/badge/Home_Assistant-41BDF5?style=for-the-badge&logo=homeassistant&logoColor=white)
![PlatformIO](https://img.shields.io/badge/PlatformIO-FF7F00?style=for-the-badge&logo=platformio&logoColor=white)
![EasyEDA](https://img.shields.io/badge/EasyEDA-1B6CA8?style=for-the-badge)
![LTspice](https://img.shields.io/badge/LTspice-A50021?style=for-the-badge)

---

## 📂 Selected Projects

### 🔌 [ESP32 + Quectel M95 — MQTT over GSM](https://github.com/abdullahshabbir2/quectelm95_gsm_mqtt)
I drive a Quectel M95 GSM modem directly via AT commands from an ESP32 — no high-level library in the middle. I implemented the full sequence myself: PDP context activation → TCP connect → MQTT CONNECT handshake → PUBLISH with proper `>` prompt handling. A custom `GSM_MQTT` class wraps the AT protocol with response validation and state tracking.
`ESP32` `C++` `AT Commands` `MQTT` `GSM/GPRS` `PlatformIO`

---

### 🚰 [Smart Cistern & Irrigation Controller](https://github.com/abdullahshabbir2/home-assistant-cistern-integration)
A custom Python Home Assistant integration exposing 6-zone relays, timers, a water-level sensor, and settings as native Lovelace entities. I implemented two-tier automation: on-device rules (rain override, low-water cutoff) for offline resilience, and HA automations for complex multi-sensor cross-zone logic. Bidirectional HTTP state sync keeps the dashboard and hardware consistent at all times.
`ESP32` `Python` `Home Assistant` `MQTT` `HTTP`

---

### 💨 Smart Diffuser Platform — *Multi-PCB · BLE 5.0 + Wi-Fi*
3V/5V/12V PCB variants from a shared schematic with hardware-selectable power paths. ESP-IDF + FreeRTOS firmware with concurrent motor control (limit-switch feedback), RTC-based offline scheduling, and BLE 5.0 with ACK-based delivery, retries, and chunked transfer. **Zero field failures** across the initial production batch.
`ESP32` `ESP-IDF` `FreeRTOS` `BLE 5.0` `EasyEDA` `C`

---

### 👶 Infant Monitoring Wearable — *nRF52840 + Zephyr OS*
Medical-grade wearable for continuous infant SpO₂/HR (PPG) and motion (IMU) monitoring. My sensor-fusion pipeline suppressed movement artefacts; the power architecture achieved **<15 µA average in deep-sleep** with 5 s wake-acquire-transmit cycles. BLE 5.0 streamed processed physiological data to a gateway hub in real time.
`nRF52840` `Zephyr OS` `BLE 5.0` `PPG` `IMU` `C`

---

### 🚗 EV Battery Monitoring & Control System — *CAN + RTOS + GSM*
CAN bus (ISO 11898, 500 kbps) backbone for battery cell telemetry with FreeRTOS priority-partitioned tasks keeping battery switching logic at **sub-5 ms latency** with safe fail-state transitions. GSM cloud uplink, GPS tracking pipeline, and PZEM-004T smart metering over RS485/Modbus.
`STM32` `FreeRTOS` `CAN Bus` `GSM` `RS485` `Modbus` `C`

---

### 🧠 Parkinson's Monitoring System — *B.Sc. FYP · Distinction*
A two-tier distributed system: wearable IMU edge nodes extracted tremor frequency, amplitude, and gait features locally (**>90% data reduction** vs raw streaming) and transmitted over BLE to a Raspberry Pi fog node running a classification pipeline. The system operated fully offline, reducing round-trip latency ~70%.
`nRF52` `BLE 5.0` `Raspberry Pi` `Python` `IMU` `Edge ML` `C`

---

## 🖨️ PCB Design Highlights

I've taped out 8+ custom boards in EasyEDA — full workflow from schematic through layout, DRC, Gerber, fabrication, and bring-up.

- 📦 Multi-voltage product boards (3V/5V/12V) with shared schematic and hardware-selectable power paths
- 📶 NFC integration with RF keepout zones, impedance-matched traces, and ground plane management
- 🛰️ Ultra-compact GPS + LoRa/GSM tracker PCB (<30 g) with RF antenna trade-offs for range, isolation, and form factor
- ⌚ Wearable layouts: miniaturised power management and PPG/IMU sensor interfaces on nRF52-based designs
- 🔬 LTspice used alongside layout for power supply simulation and analog signal-path verification

---

## 🎓 Education

| Degree | Institution | Year |
|--------|------------|------|
| M.Sc. Internet & Multimedia Engineering | University of Genoa, Italy | 2024 – Present |
| B.Sc. Computer Engineering *(FYP — Distinction)* | COMSATS University Islamabad, Pakistan | 2019 – 2023 |

---

> *"The art of programming is the art of organising complexity."*
> — Edsger W. Dijkstra

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=abdullahshabbir2&show_icons=true&theme=default&hide_border=true&count_private=true" />
</p>
