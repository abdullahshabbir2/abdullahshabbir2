<div align="center">

<h1>Hi, I'm Abdullah Shabbir 👋</h1>

<a href="https://github.com/abdullahshabbir2">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3500&pause=900&color=58A6FF&center=true&vCenter=true&width=640&lines=Embedded+Systems+%7C+IoT+%7C+Firmware+Engineer;Schematic+%E2%86%92+PCB+%E2%86%92+Firmware+%E2%86%92+Cloud;ESP32+%E2%80%A2+STM32+%E2%80%A2+nRF5340+%E2%80%A2+nRF52840+%E2%80%A2+Yocto;Secure+boot+%E2%80%A2+Mutual+TLS+%E2%80%A2+Signed+OTA;AUTOSAR+%7C+CAN+%7C+UDS+%7C+BLE+%7C+LoRa+%7C+MQTT" alt="Typing SVG">
</a>

<p>
  <strong>3+ years taking connected-device products from schematic and PCB layout through firmware, security, cloud integration, and field deployment.</strong>
</p>

<p>
  <img alt="Location" src="https://img.shields.io/badge/Genoa,_Italy-1F2937?style=flat-square&logo=googlemaps&logoColor=white">
  <img alt="Relocation" src="https://img.shields.io/badge/Open_to_relocation-EU-2563EB?style=flat-square">
  <img alt="Products" src="https://img.shields.io/badge/10%2B-products_shipped-16A34A?style=flat-square">
  <img alt="PCBs" src="https://img.shields.io/badge/8%2B-custom_PCBs-EA580C?style=flat-square">
  <img alt="Study" src="https://img.shields.io/badge/M.Sc.-University_of_Genoa-0F766E?style=flat-square">
  <img alt="Profile views" src="https://komarev.com/ghpvc/?username=abdullahshabbir2&style=flat-square&color=blueviolet&label=Profile+views">
</p>

<p>
  <a href="mailto:abdullahshabbir2@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <a href="https://linkedin.com/in/abdullahshabbir2"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a>
  <a href="https://github.com/abdullahshabbir2"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"></a>
</p>

</div>

---

## 💼 About Me

- 🔧 **Embedded Systems & IoT Engineer** who owns the whole product: requirements, architecture, hardware, firmware, cloud, and field deployment
- 🧩 Hands-on across many boards: **Nordic nRF5340 & nRF52840 (and their DKs)**, ESP32, STM32, TI CC13xx, Raspberry Pi, and my own custom PCBs
- ⏱️ Real-time firmware on **FreeRTOS and Zephyr** with **sub-10 ms task jitter** and **sub-5 ms** battery-switching latency
- 🐧 Builds **Embedded Linux** gateways with **Yocto**: read-only rootfs, A/B updates, systemd-supervised daemons
- 🚘 Working in **automotive software**: AUTOSAR Classic, CAN/ISO 11898, ISO-TP, UDS, MISRA C/C++, ISO 26262
- 🎓 Completing an **M.Sc. in Internet & Multimedia Engineering** at the University of Genoa, Italy
- 💬 Open to **embedded / IoT / automotive firmware** roles across the EU

---

## ⚡ At a Glance

<table>
<tr>
<td width="50%" valign="top">

**🔌 Boards, MCUs & dev kits I've built on**

| Family | Chips & boards |
| --- | --- |
| Nordic | **nRF5340** (dual-core, Zephyr), **nRF52840**, nRF5340 DK, nRF52840 DK |
| Espressif | ESP32, ESP8266 |
| ST | STM32 F1, STM32 F4 |
| TI Sub-GHz | CC1312, CC1352P7 |
| Linux / SBC | Raspberry Pi, qemuarm64 (Yocto) |
| FPGA | Altera DE2 (Intel Quartus) |
| Core | ARM Cortex-M (bare metal & HAL) |

</td>
<td width="50%" valign="top">

**🧵 Systems & radios**

| Area | What I use |
| --- | --- |
| RTOS / OS | FreeRTOS, Zephyr, Embedded Linux, Yocto |
| Short range | BLE 5.0, Wi-Fi, NFC (PN7160), UWB (DW3110) |
| Wired / field | CAN/CANopen, RS485/Modbus, Ethernet, OPC-UA |
| On-board | UART, I2C, SPI, JTAG/SWD |
| Cloud | AWS IoT Core, Azure IoT Hub, ThingsBoard, OpenRemote |
| Quality | Host unit tests, GitHub Actions CI, MISRA, cppcheck |

