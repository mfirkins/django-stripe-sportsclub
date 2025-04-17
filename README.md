# django-stripe-sportsclub
A [Django](https://www.djangoproject.com) web app using the [Stripe Python SDK](https://github.com/stripe/stripe-python).

## Table of Contents
* [General Info](#General-Info)
* [Environment Variables](#Environment-Variables)
* [Technologies](#Technologies)
* [Author Info](#Author-Info)
* [Additional Notes & Contributions](#Additional-Notes-&-Contributions)

## General Info
Version: 2.0, 17/04/2025<br>

This repository is public version of a web app that was commissioned by a sports club to:
* Allow members to view the types of matches available for the sports club
* Allow members to book a match
* Pay the fee for the match via [Stripe](https://stripe.com) as a payment processor
* Provide an authentication system to allow committee and admins to login to the admin dashboard
* Provide an easy to use admin dashboard for the committee of the sports club to:
    * View all bookings made by members
    * View matches available to members
    * View the status of payments
    * Export all bookings to be able to print out

## Environment Variables
The environment variables used are mainly for setting up requests with the [Stripe Python SDK](https://github.com/stripe/stripe-python). Here is a list of the environment variables needed:
* STRIPE_PK_KEY: Public Key for your Stripe API credentials
* STRIPE_SK_KEY: Secret Key for your Stripe API credentials
* STRIPE_WH_SECRET: Secret for your Stripe Webhook
* STRIPE_CONN_ID: ID of the connected account in Stripe to transfer purchase to
* STRIPE_DOMAIN_URL: URL for your web app
* STRIPE_PRODUCT_LIMIT: Product Limit for Stripe to pull through (set to however many products you have/want, has to be an integer)
* STRIPE_PERCENT_FEE: Adds a percentage fee to a transaction (set to 0.00 if not needed)
* STRIPE_AMOUNT_FEE: Adds a decimal fee to a transaction (set to 0.00 if not needed)

You can see them set in the <b>core/settings.py</b> file from there, they are imported elsewhere when need in the web app.

## Technologies
Created in Python 3.10
Along with:
* Django 4.1.5
* Stripe Python SDK v5 ([uses the legacy pattern](https://github.com/stripe/stripe-python/wiki/Migration-guide-for-v8-(StripeClient)))
* [Django Jazzmin](https://github.com/farridav/django-jazzmin)
## Author Info
Name: Morgan Firkins
GitHub: https://github.com/mfirkins
## Additional Notes & Contributions
Thanks to [palzino](https://github.com/palzino) for contributing to the original project.
In the future the repository will upgrade its dependencies, especially the new StripeClient pattern and updating the Stripe Python SDK to a version >= 8.
<a href="https://www.freepik.com/free-photo/tennis-racket-minimal-still-life_12351967.htm">Images by freepik</a>
