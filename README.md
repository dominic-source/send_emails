# How to send emails using this short method

## Requirements
>
> To use this module, import `mailSender` from `quickmail` and invoke it.
> You need your gmail password and username eg. <example@gmail.com>
> You need the address of who you want to send it to.
>
## 2-step verification gmail
>
> If you use a 2 step verification for your email, create an app password from your gmail account.
> This password is what you will use for sending the email.
> Please, make sure that your password is safe, do not expose it.

## Normal gmail verification
>
> You will just use your password here, since you don't have a two step verification.

## How to start sending
>
> Add your password to your `.env` file. The key is `GTP`, and the value is the password without quotes
`example: GTP=password`.
> invoke the function with keyword arguments such as these:

* sub= None
* body=None
* addr="smtp.gmail.com"
* pas=None,
* sen=None
* rec=None
* port=465
They all have default value which are listed above, however, the sender address (sen),
the receiver address (rec), the password (pas), are strictly required.
The Subject (sub) and body are also needed.
The addr is defaulted to "smtp.gmail.com" and the port is defaulted to "465" these values should not be changed.

YOU are advised never to push your password into any platform.