</td>
</tr>
</table>

---

## 🔐 Device & MQTT Security

Security is designed in from the first board revision, not bolted on at release.

| Layer | What I implement |
| --- | --- |
| 🔑 **Transport** | MQTT over **mutual TLS** with per-device **X.509 client certificates** and **server certificate pinning** on AWS IoT Core and Azure IoT Hub |
| 🧾 **Authorisation** | **Per-device topic permissions**: each device may publish and subscribe only on its own topics, enforced by broker policies tied to its certificate identity |
| 📨 **Messaging** | Structured **MQTT topic architectures** and **device-shadow synchronisation** across AWS IoT, Azure IoT Hub, ThingsBoard, and OpenRemote |
| 📦 **Updates** | **Signed OTA pipelines**; A/B image-swap updates on Embedded Linux gateways |
| 📐 **Practice** | **IEC 62443** principles, CE/RED design guidance, credential-hygiene checks in CI |

---

## 🧠 Expertise

| Area | Skills |
| --- | --- |
| 📦 **Embedded Firmware** | C, C++, ESP-IDF, FreeRTOS, Zephyr OS, bare-metal C, HAL, device drivers, bootloaders |
| 🐧 **Embedded Linux** | Yocto Project, custom layers, read-only rootfs, A/B image updates, systemd services and watchdog, QEMU |
| 📶 **Wireless & Protocols** | BLE 5.0, Wi-Fi, MQTT, HTTP/REST, GSM/LTE, LTE-M, LoRa, UWB, 868 MHz, NFC, CAN/CANopen, RS485/Modbus, OPC-UA |
| ☁️ **Cloud & Apps** | Python, FastAPI, Flask, AWS IoT Core, AWS Lambda, Azure IoT Hub, ThingsBoard, OpenRemote, Home Assistant, Flutter BLE apps, Docker |
| 🔬 **FPGA & HDL** | VHDL, Intel Quartus, RTL simulation, finite state machine design, RISC datapath |
| 🛠️ **Debug & Tools** | Oscilloscope, logic analyser, JTAG/SWD, OpenOCD, LTspice, Keil MDK, STM32CubeIDE, Zephyr west, CMake, PlatformIO |
| 🚘 **Automotive & Standards** | AUTOSAR Classic, ISO 11898, ISO-TP, UDS, MISRA C, MISRA C++ / AUTOSAR C++14, ISO 26262, binary analysis, fault injection |

---

## 🚀 Tech Stack

<div align="center">

**Hardware & Firmware**

<img alt="ESP32" src="https://img.shields.io/badge/ESP32-000000?style=for-the-badge&logo=espressif&logoColor=white">
<img alt="STM32" src="https://img.shields.io/badge/STM32-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white">
<img alt="nRF52840" src="https://img.shields.io/badge/nRF52840-00A9CE?style=for-the-badge&logo=nordicsemiconductor&logoColor=white">
<img alt="nRF5340" src="https://img.shields.io/badge/nRF5340-00A9CE?style=for-the-badge&logo=nordicsemiconductor&logoColor=white">
<img alt="Nordic DKs" src="https://img.shields.io/badge/nRF52840_%26_nRF5340_DK-0B3D5C?style=for-the-badge&logo=nordicsemiconductor&logoColor=white">
<img alt="Raspberry Pi" src="https://img.shields.io/badge/Raspberry_Pi-A22846?style=for-the-badge&logo=raspberrypi&logoColor=white">
<img alt="TI CC13xx" src="https://img.shields.io/badge/TI_CC1312%2FCC1352-CC0000?style=for-the-badge&logo=texasinstruments&logoColor=white">
<img alt="FreeRTOS" src="https://img.shields.io/badge/FreeRTOS-8CC84B?style=for-the-badge">
<img alt="Zephyr OS" src="https://img.shields.io/badge/Zephyr_OS-6A5ACD?style=for-the-badge">
<img alt="AUTOSAR" src="https://img.shields.io/badge/AUTOSAR_Classic-C8102E?style=for-the-badge">
<img alt="PlatformIO" src="https://img.shields.io/badge/PlatformIO-FF7F00?style=for-the-badge&logo=platformio&logoColor=white">
<img alt="KiCad" src="https://img.shields.io/badge/KiCad-314CB0?style=for-the-badge&logo=kicad&logoColor=white">
<img alt="EasyEDA" src="https://img.shields.io/badge/EasyEDA-1B6CA8?style=for-the-badge">
<img alt="STM32CubeIDE" src="https://img.shields.io/badge/STM32CubeIDE-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white">
<img alt="Keil MDK" src="https://img.shields.io/badge/Keil_MDK-394E79?style=for-the-badge&logo=arm&logoColor=white">
<img alt="LTspice" src="https://img.shields.io/badge/LTspice-A10035?style=for-the-badge&logo=analogdevices&logoColor=white">

