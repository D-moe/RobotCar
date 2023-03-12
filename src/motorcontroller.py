import machine, time
from machine import Pin, PWM

def abs(val):
    if val < 0:
        return -val
    else:
        return val

class MotorController:
    def __init__(self, standby, pwm_a, a_in, pwm_b, b_in):
        self.standby = Pin(standby, mode=Pin.OUT, pull = None)
        self.pwm_a = PWM(Pin(pwm_a))
        self.a_in = Pin(a_in, mode=Pin.OUT, pull = None)
        self.pwm_b = PWM(Pin(pwm_b))
        self.b_in = Pin(b_in, mode=Pin.OUT, pull = None)
        # Start in standby so no movement
        self.standby.value(0)
    # val range from -1023 to 1023x
    def set(self, val, control, pwm):
          # Change the motor out of standby
        if val == 0:
            self.standby.value(0)
        else:
            self.standby.value(1)

        reverse = val < 0
        mag = abs(val)
        if reverse:
            control.value(0)
        else:
            control.value(1)

        pwm.duty(mag)

    def set_right(self, val):
        # Change the motor out of standby
        self.set(val, self.a_in, self.pwm_a)

    def set_left(self, val):
        # Change the motor out of standby
        self.set(val, self.b_in, self.pwm_b)
'''
if (controlED == control_enable) //Enable motot control？
  {
    digitalWrite(PIN_Motor_STBY, HIGH);
    { //A...Right

      switch (direction_A) //movement direction control
      {
      case direction_just:
        digitalWrite(PIN_Motor_AIN_1, HIGH);
        analogWrite(PIN_Motor_PWMA, speed_A);
        break;
      case direction_back:

        digitalWrite(PIN_Motor_AIN_1, LOW);
        analogWrite(PIN_Motor_PWMA, speed_A);
        break;
      case direction_void:
        analogWrite(PIN_Motor_PWMA, 0);
        digitalWrite(PIN_Motor_STBY, LOW);
        break;
      default:
        analogWrite(PIN_Motor_PWMA, 0);
        digitalWrite(PIN_Motor_STBY, LOW);
        break;
      }
    }

    { //B...Left
      switch (direction_B)
      {
      case direction_just:
        digitalWrite(PIN_Motor_BIN_1, HIGH);

        analogWrite(PIN_Motor_PWMB, speed_B);
        break;
      case direction_back:
        digitalWrite(PIN_Motor_BIN_1, LOW);
        analogWrite(PIN_Motor_PWMB, speed_B);
        break;
      case direction_void:
        analogWrite(PIN_Motor_PWMB, 0);
        digitalWrite(PIN_Motor_STBY, LOW);
        break;
      default:
        analogWrite(PIN_Motor_PWMB, 0);
        digitalWrite(PIN_Motor_STBY, LOW);
        break;
      }
    }
  }
  else
  {
    digitalWrite(PIN_Motor_STBY, LOW);
    return;
  }
}

'''