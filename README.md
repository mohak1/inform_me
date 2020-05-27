# inform_me 

[![inform_me](https://img.shields.io/badge/release-v0.1.0-993BD8.svg)](https://shields.io/)
[![Build](https://img.shields.io/badge/Build-Passing-1abc9c.svg)](https://shields.io/)
[![OS](https://img.shields.io/badge/OS-Linux-1abb0c.svg)](https://shields.io/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![Format](https://img.shields.io/badge/Format-Wheel-709DF6.svg)](https://shields.io/)
[![Status](https://img.shields.io/badge/Status-Stable-1abc9c.svg)](https://shields.io/)
[![Python](https://img.shields.io/badge/Python-3.6-E11E1E.svg)](https://shields.io/)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)


inform_me is an alert raising python library that is specially designed to be used in machine learning projects during the model training stage. It triggers a Sound, Notification Box, and Popup Message alert as soon as it is executed, giving out a notification that the high-computation/time-consuming piece of code (eg. Deep Learning Model training, Web Scraper, etc) above it was successfully executed. The aim of this library is to automatically notify the developer as soon as a time-consuming program execution gets completed. As of now, this library only supports Linux distributions and does not work on Windows or macOS. It makes use of carefully selected Python's Standard Library modules which are efficient and do not stall the execution of the running program. Supports Python 3.6 and later but should work on previous versions of Python 3.x

## Installation

To install this package, use the following [pip](https://pypi.org/project/inform-me/) command from the terminal:

```bash
pip install inform_me
```

## Usage

The main purpose of inform_me is to raise an alert as soon as it gets executed. It can raise three types of alerts:
1. Beep Sound
2. System Notification Message
3. Pop-up Information Message

By default, all three alerts are raise but can be customized by passing specific method arguments. 

```python
import inform_me as im

#
# A piece of code that would take a long time to complete its execution.
#

im.inform(sound_duration=0.5, notification=True, popup=True, message='Your process has completed!')
#sound_duration: Time in seconds till which the beep alarm will sound.
#notification: Boolean value stating whether to show notification alert.
#popup: Boolean value stating whether to show pop-up message alert.
#message: The message to be displayed in notification and pop-up.
```
The inform method would get called after the time-consuming code completes its execution. As soon as the im.inform method is called, it would trigger a system-wide alert letting the developer know that the time-consuming code has been completely executed (i.e. the model has been trained or webpage has been scraped, etc.)

Another feature of inform_me is the 'inform_after' method which raises an alert after the specified amount of time (in seconds and minutes). It could come handy if the user is taking a break from work (by switching to some other task or window) and would like to return to it after a specific amount of time. This method allows the user to specify the time in minutes and seconds along with a custom message which gets displayed after the time lapses. This method can serve as a reminder tool as well.
```python
import inform_me as im

im.inform_after(seconds=10, minutes=0, notification=True, popup=True, message=None):
#seconds: Time in seconds after which the alarm would sound.
#notification: Boolean value stating whether to show notification alert.
#popup: Boolean value stating whether to show pop-up message alert.
#message: The message to be displayed when time lapses.
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)


