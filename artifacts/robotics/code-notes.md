# How I Read This Robot Program

The [code sample](user_main.py) is copied from my working robotics repository. It is based on Zebra Robotics starter code and needs the `robot.ackermann` library on the matching robot hardware. It will not run as a normal desktop Python program.

## The parts I look at

| Part | What it does |
| --- | --- |
| `AckermannDrive(...)` | Sets the drive-motor port to 3 and steering port to 2, with a center angle of 90. |
| `drive.drive(...)` | Sends a speed and steering command to the controller. |
| `asyncio.sleep_ms(...)` | Waits a fixed number of milliseconds before the next command. |
| Repeated movement blocks | Repeat straight and turning commands. |
| `drive.stop()` and `drive.steer_center()` | Stop the motor and center the steering. |

The display says “square,” but that label does not prove the robot traced an exact square. I would need to measure the actual path to check that.

The code also sends a steering value of `0` while the controller setup lists a minimum of `45`. I need to check how the Zebra library handles that value before claiming a particular turn angle. I have kept the original code unchanged so this example matches my saved work.

## A limitation I can explain

The robot waits for a set time, rather than checking that it has reached a position. If the wheels slip or the speed changes, the path could change too. A useful next test would compare repeated runs with the same settings and record where the robot stops.

No hardware run was performed as part of preparing this public copy.

[Robotics project](../../projects/robotics.md) · [Portfolio home](../../README.md)
