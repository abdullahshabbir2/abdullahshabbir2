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

🚀 3+ years delivering commercial embedded products across healthcare, smart home, EV, and environmental-monitoring domains.

---

## 🧠 Expertise

- 📦 <strong>Embedded Firmware:</strong> C, C++, ESP-IDF, FreeRTOS, Zephyr OS, bare-metal embedded C
- 🔌 <strong>Microcontrollers:</strong> ESP32, ESP8266, STM32, nRF52840, ARM Cortex-M, Raspberry Pi
- 📶 <strong>Wireless & Protocols:</strong> BLE 5.0, MQTT, GSM/GPRS/LTE, LoRa, CAN, RS485/Modbus, NFC
- 🧩 <strong>PCB Design:</strong> EasyEDA schematic/layout, DRC, Gerbers, fabrication handoff, bring-up, RF-aware layouts
- ☁️ <strong>Cloud & Backend:</strong> Python, FastAPI, Flask, AWS IoT Core, Azure IoT Hub, Home Assistant, ThingsBoard
- 🛠️ <strong>Debug & Simulation:</strong> LTspice, oscilloscope, logic analyzer, JTAG/OpenOCD, PlatformIO
- <strong>Automotive Diagnostics & Binary Analysis:</strong> CAN/ISO-TP and UDS lab implementations, executable inspection, checksum verification, constrained binary patching, and fault-injection testing

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
  <img alt="AUTOSAR" src="https://img.shields.io/badge/AUTOSAR_Classic-C8102E?style=for-the-badge">
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

<p><strong>Automotive diagnostics & binary analysis (host-validated projects)</strong></p>
<p>
  <img alt="ISO-TP" src="https://img.shields.io/badge/ISO--TP-176B87?style=for-the-badge">
  <img alt="UDS" src="https://img.shields.io/badge/UDS-005F73?style=for-the-badge">
  <img alt="Binary Analysis" src="https://img.shields.io/badge/Binary_Analysis-5B4B8A?style=for-the-badge">
  <img alt="GNU Binutils" src="https://img.shields.io/badge/GNU_Binutils-A42E2B?style=for-the-badge&logo=gnu&logoColor=white">
  <img alt="CRC and SHA-256" src="https://img.shields.io/badge/CRC_%26_SHA--256-287271?style=for-the-badge">
  <img alt="Fault Injection Testing" src="https://img.shields.io/badge/Fault_Injection_Testing-9B5D20?style=for-the-badge">
</p>

---

## 📂 Projects

#### 🚘 [AUTOSAR EV Telematics & Odometry ECU](https://github.com/abdullahshabbir2/autosar-ev-telematics)

Production-grade **AUTOSAR Classic** layered firmware for an electric-vehicle telematics and odometry ECU, rebuilt from a shipped v1 that lost odometer data in the field. Five layers — MCAL, ECU abstraction, services, RTE, application — with every hardware-touching module split into a host-testable pure core and a target-only platform leaf. Roughly **90% of the source runs under the host suite**, and the split is enforced mechanically: the test runner links every source file into every test binary, so a platform dependency leaking above the MCAL is a link error rather than a review comment.

Integer-only odometry with a Q32 conversion factor and carried remainder, because `float` cannot represent every millimetre past 16.8 km. Crash-safe flash persistence where a record becomes authoritative on a single byte write. ISO 14229 diagnostic event management with debouncing, freeze frames and healing. Per-task watchdog supervision with execution budgets asserted at compile time.

**333 host unit tests** across 16 suites · **six CI gates** (tests under 11 warning flags, firmware build, cppcheck, clang-format, Doxygen warnings-as-errors, credential hygiene) · 129 documented requirements with generated traceability · six architecture decision records · eight hand-written SVG diagrams.

Writing the tests found four defects in code that had already been reviewed: a silent NvM write loss, a poisoned flash slot no retry could clear, a backlog that never crossed a date boundary, and a cellular fallback that was permanent for the life of the run.

`AUTOSAR Classic` `Embedded C` `ESP32` `FreeRTOS` `CAN` `RS485/Modbus` `ISO 14229 UDS` `Unit Testing` `GitHub Actions` `Doxygen`

