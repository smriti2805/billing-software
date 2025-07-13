# 🧾 Billing Software

Welcome to the **Python Billing Software** project! This is a user-friendly, GUI-based billing system built using `Tkinter`, ideal for small retail businesses or educational purposes. It features product categorization, dynamic bill generation, customer information tracking, and persistent bill storage.

![Billing Software UI](https://img.freepik.com/free-vector/invoice-concept-illustration_114360-3605.jpg)

## 📦 Features

* 🧍 Customer Information Entry
* 🛒 Product Category and Subcategory Selection
* 💰 Automatic Price and Tax Calculation
* 🧾 Bill Generation with Save and Print Options
* 🔍 Search Bills by Bill Number
* 🧹 Clear and Reset the Application
* 📂 Bill History Stored in `/bills/`

## 🗂️ Project Structure

```
smriti2805-billing-software/
├── billing system.py     # Main Application File
└── bills/                # Folder to Store Generated Bills
    ├── 88414.txt
    └── 91375.txt
```

## 🚀 Getting Started

### ✅ Requirements

* Python 3.x
* `Pillow` library for image processing

### ▶️ Run the App

```bash
python "billing system.py"
```

> 💡 Ensure the `image/` directory with referenced images exists for proper GUI display.

## 🖥️ GUI Overview

* Built using `Tkinter` with clean sectioning:

  * Customer Info
  * Product Selection
  * Billing Area
  * Summary and Bill Controls

## 📊 Categories and Products

* **Clothing:** Pants, T-Shirts, Shirts
* **Lifestyle:** Soaps, Creams, Hair Oils
* **Mobiles:** iPhones, Samsung, Xiaomi, Realme, OnePlus

Each product has pre-defined pricing and tax rate of 1%.

## 💾 Bill Format Example

```
 Welcome Mini Mall
 Bill Number: 88414
 Customer Name:
 Phone Number:
 Customer Email:

==========================================
 Products            QTY    Price
==========================================
Ponds                1      20
Roadster             1      1800
Iphone 12            1      85000

==========================================
 Sub Amount:         Rs.86820.00
 Tax Amount:         Rs.868.20
 Total Amount:       Rs.87688.20
==========================================
```

## 🧪 Sample Bills

Check out the `bills/` directory to view saved bill samples like `88414.txt` and `91375.txt`.

<!--
## 📸 UI Screenshots

You can enhance this section by including GUI screenshots to illustrate the app layout.

--->

## ⚠️ Notes

* Ensure image paths are correctly set.
* Use unique bill numbers to avoid file overwrite.

## 📃 License

This project is intended for educational and learning purposes only.

---

Made with ❤️ using Python & Tkinter
