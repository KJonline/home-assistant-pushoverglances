## Overview
**pushoverglances/notify.py** is a custom component for the Home Assistant home automation platform.

This component allows you to send information from Home Assistant to complications on an Apple Watch.  It uses the ["Glances"](https://pushover.net/api/glances) feature of [Pushover](https://pushover.net).

This component was original created by Amir974 for and the original source can be found here: https://github.com/Amir974/home-assistant-custom-components

Learn more about [Home-assistant](https://home-assistant.io/)

## Pushover - Glances
While Home-Assistant already has a [notification platform implementation for pushover](https://home-assistant.io/components/notify.pushover/), at present it's only for sending push notifications...

This implementation of the ["Glances"](https://pushover.net/api/glances) allows you to send information directly to Apple Watch face (not as push). 

* **Notify** - (``pushoverglances``) will let you connect the service and set it up so you can send *count numeric messages* to the little info placeholder and  *short text messages* to the the larger placeholder

**You will need to get [The Pushover App](https://itunes.apple.com/us/app/pushover-notifications/id506088175?mt=8&at=1010l3fx) from the Apple app store if you haven't already...**

![Apple-Watch-Example](/images/apple-watch-with-pushover-glances.PNG?raw=true "Apple Watch with Home-Assistant Data via Pushover Glances")

# Installation Instructions
* Create a "custom_components" folder in the same directory where the configuration.yaml file is located, and sub folders for the relevant components types similar to the structure [here](https://github.com/riwifall/home-assistant-custom-components/tree/master/custom_components) just for the components you are going to use...
* Next you should take care of configuration and settings for the components - take a look at the [Yaml-Config-Example](https://github.com/Amir974/home-assistant-custom-components/tree/master/Yaml-Config-Example) folder and pay attention to the comments - it's not a straight forward copy-paste


# More information
* I invite you to read about this component and more [on Amir974's blog](http://www.virtualida.com/2016/11/status-of-my-smart-home/)