**Embedded Linux & FPGA**

<img alt="Embedded Linux" src="https://img.shields.io/badge/Embedded_Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black">
<img alt="Yocto" src="https://img.shields.io/badge/Yocto_Project-1B75BB?style=for-the-badge&logo=yoctoproject&logoColor=white">
<img alt="systemd" src="https://img.shields.io/badge/systemd-201A26?style=for-the-badge">
<img alt="QEMU" src="https://img.shields.io/badge/QEMU-FF6600?style=for-the-badge&logo=qemu&logoColor=white">
<img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
<img alt="VHDL" src="https://img.shields.io/badge/VHDL-4B0082?style=for-the-badge">
<img alt="Intel Quartus" src="https://img.shields.io/badge/Intel_Quartus-0071C5?style=for-the-badge&logo=intel&logoColor=white">

**Languages**

<img alt="C" src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white">
<img alt="C++" src="https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white">
<img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img alt="Java" src="https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white">
<img alt="Dart" src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white">
<img alt="MATLAB" src="https://img.shields.io/badge/MATLAB-E16737?style=for-the-badge">

**Connectivity & Cloud**

<img alt="BLE" src="https://img.shields.io/badge/BLE_5.0-0082FC?style=for-the-badge&logo=bluetooth&logoColor=white">
<img alt="MQTT" src="https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=mqtt&logoColor=white">
<img alt="LoRa" src="https://img.shields.io/badge/LoRa-00AEEF?style=for-the-badge">
<img alt="CAN" src="https://img.shields.io/badge/CAN_Bus-FF6600?style=for-the-badge">
<img alt="AWS IoT" src="https://img.shields.io/badge/AWS_IoT_Core-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white">
<img alt="Home Assistant" src="https://img.shields.io/badge/Home_Assistant-41BDF5?style=for-the-badge&logo=homeassistant&logoColor=white">
<img alt="Azure IoT Hub" src="https://img.shields.io/badge/Azure_IoT_Hub-0078D4?style=for-the-badge">
<img alt="ThingsBoard" src="https://img.shields.io/badge/ThingsBoard-305680?style=for-the-badge">
<img alt="OpenRemote" src="https://img.shields.io/badge/OpenRemote-4E9D2D?style=for-the-badge">
<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
<img alt="UWB" src="https://img.shields.io/badge/UWB-7A3E9D?style=for-the-badge">
<img alt="Sub-GHz" src="https://img.shields.io/badge/Sub--GHz_868_MHz-B5179E?style=for-the-badge">
<img alt="LTE-M" src="https://img.shields.io/badge/LTE--M-E4002B?style=for-the-badge">
<img alt="OPC-UA" src="https://img.shields.io/badge/OPC--UA-2E7D32?style=for-the-badge">

**Security**

<img alt="Mutual TLS" src="https://img.shields.io/badge/Mutual_TLS_(X.509)-2B2D42?style=for-the-badge&logo=letsencrypt&logoColor=white">
<img alt="Secure Boot" src="https://img.shields.io/badge/Secure_Boot-8D0801?style=for-the-badge">
<img alt="Signed OTA" src="https://img.shields.io/badge/Signed_OTA-1D3557?style=for-the-badge">
<img alt="Certificate Pinning" src="https://img.shields.io/badge/Certificate_Pinning-3D5A80?style=for-the-badge">
<img alt="MQTT Topic ACLs" src="https://img.shields.io/badge/MQTT_Topic_ACLs-660066?style=for-the-badge&logo=mqtt&logoColor=white">

**Automotive, Standards & Binary Analysis**

