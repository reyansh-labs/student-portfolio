"""Timed Ackermann-drive motion prototype.

Based on the Zebra Robotics Ackermann-drive example. This program requires
the platform-specific robot.ackermann library. The current version uses fixed
motor speeds, steering angles, and delays; it does not read sensors, use a
camera, detect obstacles, or calculate a path.
"""

import uasyncio as asyncio
from robot.ackermann import AckermannDrive


async def main(zbot):
    drive = AckermannDrive(
        zbot,
        drive_motor_port=3,
        steering_port=2,
        center_angle=90,
        min_angle=45,
        max_angle=135,
    )

    zbot.display("Ackermann", "Forward")
    drive.drive(-40, 90)
    await asyncio.sleep_ms(1200)

    zbot.display("Ackermann", "square")
    drive.drive(-90, 90)
    await asyncio.sleep_ms(5500)

    drive.drive(-100, 0)
    await asyncio.sleep_ms(3000)

    drive.drive(-90, 90)
    await asyncio.sleep_ms(5250)

    drive.drive(-100, 0)
    await asyncio.sleep_ms(3000)

    drive.drive(-90, 90)
    await asyncio.sleep_ms(5250)

    drive.drive(-100, 0)
    await asyncio.sleep_ms(3000)

    drive.drive(-90, 90)
    await asyncio.sleep_ms(5250)

    drive.drive(-100, 0)
    await asyncio.sleep_ms(3000)

    zbot.display("Ackermann", "Stopped")
    drive.stop()
    drive.steer_center()

    while True:
        await asyncio.sleep_ms(1000)

