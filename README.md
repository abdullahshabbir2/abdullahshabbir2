<h1 align="center">Abdullah Shabbir</h1>
<h3 align="center">IoT & Embedded Systems Engineer</h3>

<p align="center">
  <a href="mailto:abdullahshabbir2@gmail.com">abdullahshabbir2@gmail.com</a> &nbsp;·&nbsp;
  Genoa, Italy &nbsp;·&nbsp;
  <a href="https://linkedin.com/in/abdullah-shabbir960373196">LinkedIn</a> &nbsp;·&nbsp;
  <a href="https://github.com/abdullahshabbir2">GitHub</a>
</p>

---

## About Me

I'm an IoT and Embedded Systems Engineer with 2+ years building end-to-end embedded products — from schematic and PCB layout through firmware to cloud backend. I specialise in low-power wearables, real-time RTOS systems, and wireless stacks (BLE, LoRa, MQTT, CAN). I own the full toolchain: C/C++ firmware, EasyEDA PCB design, LTspice simulation, Python backends, and AWS IoT. Currently pursuing an M.Sc. in Internet & Multimedia Engineering at the University of Genoa.

---

## Tech Stack

**Microcontrollers**
![ESP32](https://img.shields.io/badge/ESP32-000000?style=flat&logo=espressif&logoColor=white)
![STM32](https://img.shields.io/badge/STM32-03234B?style=flat&logo=stmicroelectronics&logoColor=white)
![nRF52](https://img.shields.io/badge/nRF52840-00A9CE?style=flat&logo=nordicsemiconductor&logoColor=white)
![ARM Cortex-M](https://img.shields.io/badge/ARM_Cortex--M-0091BD?style=flat&logo=arm&logoColor=white)

**RTOS & Firmware**
![FreeRTOS](https://img.shields.io/badge/FreeRTOS-8CC84B?style=flat)
![Zephyr OS](https://img.shields.io/badge/Zephyr_OS-6A5ACD?style=flat)
![ESP-IDF](https://img.shields.io/badge/ESP--IDF-E7352C?style=flat&logo=espressif&logoColor=white)
![PlatformIO](https://img.shields.io/badge/PlatformIO-FF7F00?style=flat&logo=platformio&logoColor=white)

**Languages**
![C](https://img.shields.io/badge/C-Expert-00599C?style=flat&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-Proficient-00599C?style=flat&logo=cplusplus&logoColor=white)
![Python](https://img.shields.io/badge/Python-Proficient-3776AB?style=flat&logo=python&logoColor=white)

**Wireless & Protocols**
![BLE](https://img.shields.io/badge/BLE_5.0-0082FC?style=flat&logo=bluetooth&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-660066?style=flat&logo=mqtt&logoColor=white)
![LoRa](https://img.shields.io/badge/LoRa-00AEEF?style=flat)
![CAN](https://img.shields.io/badge/CAN_Bus-FF6600?style=flat)
![RS485](https://img.shields.io/badge/RS485%2FModbus-555555?style=flat)
![GSM](https://img.shields.io/badge/GSM%2FLTE-4CAF50?style=flat)

**Cloud & IoT Platforms**
![AWS IoT](https://img.shields.io/badge/AWS_IoT_Core-FF9900?style=flat&logo=amazonaws&logoColor=white)
![Azure IoT](https://img.shields.io/badge/Azure_IoT_Hub-0078D4?style=flat&logo=microsoftazure&logoColor=white)
![Home Assistant](https://img.shields.io/badge/Home_Assistant-41BDF5?style=flat&logo=homeassistant&logoColor=white)
![ThingsBoard](https://img.shields.io/badge/ThingsBoard-00695C?style=flat)

**PCB & EDA**
![EasyEDA](https://img.shields.io/badge/EasyEDA-1B6CA8?style=flat)
![LTspice](https://img.shields.io/badge/LTspice-A50021?style=flat)

---

## Selected Projects

### [ESP32 + Quectel M95 — MQTT over GSM](https://github.com/abdullahshabbir2/quectelm95_gsm_mqtt)
I drive a Quectel M95 GSM modem directly via AT commands from an ESP32, bypassing any high-level GSM library to implement the full PDP context activation → TCP connect → MQTT session handshake myself. A custom `GSM_MQTT` wrapper class handles command/response validation and the two-step `QMTPUB` publish flow.
`ESP32` `C++` `AT Commands` `MQTT` `GSM` `PlatformIO`

---

### [Smart Cistern & Irrigation Controller](https://github.com/abdullahshabbir2/home-assistant-cistern-integration)
A custom Python Home Assistant integration that exposes 6-zone relays, timers, a water-level sensor, and settings as native Lovelace entities. I implemented two-tier automation: on-device rules (rain override, low-water cutoff) for offline resilience, and HA automations for complex multi-sensor cross-zone logic. Bidirectional HTTP state sync keeps the dashboard and hardware consistent at all times.
`ESP32` `Python` `Home Assistant` `MQTT` `HTTP`

---

### Smart Diffuser Platform — *Multi-PCB · BLE 5.0 + Wi-Fi*
3V/5V/12V PCB variants from a shared schematic with hardware-selectable power paths. ESP-IDF + FreeRTOS firmware with concurrent motor control (limit-switch feedback), RTC-based offline scheduling, and BLE 5.0 with ACK-based delivery, retries, and chunked transfer for reliable app communication. Zero field failures across the initial production batch.
`ESP32` `ESP-IDF` `FreeRTOS` `BLE 5.0` `EasyEDA` `C`

---

### Infant Monitoring Wearable — *nRF52840 + Zephyr OS*
Medical-grade wearable for continuous infant SpO₂/HR monitoring (PPG) and motion detection (IMU). My sensor-fusion pipeline suppressed movement artefacts and the power architecture achieved <15 µA average in deep-sleep with 5 s wake-acquire-transmit cycles. BLE 5.0 streamed processed physiological data to a gateway hub in real time.
`nRF52840` `Zephyr OS` `BLE 5.0` `PPG` `IMU` `C`

---

### EV Battery Monitoring & Control System — *CAN + RTOS + GSM*
CAN bus (ISO 11898, 500 kbps) backbone for battery cell telemetry; FreeRTOS priority-partitioned tasks kept battery switching logic at sub-5 ms latency with safe fail-state transitions. GSM cloud uplink for remote diagnostics, GPS tracking pipeline, and PZEM-004T smart metering over RS485/Modbus.
`STM32` `FreeRTOS` `CAN Bus` `GSM` `RS485` `Modbus` `C`

---

### Parkinson's Monitoring System — *B.Sc. FYP · Distinction*
A two-tier distributed system: wearable IMU edge nodes extracted tremor frequency, amplitude, and gait features locally (>90% data reduction vs raw streaming) and transmitted over BLE to a Raspberry Pi fog node running a classification pipeline. The architecture operated independently of cloud, reducing round-trip latency ~70% and maintaining monitoring during outages.
`nRF52` `BLE 5.0` `Raspberry Pi` `Python` `IMU` `Edge ML` `C`

---

## PCB Design Highlights

I've designed 8+ custom boards in EasyEDA across commercial and research projects — full workflow from schematic through layout, DRC, Gerber, fabrication, and bring-up.

- Multi-voltage product boards (3V/5V/12V) with shared schematic and hardware-selectable power paths
- NFC integration: RF keepout zones, impedance-matched traces, ground plane management
- Ultra-compact GPS + LoRa/GSM tracker PCB (<30 g): RF antenna trade-offs for range, isolation, and form factor
- Wearable layouts: miniaturised power management and PPG/IMU sensor interfaces on nRF52-based designs
- LTspice used alongside layout for power supply simulation and analog signal-path verification

---

## Education

| Degree | Institution | Year |
|--------|------------|------|
| M.Sc. Internet & Multimedia Engineering | University of Genoa, Italy | 2024 – Present |
| B.Sc. Computer Engineering | COMSATS University Islamabad, Pakistan | 2019 – 2023 |

---

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=abdullahshabbir2&show_icons=true&theme=default&hide_border=true" alt="GitHub Stats" />
</p>
