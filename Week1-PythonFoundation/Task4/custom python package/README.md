# Custom Package: `custom_pkg` 📦

## Overview

`custom_pkg` is a **custom-built Python package** that provides **basic calculator operations** and **geometry-related calculations**.  
It is designed to be **reusable, modular**, and easy to integrate into other Python projects.

This package demonstrates **how to organize Python code into modules and packages**, exposing clean functions for common mathematical and geometric tasks.

---

## 🏗 Package Structure

The `custom_pkg` package has the following structure:

    custom_pkg/           # 📦 Root folder (package)
    ├── __init__.py       # Initializes the package, imports functions for easy access
    ├── calculator.py     # 🧮 Module for basic arithmetic operations
    └── geometry.py       # 📐 Module for geometry calculations


- **`__init__.py`**: Makes the folder a Python package.  
- **`calculator.py`**: Contains arithmetic functions such as addition, subtraction, multiplication, and division.  
- **`geometry.py`**: Contains functions to calculate areas and perimeters of shapes such as circles, rectangles, and triangles.

---

## ⚙ How the Custom Package was Created

### Module Creation
- Each module is a separate Python file (`.py`) containing logically grouped functions.  
- `calculator.py` handles arithmetic operations.  
- `geometry.py` handles geometric calculations.  

### Package Creation
- Created a folder named `custom_pkg`.  
- Added an `__init__.py` file to initialize the package.  
- Imported functions from modules inside `__init__.py` so they can be accessed directly when importing the package.


## 🧮 Functionality of Each Module

### 1️⃣ Calculator Module (`calculator.py`)

Contains **basic arithmetic operations**:

| Function | Description | Example |
|----------|------------|---------|
| `add(a, b)` | Returns the sum of `a` and `b` | `add(2, 3)` → 5 |
| `subtract(a, b)` | Returns the difference `a - b` | `subtract(5, 2)` → 3 |
| `multiply(a, b)` | Returns the product of `a` and `b` | `multiply(4, 5)` → 20 |
| `divide(a, b)` | Returns the quotient `a / b` | `divide(10, 2)` → 5.0 |

---

### 2️⃣ Geometry Module (`geometry.py`)

Contains **functions to calculate area and perimeter** for common shapes.

#### Circle
| Function | Description | Example |
|----------|------------|---------|
| `circle_area(radius)` | Area = π × radius² | `circle_area(5)` → 78.54 |
| `circle_perimeter(radius)` | Perimeter (circumference) = 2 × π × radius | `circle_perimeter(5)` → 31.42 |

#### Rectangle
| Function | Description | Example |
|----------|------------|---------|
| `rectangle_area(length, width)` | Area = length × width | `rectangle_area(4, 6)` → 24 |
| `rectangle_perimeter(length, width)` | Perimeter = 2 × (length + width) | `rectangle_perimeter(4, 6)` → 20 |

## 🚀 Usage

```python
from custom_pkg import add, circle_area

print(add(2, 3))       # Output: 5
print(circle_area(5))  # Output: 78.5398...

