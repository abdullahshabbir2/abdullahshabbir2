<h1 align="center">Hi, I'm Abdullah Shabbir</h1>

<p align="center">
  <strong>IoT and Embedded Systems Engineer</strong><br>
  Building connected hardware from schematic and PCB layout to firmware, cloud, and dashboards.
</p>

<p align="center">
  Genoa, Italy |
  <a href="mailto:abdullahshabbir2@gmail.com">abdullahshabbir2@gmail.com</a> |
  <a href="https://linkedin.com/in/abdullah-shabbir960373196">LinkedIn</a>
</p>

---

## About

I build end-to-end embedded products across firmware, PCB design, wireless communication, and IoT backends. My work focuses on low-power wearables, real-time control systems, BLE/GSM/LoRa connectivity, and cloud-connected automation.

- 2+ years delivering commercial embedded products in healthcare, smart home, EV, and environmental monitoring.
- 10+ product builds across ESP32, STM32, nRF52, Raspberry Pi, FreeRTOS, Zephyr OS, and bare-metal C/C++.
- 8+ custom PCB designs in EasyEDA, covering schematic capture, layout, DRC, Gerbers, fabrication, bring-up, and debugging.
- Currently pursuing an M.Sc. in Internet and Multimedia Engineering at the University of Genoa, Italy.

---

## Core Stack

| Area | Tools and technologies |
| --- | --- |
| Firmware | C, C++, ESP-IDF, FreeRTOS, Zephyr OS, bare-metal embedded C |
| Hardware | ESP32, ESP8266, STM32, nRF52840, ARM Cortex-M, Raspberry Pi |
| Connectivity | BLE 5.0, MQTT, GSM/GPRS/LTE, LoRa, CAN, RS485/Modbus, NFC |
| PCB and debug | EasyEDA, LTspice, oscilloscope, logic analyzer, JTAG/OpenOCD |
| Cloud and backend | Python, FastAPI, Flask, AWS IoT Core, Azure IoT Hub, Home Assistant, ThingsBoard |

<p align="center">
  <img alt="ESP32" src="https://img.shields.io/badge/ESP32-000000?style=for-the-badge&logo=espressif&logoColor=white">
  <img alt="STM32" src="https://img.shields.io/badge/STM32-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white">
  <img alt="nRF52" src="https://img.shields.io/badge/nRF52-00A9CE?style=for-the-badge&logo=nordicsemiconductor&logoColor=white">
  <img alt="FreeRTOS" src="https://img.shields.io/badge/FreeRTOS-8CC84B?style=for-the-badge">
  <img alt="Zephyr OS" src="https://img.shields.io/badge/Zephyr_OS-6A5ACD?style=for-the-badge">
  <img alt="C" src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white">
  <img alt="C++" src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
</p>

---

## Selected Work

### [ESP32 + Quectel M95: MQTT over GSM](https://github.com/abdullahshabbir2/quectelm95_gsm_mqtt)

Direct ESP32 control of a Quectel M95 GSM modem using AT commands, with no high-level modem library. The firmware handles PDP context activation, TCP connection setup, MQTT CONNECT/PUBLISH flow, prompt parsing, response validation, and modem state tracking.

`ESP32` `C++` `AT Commands` `MQTT` `GSM/GPRS` `PlatformIO`

### [Smart Cistern and Irrigation Controller](https://github.com/abdullahshabbir2/home-assistant-cistern-integration)

Custom Home Assistant integration for 6-zone relay control, timers, water-level sensing, and native Lovelace entities. The system combines offline device-side protection rules with Home Assistant automations and bidirectional HTTP state sync.

`ESP32` `Python` `Home Assistant` `MQTT` `HTTP`

### Smart Diffuser Platform

Multi-voltage 3V/5V/12V PCB variants from a shared schematic, with ESP-IDF and FreeRTOS firmware for motor control, limit-switch feedback, RTC-based offline scheduling, and BLE 5.0 transfer with acknowledgements, retries, and chunking.

`ESP32` `ESP-IDF` `FreeRTOS` `BLE 5.0` `EasyEDA` `C`

### Infant Monitoring Wearable

nRF52840 and Zephyr OS wearable for continuous infant SpO2/HR and IMU monitoring. The design combined low-power firmware, BLE streaming, motion-aware signal processing, and a deep-sleep power profile below 15 uA average.

`nRF52840` `Zephyr OS` `BLE 5.0` `PPG` `IMU` `C`

### EV Battery Monitoring and Control System

FreeRTOS-based battery telemetry and switching control over CAN bus, with GSM cloud uplink, GPS tracking, RS485/Modbus metering, and safe fail-state handling for battery-side control logic.

`STM32` `FreeRTOS` `CAN` `GSM` `RS485` `Modbus` `C`

### Parkinson's Monitoring System

B.Sc. final-year project using wearable IMU edge nodes and a Raspberry Pi fog node. The edge nodes extracted tremor and gait features locally, reducing raw data transmission by more than 90% before BLE transfer to the classifier.

`nRF52` `BLE 5.0` `Raspberry Pi` `Python` `IMU` `Edge ML`

---

## PCB Design Highlights

- Multi-voltage product boards with shared schematics and hardware-selectable power paths.
- NFC layouts with RF keepout zones, impedance-aware routing, and ground-plane control.
- Compact GPS + LoRa/GSM tracker PCB design under 30 g.
- Wearable PCB layouts with miniaturized power management and PPG/IMU sensor interfaces.
- Power-supply and analog signal-path verification with LTspice.

---

## Education

| Degree | Institution | Year |
| --- | --- | --- |
| M.Sc. Internet and Multimedia Engineering | University of Genoa, Italy | 2024 - Present |
| B.Sc. Computer Engineering, FYP Distinction | COMSATS University Islamabad, Pakistan | 2019 - 2023 |

---

<p align="center">
  <img alt="Abdullah's GitHub stats" src="https://github-readme-stats.vercel.app/api?username=abdullahshabbir2&show_icons=true&theme=default&hide_border=true">
</p>
