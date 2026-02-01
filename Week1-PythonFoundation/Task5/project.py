import streamlit as st
import math
import cmath


# Basic Arithmetic
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


# Trigonometric (input in degrees)
def sin_deg(x):
    return math.sin(math.radians(x))

def cos_deg(x):
    return math.cos(math.radians(x))

def tan_deg(x):
    try:
        return math.tan(math.radians(x))
    except:
        return "Error: Undefined"


# Complex Numbers
def complex_add(a, b):
    return a + b

def complex_subtract(a, b):
    return a - b

def complex_multiply(a, b):
    return a * b

def complex_divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def complex_to_polar(z):
    r, theta = cmath.polar(z)
    return r, math.degrees(theta)

def polar_to_complex(r, theta_deg):
    theta_rad = math.radians(theta_deg)
    return cmath.rect(r, theta_rad)



# Streamlit UI
st.set_page_config(page_title="Streamlit Calculator", page_icon="🧮")
st.title("🧮 Streamlit Calculator")

# Tabs for functionality
tab1, tab2, tab3 = st.tabs(["Arithmetic", "Trigonometry", "Complex Numbers"])


# Tab 1: Arithmetic
with tab1:
    st.header("Arithmetic Operations")
    a = st.number_input("Enter first number", value=0.0)
    b = st.number_input("Enter second number", value=0.0)
    operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate"):
        if operation == "Add":
            st.success(f"Result: {add(a, b)}")
        elif operation == "Subtract":
            st.success(f"Result: {subtract(a, b)}")
        elif operation == "Multiply":
            st.success(f"Result: {multiply(a, b)}")
        elif operation == "Divide":
            st.success(f"Result: {divide(a, b)}")


# Tab 2: Trigonometry
with tab2:
    st.header("Trigonometric Functions")
    angle = st.number_input("Enter angle in degrees", value=0.0)
    trig_func = st.selectbox("Select function", ["sin", "cos", "tan"])

    if st.button("Calculate  "):
        if trig_func == "sin":
            st.success(f"sin({angle}°) = {sin_deg(angle)}")
        elif trig_func == "cos":
            st.success(f"cos({angle}°) = {cos_deg(angle)}")
        elif trig_func == "tan":
            st.success(f"tan({angle}°) = {tan_deg(angle)}")


# Tab 3: Complex
with tab3:
    st.header("Complex Number Operations")
    comp_option = st.selectbox("Choose Operation", ["Add", "Subtract", "Multiply", "Divide", 
                                                    "Rectangular → Polar", "Polar → Rectangular"])

    if comp_option in ["Add", "Subtract", "Multiply", "Divide"]:
        real1 = st.number_input("Real part of first number", value=0.0)
        imag1 = st.number_input("Imaginary part of first number", value=0.0)
        real2 = st.number_input("Real part of second number", value=0.0)
        imag2 = st.number_input("Imaginary  part of second number", value=0.0)
        z1 = complex(real1, imag1)
        z2 = complex(real2, imag2)

        if st.button("Calculate "):
            if comp_option == "Add":
                st.success(f"Result: {complex_add(z1, z2)}")
            elif comp_option == "Subtract":
                st.success(f"Result: {complex_subtract(z1, z2)}")
            elif comp_option == "Multiply":
                st.success(f"Result: {complex_multiply(z1, z2)}")
            elif comp_option == "Divide":
                st.success(f"Result: {complex_divide(z1, z2)}")

    elif comp_option == "Rectangular → Polar Form":
        real = st.number_input("Real part", value=0.0)
        imag = st.number_input("Imaginary part", value=0.0)
        z = complex(real, imag)
        if st.button("Convert to Polar Form"):
            r, theta = complex_to_polar(z)
            st.success(f"Polar Form: r = {r}, θ = {theta}°")

    elif comp_option == "Polar → Rectangular":
        r = st.number_input("Magnitude (r)", value=0.0)
        theta = st.number_input("Angle (θ in degrees)", value=0.0)
        if st.button("Convert to Rectangular"):
            z = polar_to_complex(r, theta)
            st.success(f"Rectangular Form: {z.real} + {z.imag}j")

