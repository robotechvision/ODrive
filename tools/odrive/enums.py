
# TODO: This is dangerous. Transmit as part of the JSON

AXIS_STATE_UNDEFINED = 0
AXIS_STATE_IDLE = 1
AXIS_STATE_STARTUP_SEQUENCE = 2
AXIS_STATE_FULL_CALIBRATION_SEQUENCE = 3
AXIS_STATE_MOTOR_CALIBRATION = 4
AXIS_STATE_SENSORLESS_CONTROL = 5
AXIS_STATE_ENCODER_INDEX_SEARCH = 6
AXIS_STATE_ENCODER_OFFSET_CALIBRATION = 7
AXIS_STATE_CLOSED_LOOP_CONTROL = 8
AXIS_STATE_LOCKIN_SPIN = 9
AXIS_STATE_ENCODER_DIR_FIND = 10
AXIS_STATE_HOMING = 9

class errors:
    class axis:
        ERROR_NONE = 0x00
        ERROR_INVALID_STATE = 0x01 #<! an invalid state was requested
        ERROR_DC_BUS_UNDER_VOLTAGE = 0x02
        ERROR_DC_BUS_OVER_VOLTAGE = 0x04
        ERROR_CURRENT_MEASUREMENT_TIMEOUT = 0x08
        ERROR_BRAKE_RESISTOR_DISARMED = 0x10 #<! the brake resistor was unexpectedly disarmed
        ERROR_MOTOR_DISARMED = 0x20 #<! the motor was unexpectedly disarmed
        ERROR_MOTOR_FAILED = 0x40 # Go to motor.hpp for information, check odrvX.axisX.motor.error for error value 
        ERROR_SENSORLESS_ESTIMATOR_FAILED = 0x80
        ERROR_ENCODER_FAILED = 0x100 # Go to encoder.hpp for information, check odrvX.axisX.encoder.error for error value
        ERROR_CONTROLLER_FAILED = 0x200
        ERROR_POS_CTRL_DURING_SENSORLESS = 0x400
        ERROR_WATCHDOG_TIMER_EXPIRED = 0x800

    class motor:
        ERROR_NONE = 0
        ERROR_PHASE_RESISTANCE_OUT_OF_RANGE = 0x0001
        ERROR_PHASE_INDUCTANCE_OUT_OF_RANGE = 0x0002
        ERROR_ADC_FAILED = 0x0004
        ERROR_DRV_FAULT = 0x0008
        ERROR_CONTROL_DEADLINE_MISSED = 0x0010
        ERROR_NOT_IMPLEMENTED_MOTOR_TYPE = 0x0020
        ERROR_BRAKE_CURRENT_OUT_OF_RANGE = 0x0040
        ERROR_MODULATION_MAGNITUDE = 0x0080
        ERROR_BRAKE_DEADTIME_VIOLATION = 0x0100
        ERROR_UNEXPECTED_TIMER_CALLBACK = 0x0200
        ERROR_CURRENT_SENSE_SATURATION = 0x0400
        ERROR_CURRENT_LIMIT_VIOLATION = 0x1000

    class encoder:
        ERROR_NONE = 0
        ERROR_UNSTABLE_GAIN = 0x01
        ERROR_CPR_POLEPAIRS_MISMATCH = 0x02
        ERROR_NO_RESPONSE = 0x04
        ERROR_UNSUPPORTED_ENCODER_MODE = 0x08
        ERROR_ILLEGAL_HALL_STATE = 0x10
        ERROR_INDEX_NOT_FOUND_YET = 0x20

    class controller:
        ERROR_NONE = 0
        ERROR_OVERSPEED = 0x01
        ERROR_INVALID_INPUT_MODE = 0x02
        ERROR_UNSTABLE_GAIN = 0x04
        ERROR_INVALID_MIRROR_AXIS = 0x08

MOTOR_TYPE_HIGH_CURRENT = 0
#MOTOR_TYPE_LOW_CURRENT = 1
MOTOR_TYPE_GIMBAL = 2

CTRL_MODE_VOLTAGE_CONTROL = 0
CTRL_MODE_CURRENT_CONTROL = 1
CTRL_MODE_VELOCITY_CONTROL = 2
CTRL_MODE_POSITION_CONTROL = 3

INPUT_MODE_INACTIVE = 0
INPUT_MODE_PASSTHROUGH = 1
INPUT_MODE_VEL_RAMP = 2
INPUT_MODE_POS_FILTER = 3
INPUT_MODE_MIX_CHANNELS = 4
INPUT_MODE_TRAP_TRAJ = 5
INPUT_MODE_CURRENT_RAMP = 6
INPUT_MODE_MIRROR = 7

ENCODER_MODE_INCREMENTAL = 0x00
ENCODER_MODE_HALL = 0x01
ENCODER_MODE_SINCOS = 0x02
ENCODER_MODE_SPI_ABS_CUI = 0x100
ENCODER_MODE_SPI_ABS_AMS = 0x101
