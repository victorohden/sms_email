### Sending SMS and Email for Free Using Python
In this repository, I am going to show how to use Python to send SMS and email for free. This is a useful feature to automate some processes. For example, you may want to create a newsletter or receive a notification when your processing ends. The process involves setting up a virtual environment and using the smtplib package. While the instructions are provided for a Windows environment with a .venv virtual environment, the process can be adapted for Conda environments and other operating systems.

It is important to mention that I am not creating this from scratch. Here are some references that I used to create it:
- https://www.youtube.com/watch?v=3247tuklMEk
- https://github.com/AdamGetbags/emailToSMS/blob/main/emailToSMSConfig.py
- https://medium.com/testingonprod/how-to-send-text-messages-with-python-for-free-a7c92816e1a4

#### Setting Up Virtual Environment
1. Ensure Python is installed on your computer.
2. Create a virtual environment using the following command:
    `python -m venv .venv`
    You can replace ".venv" with a different environment name if desired. More information [in this website](https://docs.python.org/3/library/venv.html).
3. Activate the virtual environment by navigating to ".venv\Scripts\activate".
4. Once the virtual environment is activated, you can import the [SMTP protocol client](https://docs.python.org/3/library/smtplib.html) package.

#### Configuration before sending SMS and email:

I used **GMAIL** to send SMS and e-mail. So, I need to configure the email to use on APP password. This will allow you to send emails and SMS using Python. You can find more information in these links:
- source: [YouTube](https://www.youtube.com/watch?v=YKn6iRlYd_Q) 
- [Google App Passwords](https://myaccount.google.com/apppasswords)

After creating it, you need to change the `EMAIL` and `PASSWORD` [here](send_sms_email_organize.ipynb) and [here](Scripts/send_email_sms.py).</br>

Unfortunately, you need to know the carrier from [the phone you want to send an SMS](https://gtsfleet.com/docs/SMS-Gateways-for-GTS-Fleet-Alert-Delivery.pdf).

#### Sending SMS and emails

You can use a `.py` approach or a `Jupyter Notebook` to send the SMS and e-mail. Both of them are inside this repository
- **Jupyter Notebook option:** All the functions and tips are inside this [Notebook](send_sms_email_organize.ipynb). Just change for your data and give it a try.

- **Python option:** If you want to run it on a larger scale, `.py` is a good option. You can run using [this python file](send_sms_email_organize.py). All the configurations are inside this [file](Scripts/send_email_sms.py).

**All this is working just fine in the USA; not sure about how to adapt it for different countries.**

Feel free to explore and modify the code to suit your needs!