#### [ECU Programming Workbench](https://github.com/abdullahshabbir2/ecu-programming-workbench)

Python diagnostic-programming laboratory with a virtual ECU, classical CAN/ISO-TP transport, a UDS service subset, session handling, block transfers, integrity verification, and A/B image activation. Includes lost-acknowledgement recovery, voltage/RPM interlocks, interrupted-update tests, and recorded CAN/UDS traces. **36 automated tests** cover the host simulation; physical ECU flashing is outside its validated scope.

`Python` `CAN` `ISO-TP` `UDS` `A/B Update Model` `CRC32` `SHA-256` `Fault Injection`

#### [Strategy Patch Lab](https://github.com/abdullahshabbir2/strategy-patch-lab)

C++17 strategy model and owned-binary modification workflow for a Windows x86-64 host executable. Extracts calibration tables, applies a hash-checked instruction patch, corrects the PE checksum, compares baseline/patched behavior, and restores the exact original binary. Models map switching, ethanol fuel compensation, launch and shift torque limits with protection checks. Includes disassembly, address maps, **11 patch tests**, and a **421-step replay**. Validation uses an owned x86-64 image and synthetic inputs.

`C++17` `Python` `Binary Analysis` `PE32+` `GNU objdump / nm` `Checksum Verification` `Regression Testing`


#### 💨 Smart Diffuser Platform

Multi-voltage 3V/5V/12V PCB variants from a shared schematic, with ESP-IDF and FreeRTOS firmware for motor control, limit-switch feedback, RTC-based offline scheduling, and BLE 5.0 transfer with acknowledgements, retries, and chunking.

`ESP32` `ESP-IDF` `FreeRTOS` `BLE 5.0` `EasyEDA` `C`

#### 🚗 EV Battery Monitoring & Control System

FreeRTOS-based battery telemetry and switching control over CAN bus, with GSM cloud uplink, GPS tracking, RS485/Modbus metering, and safe fail-state handling for battery-side control logic.

`STM32` `FreeRTOS` `CAN` `GSM` `GPS` `RS485` `Modbus` `C`

#### 👶 Infant Monitoring Wearable

nRF52840 and Zephyr OS wearable for continuous infant SpO2/HR and IMU monitoring. The design combined low-power firmware, BLE streaming, motion-aware signal processing, and a deep-sleep power profile below 15 uA average.

`nRF52840` `Zephyr OS` `BLE 5.0` `PPG` `IMU` `Low Power` `C`

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

B.Sc. final-year project using wearable IMU edge nodes and a Raspberry Pi fog node. The edge nodes extracted tremor and gait features locally, reducing raw data transmission by more than 90% before BLE transfer to the classifier.

`nRF52` `BLE 5.0` `Raspberry Pi` `Python` `IMU` `Edge ML`

#### 🛒 [Grocery Warehouse Inventory System](https://github.com/abdullahshabbir2/Grocery-WareHouse)

Java Swing desktop inventory system with MySQL-backed create, read, update, and delete flows for grocery items, plus a Jupyter Notebook component for data-oriented work in the same repository.

`Java` `Swing` `MySQL` `JDBC` `CRUD` `Jupyter Notebook`

---

## 🖨️ PCB Design Highlights

- 📦 Multi-voltage product boards with shared schematics and hardware-selectable power paths
- 📶 NFC layouts with RF keepout zones, impedance-aware routing, and ground-plane control
- 🛰️ Compact GPS + LoRa/GSM tracker PCB design under 30 g
- ⌚ Wearable PCB layouts with miniaturized power management and PPG/IMU sensor interfaces
- 🔬 Power-supply and analog signal-path verification with LTspice

---

## 🎓 Education

| Degree | Institution | Year |
| --- | --- | --- |
| M.Sc. Internet and Multimedia Engineering | University of Genoa, Italy | 2024 - Present |
| B.Sc. Computer Engineering, FYP Distinction | COMSATS University Islamabad, Pakistan | 2019 - 2023 |
