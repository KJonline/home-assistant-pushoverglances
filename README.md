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

1) Click the below to add the repository to HACS via a custom repository.

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=KJonline&repository=home-assistant-pushoverglances&category=Integration)


2) Following the on screen instructions

3) Click the option to download the component from the HACS store.

4) After this is done a restart of Home Assistant is required.

5) Once this is compelte you can click the below button to install the component.


[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=pushoverglances)


## How to send update with notify service
```yaml
action: notify.pushover_glances
data:
  title: Lights
  data:
    ## Not all of these are required only 1 will be shown, we are just them all for completeness
    count: 6
    percent: 100
    subtext: 6 Lights currently on
  message: Lights

```

Below is a screenshot showing the fields available and what they mean as per the [Pushover](https://pushover.net/api/glances) documentation

![Field-Definitions](/images/Pushover-Glances-Field-Definitions.png?raw=true "Field Definitions for Pushover Glances")


## Automation Example
```yaml
description: ""
mode: single
triggers:
  - trigger: state
    entity_id:
      - light.light1
      - light.light2
      - light.light3
    to: "on"
conditions: []
actions:
  - action: notify.pushover_glances
    metadata: {}
    data:
      message: Lights update
      title: Lights
      data:
        count: 3 
        percent: 100
        subtext: 3 Lights currently on

```

# More information
* I invite you to read about this component and more [on Amir974's blog](http://www.virtualida.com/2016/11/status-of-my-smart-home/)
