# Instagram Analyzer 📊

A Python-based tool that analyzes Instagram followers and following data to identify:
- People you follow but who don’t follow you back
- People who follow you but you don’t follow back
- Mutual followers
- Summary statistics

The project is containerized using Docker for easy setup and portability.

---

## 🚀 Features
- Reads `followers.csv` and `following.csv`
- Finds non-reciprocal relationships
- Identifies mutual connections
- Provides summary counts
- Dockerized for consistent execution

---

## 🛠️ Tech Stack
- Python 3.10
- Pandas
- Docker

---

## 📁 Project Structure
Instagram-Analyzer/
│── app.py
│── requirements.txt
│── Dockerfile
│── followers.csv
│── following.csv
│── README.md

---

## ⚙️ Run Locally

### 1. Install dependencies

pip install -r requirements.txt


### 2. Run the script

python app.py


---

## 🐳 Run with Docker

### 1. Build image

docker build -t instagram-analyzer .


### 2. Run container

docker run --rm instagram-analyzer


---

## 📊 Output Example

=== People you follow but they don't follow back ===
user1
user2

=== People who follow you but you don't follow back ===
user3
user4

=== Summary ===
Following: 129
Followers: 130
Mutual: 124


---

## 📌 Notes
- Ensure CSV files are in the same directory as `app.py`
- File names are case-sensitive in Docker
- Rebuild Docker image if files are updated

---
