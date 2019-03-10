This component was original created by Amir974 and can be found [https://github.com/Amir974/home-assistant-custom-components]
This component was created by Amir974 for the home-assistant open-source home automation platform.

Learn more about the [Home-assistant platform](https://home-assistant.io/)

# Included Components

See below:
 * Pushover-Glances for displaying information on Apple Watch for example

## Pushover - Glances
While Home-Assistant already had a [notification platform implementation for pushover](https://home-assistant.io/components/notify.pushover/), at present it's only for sending push notifications...

My implementation of the ["Glances" A](https://pushover.net/api/glances) allows you to send information directly to Apple Watch face (not as push). 

* **Notify** - (``pushoverglances``) will let you connect the service and set it up so you can send *count numeric messages* to the little info placeholder and  *short text messages* to the the larger placeholder

**You will want to get [The Pushover App](https://itunes.apple.com/us/app/pushover-notifications/id506088175?mt=8&at=1010l3fx) from the Apple app store if you haven't already...**

![Apple-Watch-Example](/images/apple-watch-with-pushover-glances.PNG?raw=true "Apple Watch with Home-Assistant Data via Pushover Glances")

# Installation Instructions

* I invite you to read about this component and more [on Amir974's blog](http://www.virtualida.com/2016/11/status-of-my-smart-home/)
* Create a "custom_components" folder where the configuration.yaml file is located, and sub folders for the relevant components types similar to the structure I have [here](https://github.com/Amir974/home-assistant-custom-components/tree/master/custom_components) just for the componts you are going to use...
* Next you should take care of configuration and settings for the components - take a look at the [Yaml-Config-Example](https://github.com/Amir974/home-assistant-custom-components/tree/master/Yaml-Config-Example) folder and pay attention to the comments - it's not a straight forward copy-paste
