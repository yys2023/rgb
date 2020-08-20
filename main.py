def on_forever():
    if pins.digital_read_pin(DigitalPin.P0) == 1:
        pins.digital_write_pin(DigitalPin.P15, 1)
        basic.pause(1000)
        pins.digital_write_pin(DigitalPin.P15, 1)
        basic.pause(1000)
    else:
        pins.digital_write_pin(DigitalPin.P16, 1)
        basic.pause(500)
        pins.digital_write_pin(DigitalPin.P16, 1)
        basic.pause(500)
basic.forever(on_forever)
