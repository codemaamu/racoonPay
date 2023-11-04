# RacoonPay Transaction Management System

The RacoonPay Transaction Management System is a Python application that allows you to record and manage financial transactions between senders and recipients. It utilizes a MySQL database to store transaction data and maintains a list of NGOs (Non-Governmental Organizations) with their transaction history.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before using this application, make sure you have the following prerequisites:

- Python 3.x installed on your system.
- The `mysql.connector` library for Python.

## Installation

1. Clone the repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Install the `mysql.connector` library if not already installed:


4. Set up a MySQL server and configure the connection details in the code (host, user, password).

## Usage

1. Create a JSON file with transaction data in the following format:

```json
{
    "sender_name": "John Doe",
    "s_address": "0x1234567890abcdef",
    "receiver_name": "Charity Organization",
    "r_address": "0x9876543210fedcba",
    "amount": 100.0,
    "date": "2023-11-04"
}