<img alt="ISO-TP" src="https://img.shields.io/badge/ISO--TP-176B87?style=for-the-badge">
<img alt="UDS" src="https://img.shields.io/badge/UDS-005F73?style=for-the-badge">
<img alt="Binary Analysis" src="https://img.shields.io/badge/Binary_Analysis-5B4B8A?style=for-the-badge">
<img alt="GNU Binutils" src="https://img.shields.io/badge/GNU_Binutils-A42E2B?style=for-the-badge&logo=gnu&logoColor=white">
<img alt="CRC and SHA-256" src="https://img.shields.io/badge/CRC_%26_SHA--256-287271?style=for-the-badge">
<img alt="Fault Injection Testing" src="https://img.shields.io/badge/Fault_Injection_Testing-9B5D20?style=for-the-badge">
<img alt="MISRA C" src="https://img.shields.io/badge/MISRA_C%2FC%2B%2B-3A506B?style=for-the-badge">
<img alt="ISO 26262" src="https://img.shields.io/badge/ISO_26262-1F4E79?style=for-the-badge">

</div>

---

## 💼 Experience

| Role | Company | Period |
| --- | --- | --- |
| 🧑‍💻 **Freelance IoT & Embedded Systems Engineer** | Self-employed · Remote | Jul 2024 – Present |
| ⚡ **Embedded Systems Engineer** (contract) | LUMS Energy Institute, Pakistan | Oct 2024 – Nov 2024 |
| 📡 **IoT Engineer** | Digitalux, Pakistan | Jul 2023 – Nov 2024 |
| 🔧 **Embedded Systems Intern** | KICS, UET, Pakistan | Jul 2022 – Sep 2022 |
| 🏭 **Engineering Intern** | Pak Elektron Limited (PEL), Pakistan | Aug 2021 – Sep 2021 |

<details>
<summary><strong>Highlights</strong></summary>

- **LUMS Energy Institute:** ESP-IDF firmware for an EV battery monitoring and control unit (CAN telemetry, GPS, fail-safe switching) and a PZEM-004T RS485/Modbus smart energy meter, both with GSM/MQTT uplink to AWS
- **Digitalux:** ESP32/ESP8266 firmware for commercial products shipped to customers, MQTT topic design, device shadows, and OTA on AWS IoT, Azure IoT Hub, ThingsBoard, and OpenRemote; introduced a DFM checklist that cut board re-spins
- **KICS, UET:** UART, I2C, and SPI drivers and HAL work on ARM Cortex-M, sensor-node pipelines to AWS IoT Core

</details>

---

## 📂 Projects

### ⭐ Featured

#### 🚘 [AUTOSAR EV Telematics & Odometry ECU](https://github.com/abdullahshabbir2/autosar-ev-telematics)

Production-grade **AUTOSAR Classic** layered firmware for an electric-vehicle telematics and odometry ECU, rebuilt from a shipped v1 that lost odometer data in the field. Five layers — MCAL, ECU abstraction, services, RTE, application — with every hardware-touching module split into a host-testable pure core and a target-only platform leaf. Roughly **90% of the source runs under the host suite**, and the split is enforced mechanically: the test runner links every source file into every test binary, so a platform dependency leaking above the MCAL is a link error rather than a review comment.

Integer-only odometry with a Q32 conversion factor and carried remainder, because `float` cannot represent every millimetre past 16.8 km. Crash-safe flash persistence where a record becomes authoritative on a single byte write. ISO 14229 diagnostic event management with debouncing, freeze frames and healing. Per-task watchdog supervision with execution budgets asserted at compile time.

**335 host unit tests** across 16 suites · **six CI gates** (tests under 11 warning flags, firmware build, cppcheck, clang-format, Doxygen warnings-as-errors, credential hygiene) · 129 documented requirements with generated traceability · six architecture decision records · eight hand-written SVG diagrams.

Writing the tests found four defects in code that had already been reviewed: a silent NvM write loss, a poisoned flash slot no retry could clear, a backlog that never crossed a date boundary, and a cellular fallback that was permanent for the life of the run.

`AUTOSAR Classic` `Embedded C` `ESP32` `FreeRTOS` `CAN` `RS485/Modbus` `ISO 14229 UDS` `Unit Testing` `GitHub Actions` `Doxygen`

<p align="right"><a href="https://github.com/abdullahshabbir2/autosar-ev-telematics"><img alt="View repository" src="https://img.shields.io/badge/View_Repository-181717?style=flat-square&logo=github&logoColor=white"></a></p>

