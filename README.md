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
The IMS custom component can be installed manualy by downloading the files and place it under custom_components folder.

The second way is by adding the repo address to HACS custom repositories.

First, in HACS you need to add the repository to the lis of custom repositories by clicking the 3 dots on the upper right corner and click the "Custom repositories" button:

[![Manish custom notifier](https://github.com/t0mer/ims-custom-component/blob/main/screenshots/add_custom_repositories.png?raw=true "Manish custom notifier")](https://github.com/t0mer/ims-custom-component/blob/main/screenshots/add_custom_repositories.png.png?raw=true "Manish custom notifier")


Now, add the custom repository address: https://github.com/t0mer/manish-custom-notifier and under category select "Integration".

Click on the "Add button" to add the repository.

[![Manish custom notifier](https://github.com/t0mer/manish-custom-notifier/blob/main/screenshots/manish-notifier-add-hacs-repo.png?raw=true "Manish custom notifier")](https://github.com/t0mer/manish-custom-notifier/blob/main/screenshots/manish-notifier-add-hacs-repo.png?raw=true "Manish custom notifier")

You can now see that the repository has been added to the custom repositories list:

[![Manish custom notifier](https://github.com/t0mer/manish-custom-notifier/blob/main/screenshots/manish-new-repo.png?raw=true "Manish custom notifier")](https://github.com/t0mer/manish-custom-notifier/blob/main/screenshots/manish-new-repo.png?raw=true "Manish custom notifier")


Click the new repo and you will see the repo details:

[![IMS custom component](https://github.com/t0mer/manish-custom-notifier/blob/main/screenshots/manish-add-button.png?raw=true "IMS custom component")](https://github.com/t0mer/manish-custom-notifier/blob/main/screenshots/manish-add-button.png?raw=true "IMS custom component")

Now click the download button on the lower left corner:

**Restart** the Home Assistant instance to load ims integration before moving on.

### Configuration