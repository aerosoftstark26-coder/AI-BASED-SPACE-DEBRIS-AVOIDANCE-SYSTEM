import numpy as np
from skyfield.api import load
from tle_loader import load_satellite, load_debris
from sensor_module import SensorModule
from ai_decision import ai_decision
from maneuver import maneuver_strategy
from gui import launch_gui

ts = load.timescale()
sensor = SensorModule()

sat = load_satellite("ISS")
debris_list = load_debris()

if sat is None or not debris_list:
    print("TLE loading failed")
    exit()

root, status, info = launch_gui()
altitude = 420  # km

def simulation_loop():
    global altitude

    t = ts.now()

    sat_geo = sat.at(t)
    sat_pos = np.array(sat_geo.position.km)
    sat_vel = np.array(sat_geo.velocity.km_per_s)

    highest_risk = 0
    closest_distance = 1e9

    for debris in debris_list[:30]:  # limit for performance
        debris_geo = debris.at(t)
        debris_pos = np.array(debris_geo.position.km)
        debris_vel = np.array(debris_geo.velocity.km_per_s)

        distance, closing_speed = sensor.detect(
            sat_pos, sat_vel, debris_pos, debris_vel
        )

        risk = ai_decision(distance, closing_speed)

        if risk > highest_risk:
            highest_risk = risk
            closest_distance = distance

    delta_v, altitude = maneuver_strategy(highest_risk, altitude)

    if highest_risk > 0.6:
        status.config(text="⚠️ REAL DEBRIS THREAT", fg="red")
    else:
        status.config(text="✅ ORBIT SAFE", fg="green")

    info.config(
        text=f"Tracked Debris: {len(debris_list)}\n"
             f"Closest Distance: {closest_distance:.2f} km\n"
             f"Collision Risk: {highest_risk:.2f}\n"
             f"Δv Applied: {delta_v} km/s"
    )

    root.after(2000, simulation_loop)

simulation_loop()
root.mainloop()