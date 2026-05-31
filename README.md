<p align="center">
  <img src="media/pylerts_logo.gif" alt="pylerts logo" width="600" />
</p>

<h1 align="center">
  <span style="color:#FFD43B; font-weight:bold;">py</span><span style="color:#FF6600; font-weight:bold;">lerts</span>
</h1>

<p align="center">
  <strong>A lightweight python discord-bot for automatic assignment and updating of roles based on donations from DonationAlerts in real time. Say no to patreon/boosty!</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11%2B-blue?style=flat-square&logo=python&logoColor=yellow" alt="Python Version">
  <img src="https://img.shields.io/badge/discord.py-2.0%2B-blueviolet?style=flat-square" alt="Discord.py Version">
  <img src="https://img.shields.io/badge/Socket.IO-v4-orange?style=flat-square" alt="Socket.io">
</p>

---

## 🪧 About

<span style="color:#FFD43B; font-weight:bold;">py</span><span style="color:#FF6600; font-weight:bold;">lerts</span> listens to the donation stream from your DonationAlerts account via WebSocket connection. As soon as a donation is received, the bot searches for the sender on your Discord server and applies the role assignment rules defined in the configuration file.

## ✨ Features
* **Real-time!** Connection via the official WebSocket widget from DonationAlerts ensures instant reaction.
* **Flexible rule system!** Ability to bind role assignment to donation amount and currency.
* **Multiple role support!** One rule can give a user multiple Discord roles at once.
* **Tier system!** Automatic removal of old roles when a user reaches a higher level (e.g., replacing *tier 1* with *tier 2* on a large donation).

## 🗺️ Roadmap

Here are the planned features for the upcoming releases of <span style="color:#FFD43B; font-weight:bold;">py</span><span style="color:#FF6600; font-weight:bold;">lerts</span>:

- **Cumulative Donation System (CDS)**
  * Add a lightweight SQLite database to track and sum up donations over time, allowing users to unlock roles progressively
- **Discord embeds and public logs**
  * Send beautiful public thank-you cards to a dedicated channel and set up admin logs to track role grant events
- **Dockerization**
  * Provide a `Dockerfile` and `docker-compose.yml` to enable one-command deployment on any Linux VPS/server

---

<p align="center">
  <img src="media/pylerts_install.gif" alt="pylerts install" width="600" />
</p>

## ⚙️ Install and run (Windows)

### Requirements
* Python **3.11** or higher (uses the built-in `tomllib` library for reading configuration).
* Discord bot token with **Server Members Intent** enabled in the Discord developer panel.
* DonationAlerts widget token (You can find it [here](https://www.donationalerts.com/dashboard/general-settings/account).).

### Installation

* Optional: make a directory for pylerts.
```bash
mkdir pylerts
cd pylerts
```
* Clone the repository.
```bash
git clone https://github.com/zito1337/pylerts.git
```
* After cloning, navigate to the `pylerts` directory.
```bash
cd pylerts
```
* Install the required dependencies manually or use the provided `requirements.txt` file.
```bash
pip install -r requirements.txt
```
* Run the bot and wait until it initializes!
```bash
python -m src.pylerts_main
```

---

## ⚙️ Install and run (Linux / Arch)

### Requirements
* same shit as windows...

### Installation

* Optional: make a directory for pylerts.
```bash
mkdir pylerts
cd pylerts
```
* Clone the repository.
```bash
git clone https://github.com/zito1337/pylerts.git
```
* After cloning, navigate to the `pylerts` directory.
```bash
cd pylerts
```
* Since Arch Linux blocks global `pip` installations, set up and activate a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```
* Install the required dependencies inside the virtual environment using the provided `requirements.txt` file.
```bash
pip install -r requirements.txt
```
* Run the bot and wait until it initializes!
```bash
python -m src.pylerts_main
```

---

## ⚙️ Install and run (Linux / Alpine)

### Requirements
* **System packages:** Git, Python, and Pip (`git`, `python3`, `py3-pip`). Install them on Alpine via:
  ```bash
  apk add git python3 py3-pip
  ```
* aaand... pretty same shit as windows

### Installation

* Optional: make a directory for pylerts.
```bash
mkdir pylerts
cd pylerts
```
* Clone the repository.
```bash
git clone https://github.com/zito1337/pylerts.git
```
* After cloning, navigate to the `pylerts` directory.
```bash
cd pylerts
```
* Since Alpine Linux (from v3.19+) blocks global `pip` installations, set up and activate a Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
* Install the required dependencies inside the virtual environment using the provided `requirements.txt` file.
```bash
pip install -r requirements.txt
```
* Run the bot and wait until it initializes!
```bash
python3 -m src.pylerts_main
```

---

## ⚙️ Install and run (FreeBSD)

### Requirements
* System packages: Git, Python 3.11, and Pip (`git`, `python3`, `py311-pip`). Install them on FreeBSD via:
  ```bash
  sudo pkg install git python3 py311-pip
  ```
  or
  ```bash
  su -
  pkg install git python3 py311-pip
  ```
* same shit as windows again...

### Installation

* Optional: make a directory for pylerts.
```bash
mkdir pylerts
cd pylerts
```
* Clone the repository.
```bash
git clone https://github.com/zito1337/pylerts.git
```
* After cloning, navigate to the `pylerts` directory.
```bash
cd pylerts
```
* To avoid conflicts with system packages managed by `pkg`, set up and activate a Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
* Install the required dependencies inside the virtual environment using the provided `requirements.txt` file.
```bash
pip install -r requirements.txt
```
* Run the bot and wait until it initializes!
```bash
python3 -m src.pylerts_main
```
