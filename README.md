[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://github.com/hacs/integration)

# manish-custom-notifier-
manish custom notifier for HomeAssistant allows you to send whatsapp notification using Whatsapp Cloud API easily and with minimal configuration.

## Limitations
* 1000 free messages per month (Free tier)
* It is only possible to send messages other than templates after the target phone responds to an initial message (Unless you use Template messages)
* You can't send message to a group

## Getting started
First you’ll need to follow the [instructions on this page](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started) to:

* Register as a Meta Developer
* Enable two-factor authentication for your account
* Create a Meta App – you need to create a Business App for WhatsApp

Once you’ve done that, go to your app and set up the WhatsApp product.

[![New app](https://techblog.co.il/wp-content/uploads/2022/12/new-app.png "New App")](https://techblog.co.il/wp-content/uploads/2022/12/new-app.png "New App")

You’ll be given a temporary access token and a Phone Number ID, note these down as you’ll need them later. Set up your own phone number as a recipient and you can have a go at sending yourself a test message:

[![Getting started](https://techblog.co.il/wp-content/uploads/2022/12/test-number.png "Getting started")](https://techblog.co.il/wp-content/uploads/2022/12/test-number.png "Getting started")

### Set Up Message Template

In the test message above, you used the **hello_world** template. You’ll need to set up your own template for your own purposes. If you go to [“Message Templates”](https://business.facebook.com/wa/manage/message-templates/) in the WhatsApp manager you can build your own templates.

In the following example, i created a template for my smat home. The template header if fixed and so is the footer. in the body i added variable for dynamic text:

[![Smart Home Template](https://techblog.co.il/wp-content/uploads/2022/12/my-template.png "Smart Home Template")](https://techblog.co.il/wp-content/uploads/2022/12/my-template.png "Smart Home Template")


Once you're done with the above ,you're ready to start send notifications using **manish**.


### Installation
manish is now part ot the Default HACS repositories list.
Just add it from the Integrations list.

### Configuration
To use the custom notification, we need to add some linse to the configuration.yaml file.

```yaml
notify:
  - platform: manish
    name: MaNish whatsapp notifire
    target: # WhatsApp number for notificatin (Without the + sign of the country_code)
    token: #T he token for the Whatsapp cloud API
    phone_number_id: #Phone number id from the Whatsapp cloud API
    template: # Template's name's to use
    language: # Template's language
```

Restart HomeAssistant and you should see a new service :
[![manish custom component](https://github.com/t0mer/manish-custom-notifier/blob/main/screenshots/manish-notification-service.png?raw=true "manish custom component")](https://github.com/t0mer/manish-custom-notifier/blob/main/screenshots/manish-notification-service.png?raw=true "manish custom component")