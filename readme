# Parking Monitoring System

## Overview
This project is a parking monitoring system that uses a camera to capture images, analyzes them using Alibaba DashScope API, and sends SMS alerts via Alibaba Cloud SMS service when no parking spaces are available.

## Features
- **Image Analysis**: Uses Alibaba DashScope API to analyze parking lot images.
- **SMS Alerts**: Sends SMS notifications when no parking spaces are available.
- **Daytime Mode**: Option to monitor only during daytime hours.
- **Environment Variables**: Sensitive information is stored in a `.env` file for security.

## Project Structure
```
left_parking/
├── [detect_park.py](http://_vscodecontentref_/0)          # Main script
├── [ali_sms.py](http://_vscodecontentref_/1)              # SMS sending module
├── [dashscope_client.py](http://_vscodecontentref_/2)     # Image analysis module
├── [.env.example](http://_vscodecontentref_/3)            # Example environment variables file
```

## Prerequisites
1. Python 3.9 or later
2. Install dependencies
3. Create a .env file Copy the .env.example

```
conda create --name parking python=3.9 -y
conda activate parking
pip install -r requirements.txt
cp .env.example .env
```

## Run
```
python detect_park.py --frequency 1 --mode all
```
