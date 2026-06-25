# 🚂 Railway Reservation System
  ____       _      ___   _      __        __     _     __   __       ____    _____   ____    _____   ____   __     __     _      _____   ___    ___    _   _
 |  _ \     / \    |_ _| | |     \ \      / /    / \    \ \ / /      |  _ \  | ____| / ___|  | ____| |  _ \  \ \   / /    / \    |_   _| |_ _|  / _ \  | \ | | 
 | |_) |   / _ \    | |  | |      \ \ /\ / /    / _ \    \ V /       | |_) | |  _|   \___ \  |  _|   | |_) |  \ \ / /    / _ \     | |    | |  | | | | |  \| |
 |  _ <   / ___ \   | |  | |___    \ V  V /    / ___ \    | |        |  _ <  | |___   ___) | | |___  |  _ <    \ V /    / ___ \    | |    | |  | |_| | | |\  |
 |_| \_\ /_/   \_\ |___| |_____|    \_/\_/    /_/   \_\   |_|        |_| \_\ |_____| |____/  |_____| |_| \_\    \_/    /_/   \_\   |_|   |___|  \___/  |_| \_|
 
A command-line based Railway Reservation System built with Python and MySQL. This project was developed as part of a Computer Science project at JIIT Noida.

## 📋 Features

- **User Authentication** — Register and login with username/password
- **Ticket Booking** — Book train tickets between stations
- **PNR Status** — Check booking status
- **Seat Classes** — AC-1, AC-2, AC-3, and General class support
- **Train Information** — View train details, routes, and speeds
- **Station Management** — View stations with codes and distances
- **Price Management** — View ticket prices per class
- **Developer Mode** — Admin panel to manage trains, stations, routes, and prices
- **Account Management** — Update or delete your account

## 🛤️ Supported Route

```
New Delhi (NDLS) → Aligarh (ALJN) → Etawah (ETW) → Kanpur (CNB) → Lucknow (LKO)
```

## 🛠️ Tech Stack

- **Language:** Python 3
- **Database:** MySQL
- **Library:** PyMySQL

## ⚙️ Requirements

- Python 3.x
- MySQL Server
- PyMySQL library

```bash
pip install pymysql
```

## 🚀 Setup & Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/railway-reservation-system.git
cd railway-reservation-system
```

2. **Install dependencies**
```bash
pip install pymysql
```

3. **Configure MySQL**

Open `Main.py` and update your MySQL credentials:
```python
db = pymysql.connect(host="localhost", user="root", password="YOUR_PASSWORD")
```

4. **Run the project**
```bash
python Main.py
```

The program will automatically create the database and tables on first run.

## 📖 How to Use

### User
1. **Register** — Create a new account
2. **Login** — Login with your credentials
3. **Book Ticket** — Select source, destination, date and class
4. **Check PNR** — View your booking status
5. **Manage Account** — Update name/password or delete account

### Developer Mode
Access admin panel to:
- Add/modify/delete trains
- Add/modify/delete stations
- Manage ticket prices
- View all bookings and users

## 📁 Database Structure

| Table | Description |
|-------|-------------|
| `users_information` | Stores user credentials and names |
| `train_information` | Train codes, names, routes, speeds, seat counts |
| `stations_details`  | Station names, codes, routes, distances |
| `Route`             | Route numbers and station sequences |
| `booking`           | Ticket booking records |
| `Price`             | Ticket prices per class per train |

## ⚠️ Notes

- Make sure MySQL server is running before starting the program
- Default route is New Delhi to Lucknow
- Password is stored as plain text (not recommended for production)

## 👨‍💻 Developer

**Aarav Srivastava**  
B.Tech IT — JIIT Noida  

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
