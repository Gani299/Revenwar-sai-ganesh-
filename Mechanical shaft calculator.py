import math
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mechanical Shaft Design Calculator", page_icon="⚙️", layout="centered"
)


def calculate_torque(force, radius):
  """Calculate torque: T = F * r"""
  return force * radius


def calculate_power(torque, rpm):
  """Calculate transmitted power in watts: P = 2*pi*N*T / 60"""
  return (2 * math.pi * rpm * torque) / 60


def calculate_shear_stress(torque, diameter):
  """Calculate maximum shear stress for a solid circular shaft.

  τ = 16T / (πd³)
  """
  return (16 * torque) / (math.pi * diameter**3)


def calculate_diameter(torque, allowable_stress):
  """Calculate required diameter for a solid circular shaft.

  d = [16T / (πτ)]^(1/3)
  """
  return ((16 * torque) / (math.pi * allowable_stress)) ** (1 / 3)


def main():
  st.title("⚙️ Mechanical Shaft Design Calculator")
  st.write(
      "Easily calculate torque, transmitted power, maximum shear stress, and"
      " required shaft diameter for solid circular shafts."
  )

  # Sidebar Navigation Menu
  st.sidebar.header("Navigation")
  choice = st.sidebar.radio(
      "Select Calculation Type:",
      [
          "1. Calculate Torque",
          "2. Calculate Transmitted Power",
          "3. Calculate Shear Stress",
          "4. Calculate Required Shaft Diameter",
      ],
  )

  st.markdown("---")

  if choice == "1. Calculate Torque":
    st.subheader("Calculate Torque")
    st.latex(r"T = F \times r")

    force = st.number_input("Enter force (N):", min_value=0.0, value=100.0)
    radius = st.number_input("Enter shaft radius (m):", min_value=0.0, value=0.05)

    if st.button("Calculate Torque", type="primary"):
      torque = calculate_torque(force, radius)
      st.success(f"**Torque = {torque:.3f} N·m**")

  elif choice == "2. Calculate Transmitted Power":
    st.subheader("Calculate Transmitted Power")
    st.latex(r"P = \frac{2\pi N T}{60}")

    torque = st.number_input("Enter torque (N·m):", min_value=0.0, value=50.0)
    rpm = st.number_input(
        "Enter rotational speed (RPM):", min_value=0.0, value=1440.0
    )

    if st.button("Calculate Power", type="primary"):
      power = calculate_power(torque, rpm)
      st.success(f"**Power = {power:.3f} W**")
      st.info(f"**Power = {power / 1000:.3f} kW**")

  elif choice == "3. Calculate Shear Stress":
    st.subheader("Calculate Maximum Shear Stress")
    st.latex(r"\tau = \frac{16T}{\pi d^3}")

    torque = st.number_input("Enter torque (N·m):", min_value=0.0, value=50.0)
    diameter = st.number_input(
        "Enter shaft diameter (m):", min_value=0.001, value=0.02
    )

    if st.button("Calculate Shear Stress", type="primary"):
      stress = calculate_shear_stress(torque, diameter)
      st.success(f"**Maximum shear stress = {stress:.3f} Pa**")
      st.info(f"**Maximum shear stress = {stress / 1e6:.3f} MPa**")

  elif choice == "4. Calculate Required Shaft Diameter":
    st.subheader("Calculate Required Shaft Diameter")
    st.latex(r"d = \left(\frac{16T}{\pi \tau}\right)^{1/3}")

    torque = st.number_input("Enter torque (N·m):", min_value=0.0, value=50.0)
    allowable_stress = st.number_input(
        "Enter allowable shear stress (Pa):", min_value=1.0, value=50e6
    )

    if st.button("Calculate Diameter", type="primary"):
      diameter = calculate_diameter(torque, allowable_stress)
      st.success(f"**Required shaft diameter = {diameter:.4f} m**")
      st.info(f"**Required shaft diameter = {diameter * 1000:.2f} mm**")


if __name__ == "__main__":
  main()