### 🚙 Automotive Diagnostics & Binary Analysis

#### 🧪 [ECU Programming Workbench](https://github.com/abdullahshabbir2/ecu-programming-workbench)

Python diagnostic-programming laboratory with a virtual ECU, classical CAN/ISO-TP transport, a UDS service subset, session handling, block transfers, integrity verification, and A/B image activation. Includes lost-acknowledgement recovery, voltage/RPM interlocks, interrupted-update tests, and recorded CAN/UDS traces. **36 automated tests** cover the host simulation; physical ECU flashing is outside its validated scope.

`Python` `CAN` `ISO-TP` `UDS` `A/B Update Model` `CRC32` `SHA-256` `Fault Injection`

#### 🧬 [Strategy Patch Lab](https://github.com/abdullahshabbir2/strategy-patch-lab)

C++17 strategy model and owned-binary modification workflow for a Windows x86-64 host executable. Extracts calibration tables, applies a hash-checked instruction patch, corrects the PE checksum, compares baseline/patched behavior, and restores the exact original binary. Models map switching, ethanol fuel compensation, launch and shift torque limits with protection checks. Includes disassembly, address maps, **11 patch tests**, and a **421-step replay**. Validation uses an owned x86-64 image and synthetic inputs.

`C++17` `Python` `Binary Analysis` `PE32+` `GNU objdump / nm` `Checksum Verification` `Regression Testing`

### 📡 IoT & Embedded Products

#### 🚗 EV Battery Monitoring & Control System

CAN telemetry to **ISO 11898 at 500 kbps** for cell and vehicle data, with FreeRTOS priority-partitioned tasks holding battery switching logic at **sub-5 ms latency**. Control firmware written to **MISRA C++ / AUTOSAR C++14** guidelines: no runtime allocation, bounded loops, deterministic state transitions. GPS tracking, RS485/Modbus metering, and GSM/MQTT cloud uplink, validated on vehicle hardware.

`STM32` `ESP32` `C++` `FreeRTOS` `CAN / ISO 11898` `RS485/Modbus` `GSM` `MQTT` `MISRA C++`

#### 📻 Sub-GHz Sensor Network & Gateway

Shared **868 MHz** network where coin-cell sensor nodes report to a common hub that relays to the cloud, reusing one radio infrastructure across product lines. Selected CC1312 and dual-band CC1352P7 against size, power, and cost.

`TI CC1312` `CC1352P7` `868 MHz` `Coin Cell` `Gateway`

#### 🌬️ [Smart Air Purifier & Air Quality Monitor](https://github.com/abdullahshabbir2/AirPurifier)

ESP32 purifier firmware that computes a US EPA Air Quality Index on-device from particulate, CO, NO2, temperature, and humidity sensors, then drives the fan to match through hysteresis-damped PWM speed control. Publishes telemetry over both a versioned REST API and a NimBLE GATT service with notifications, provisions WiFi from a phone over BLE, and ships a dependency-free AQI engine covered by 120 host unit tests in CI.

`ESP32` `ESP-IDF` `FreeRTOS` `BLE 5.0` `NimBLE` `REST API` `LEDC PWM` `Unit Testing` `GitHub Actions` `C`

#### 🌱 [Smart IoT Greenhouse System](https://github.com/abdullahshabbir2/Smart_IoT_GreenHouse)

Dual-node ESP32 greenhouse automation system with independent local dashboards, REST APIs, mDNS discovery, NVS persistence, watchdog recovery, CORS support, fan hysteresis, pump scheduling, low-water lockout, and rain-based irrigation protection.

`ESP32` `C++` `PlatformIO` `REST API` `mDNS` `NVS` `Watchdog` `IoT Dashboard`

#### 💧 Hydroponic Monitoring System

STM32 hydroponic monitoring with high-precision water chemistry and environmental sensing, including analog front-end conditioning and calibration where sensor drift directly affects crop outcomes.

`STM32` `Analog Front End` `Sensor Calibration`

#### 🚰 [Smart Cistern & Irrigation Controller](https://github.com/abdullahshabbir2/home-assistant-cistern-integration)

Custom Home Assistant integration plus ESP32 firmware for cistern monitoring, relay control, irrigation scheduling, telemetry polling, Zeroconf discovery, coordinator-based updates, and Lovelace dashboard entities.

