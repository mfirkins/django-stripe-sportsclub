# django-stripe-sportsclub
A [Django]("https://www.djangoproject.com/") web app using the [Stripe Python SDK]("https://github.com/stripe/stripe-python") API.

## Table of Contents
* [General Info](#General-Info)
* [Technologies](#Technologies)
* [Author Info](#Author-Info)

## General Info
Version: 2.0, 17/04/2025<br>

This repository is public version of a web app that was commissioned by a sports club to:
* Allow members to view the types of matches available for the sports club
* Allow members to book a match
* Pay the fee for the match via [Stripe]("https://stripe.com") as a payment processor
* Provide an authentication system to allow committee and admins to login to the admin dashboard
* Provide an easy to use admin dashboard for the committee of the sports club to:
    * View all bookings made by members
    * View matches available to members
    * View the status of payments
    * Export all bookings to be able to print out

## Technologies
Created in Python 3.10
Along with:
* Django 4.1.5
* Stripe Python SDK v5 ([uses the legacy pattern]("https://github.com/stripe/stripe-python/wiki/Migration-guide-for-v8-(StripeClient)"))
* [Django Jazzmin]("https://github.com/farridav/django-jazzmin")
## Author Info
Name: Morgan Firkins<br>
GitHub: https://github.com/mfirkins<br>
## Additional Notes & Contributions
Thanks to [palzino]("https://github.com/palzino") for contributing to the original project
In the future the repository will upgrade its dependencies, especially the new StripeClient pattern and updating the Stripe Python SDK to a version >= 8.
<a href="https://www.freepik.com/free-photo/tennis-racket-minimal-still-life_12351967.htm">Images by freepik</a>
