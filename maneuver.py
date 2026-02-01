def maneuver_strategy(risk_probability, altitude):
    if risk_probability < 0.6:
        return 0.0, altitude

    delta_v = 0.02 + (risk_probability * 0.08)
    new_altitude = altitude + (risk_probability * 10)

    return round(delta_v, 3), round(new_altitude, 2)