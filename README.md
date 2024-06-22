# UDP Throughput Measurement with iPerf-like Python Implementation

This repository contains a Python implementation for measuring UDP throughput, similar to iPerf. The project includes a client and a server script that send and receive data over a UDP connection to measure network performance.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Introduction
This project provides a simple way to measure UDP throughput between a client and a server using Python. It mimics the functionality of iPerf by sending a fixed amount of data from the client to the server and measuring the time taken to receive the data, then calculating the throughput.

## Project Structure
The project includes the following files:
- **ProgramiPerfServer.py**: The server script that receives data and calculates throughput.
- **ProgramiPerfClient.py**: The client script that sends data to the server.
- **browserproxy-mob/**: (not provided) Directory expected to contain BrowserMob Proxy executable and related files.

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/udp-throughput-measurement.git
   cd udp-throughput-measurement
   ```

2. Ensure Python 3 is installed on your system.

## Usage
1. **Start the Server**:
   - Open a terminal and navigate to the project directory.
   - Run the server script:
     ```sh
     python ProgramiPerfServer.py
     ```

2. **Run the Client**:
   - Open another terminal and navigate to the project directory.
   - Run the client script:
     ```sh
     python ProgramiPerfClient.py
     ```

3. The client will send data to the server, which will measure and print the throughput.

## Configuration
- **Server Configuration**: Modify the `HOST` and `PORT` variables in `ProgramiPerfServer.py` to change the server address and port.
- **Client Configuration**: Modify the `SERVER_HOST` and `SERVER_PORT` variables in `ProgramiPerfClient.py` to match the server's address and port.
- **Data Size**: Adjust the `data_size` variable in `ProgramiPerfClient.py` to change the amount of data sent.