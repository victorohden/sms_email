### Sending SMS and email for free using Python
It this repository I am going to show how to use python to send SMS and email for free. This is a good feature to automate some process. For example, you want to creat a newsletter or you want recieve a notification when your processing ends. The process involves setting up a virtual environment and use the `smtplib` package. While the instructions are provided for a Windows environment with a .venv virtual environment, the process can be adapted for conda environments and other operating systems.

It is importanto to mention that I am not creating this from strech. Here there are some references that I used to create it:
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

I used **GMAIL** to send SMS and e-mail. So, I need to configure the email to use on APP password. This will allow you to send emails and sms using python. You can find more information in these links:
- source:(https://www.youtube.com/watch?v=YKn6iRlYd_Q) 
- https://myaccount.google.com/apppasswords
After created it, you need change the `EMAiL` and `PASSWORD` [here](send_sms_email_organize.ipynb) and [here](Scripts/send_email_sms.py).</br>

Unfortunatly you need to know the carrier from [the phone you want to send a SMS](https://gtsfleet.com/docs/SMS-Gateways-for-GTS-Fleet-Alert-Delivery.pdf).

#### Sending SMS and emails
You can use a `.py` approach or a `Jupyter Notebook` to send the SMS and e-mail. Both of them are inside this repository
- **Jupyter Notebook option**
All the functions and tips are inside this [Notebook](send_sms_email_organize.ipynb). Just change for your data and give it a try.


- **Python option**
If you want to run it in a more large scale, `.py` is a good option. You can run using [this python file](send_sms_email_organize.py). All the configuration are inside this [file](Scripts/send_email_sms.py).


**All this is working just fine in USA, not sure about how adapt it for different countries**

Feel free to explore and modify the code to suit your needs!
