import time
import config

class Week5:
    def __init__(self, led_1, ult_1, motors_1, servo_1):
        self.led_1 = led_1
        self.ult_1 = ult_1
        self.motors_1 = motors_1
        self.servo_1 = servo_1

    def show_ult_distance(self, goal = 0):
        # Dynamically adjust the led color based on the distance from the object
        # How much to scale down the brightness so not overly bright
        scale = 10
        full_color = 255 / scale
        # Distance in cm
        threshold_1 = 10
        threshold_2 = 75
        red = 0
        green = 0
        blue = 0

        dist = self.ult_1.distance_cm() - goal
        # Just red (STOP!)
        if dist < threshold_1:
            red = (threshold_1 - dist) * full_color
        # Yellow (SLOW DOWN!)
        elif dist >= threshold_1 and dist < threshold_2:
            # Full red at threshold_1, no red at threshold_2
            red = full_color *  ( 1 - (dist - threshold_1)/(threshold_2 - threshold_1))
            # Full green at threshold_2, no green at threshold_3x
            green = full_color * (dist-threshold_1)/(threshold_2 -threshold_1)
        # Green (GO)
        else:
            green = full_color
        print("dist: ",dist)
        self.led_1[0] = [int(red), int(green), int(blue)]
        self.led_1.write()

    def run(self):
        # This sample script spins in a circle for two seconds.
        # Try writing scripts of your own!

        # TODO: implement your code here
        # Remember to use self in front of your variable names

        print("Going forward")
        self.motors_1.set_right(400)
        self.motors_1.set_left(400)
        time.sleep(2)
        print("Stop")
        self.motors_1.set_right(0)
        self.motors_1.set_left(0)

        # Exit our loop using a global variable!
        config.current_state = 1

    def servo_sweep(self):
        # The ranges on the servo are [-90 degrees, 90 degrees]
        sweep = [-90, -45, 0, 45, 90]
        for angle in sweep:
            self.servo_1.set(angle)
            self.show_ult_distance()
            time.sleep(1)
        # Exit our loop using a global variable!
        config.current_state = 1

    def magic(self):
        # TODO: implement anything you can think of here!!!
        pass

    def drive_to_dist(self, goal = 0):
        # TODO: implement your code here
        # Remember to use self in front of your variable names

        speed_fast = 500
        speed_med = 200
        speed_slow = 100

        threshold_0 = 2
        threshold_1 = 10
        threshold_2 = 75
        dist = self.ult_1.distance_cm() - goal

        if dist > threshold_2:
            # GO GO GO
            pass

        elif dist > threshold_1:
            # Slowing Down
            pass

        elif dist > threshold_0:
            # Coming to STOP
            pass

        else:
            # STOP STOP
            pass
        self.show_ult_distance(goal)

        # TODO Version 1: See if you can get the robot to drive to a certain distance!
        # Hint: You will want to use a loop and have the robot drive forward if behind the goal
        # and backwards if behind the goal (Use the light code if statement as a reference, you want to go slower
        # at yellow and almost stop at close to red)

        # TODO Version 2: See if you can now make the robot go backwards when you overshoot the target,
        # while driving much more aggressively!

        # TODO Version 3: Set your speed to be proportional to your distance from the target so you reach a smooth
        # gradual stop