`ESP32` `Python` `Home Assistant` `Arduino` `REST/JSON` `Lovelace` `Automation`

#### 🔌 [ESP32 + Quectel M95 - MQTT over GSM](https://github.com/abdullahshabbir2/quectelm95_gsm_mqtt)

Bare-metal ESP32 firmware that drives a Quectel M95 GSM modem directly through AT commands. It handles PDP context activation, TCP transport setup, MQTT CONNECT/PUBLISH flow, response validation, and the two-step `QMTPUB` payload prompt sequence.

`ESP32` `C++` `AT Commands` `MQTT` `GSM/GPRS` `UART` `PlatformIO`

### 🐧 Embedded Linux

#### 🧱 meta-iot-gateway — Yocto Linux Layer

Custom Yocto image booted on **qemuarm64** with a read-only rootfs, writable state overlay, **A/B image-swap updates**, and no package manager on target. A C daemon validates **CRC-16/CCITT** UART frames and republishes them to MQTT, with systemd watchdog integration and exponential reconnect backoff.

`Yocto` `Embedded Linux` `systemd` `QEMU` `C` `MQTT` `A/B Updates`

### 🎓 Academic & Other

#### 🧠 Parkinson's Monitoring System


`nRF52` `BLE 5.0` `Raspberry Pi` `Python` `IMU` `Edge ML`

#### 🔲 Digital Design on FPGA

Basic **RISC processor in VHDL** (fetch, decode, execute datapath with register file and control unit) verified in simulation and on the DE2 board, plus FSM controllers for a vending machine and home automation system.

`VHDL` `Intel Quartus` `Altera DE2` `RTL Simulation` `FSM`

#### 🛒 [Grocery Warehouse Inventory System](https://github.com/abdullahshabbir2/Grocery-WareHouse)

Java Swing desktop inventory system with MySQL-backed create, read, update, and delete flows for grocery items, plus a Jupyter Notebook component for data-oriented work in the same repository.

`Java` `Swing` `MySQL` `JDBC` `CRUD` `Jupyter Notebook`

---

## 🖨️ PCB Design Highlights

- 📦 **8+ custom PCBs** in KiCad and EasyEDA, with multi-voltage 3V/5V/12V power architectures and hardware-selectable power paths
- 📶 NFC and multi-radio layouts with RF keep-out zones, impedance-aware routing, and ground stitching
- 🛰️ Sub-30 g GPS + LoRa + UWB + GSM tracker PCB
- ⚡ 12V DC-to-AC inverter with MOSFET H-bridge, dead-time generation, TVS protection, and fusing
- 🔬 Power-supply and analog signal-path verification in LTspice; DFM checklist that reduced re-spins

---

## 🎓 Education & Certifications

| | | |
| --- | --- | --- |
| 🎓 **M.Sc. Internet & Multimedia Engineering** | University of Genoa, Italy | 2024 – 2026 (expected) |
| 🎓 **B.Sc. Computer Engineering**, graduated with Distinction | COMSATS University Islamabad, Pakistan | 2019 – 2023 |
| 📜 **ISO 26262: Essentials of Automotive Functional Safety** | Alison (CPD certified) | Sep 2026 |
| 📜 **Registered Computer Engineer** | Pakistan Engineering Council | Jan 2024 |

🗣️ **Languages:** English (C1, professional) · Urdu (native) · Italian (A1, working toward B2)

---

## 🔥 GitHub Stats

<div align="center">

<img height="170" alt="GitHub stats" src="./profile-summary-card-output/github_dark/3-stats.svg">
<img height="170" alt="Most used languages" src="./assets/top-langs.svg">

<img alt="Contribution profile" src="./profile-summary-card-output/github_dark/0-profile-details.svg">

<img alt="GitHub streak" src="https://streak-stats.demolab.com?user=abdullahshabbir2&theme=github-dark-blue&hide_border=true&border_radius=10">

</div>

---

## 📫 Contact

<div align="center">

<a href="mailto:abdullahshabbir2@gmail.com"><img alt="Email" src="https://img.shields.io/badge/abdullahshabbir2@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white"></a>
<a href="https://linkedin.com/in/abdullahshabbir2"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a>
<a href="https://github.com/abdullahshabbir2"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"></a>

<sub>Always happy to talk embedded systems, IoT security, and automotive firmware.</sub>

</div>
