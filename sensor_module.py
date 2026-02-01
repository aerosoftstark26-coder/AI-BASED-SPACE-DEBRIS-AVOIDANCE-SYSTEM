import numpy as np

class SensorModule:
    def detect(self, sat_pos, sat_vel, debris_pos, debris_vel):
        relative_pos = debris_pos - sat_pos
        relative_vel = debris_vel - sat_vel

        distance = np.linalg.norm(relative_pos)
        closing_speed = np.dot(relative_pos, relative_vel) / distance

        return distance, abs(closing_speed)