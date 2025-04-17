from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from matches.forms import Singles, DoublesWithNoPartner, Doubles, MixedDoubles
import stripe
from django.conf import settings
from . import models
import json

# Create your views here.

stripe.api_key = settings.STRIPE_SK_KEY


def create_checkout_session(matchname, orderId):
    print("got to view")
    domain_url = settings.STRIPE_DOMAIN_URL
    products = stripe.Product.list(limit=settings.STRIPE_PRODUCT_LIMIT)
    products = products.get("data")
    product_name = ""
    if matchname == "dnp":
        product_name = "Doubles - No Partner"
    elif matchname == "sm":
        product_name = "Singles Match"
    elif matchname == "dm":
        product_name = "Doubles Match"
    elif matchname == "mdm":
        product_name = "Mixed Doubles Match"

    line_items = []
    product_price = 0
  
    for product in products:
        if product["name"] == product_name:
            price_object = stripe.Price.retrieve(
                product["default_price"],
            )
            line_items.append({"price": product["default_price"], "quantity": 1})
            product_price = price_object["unit_amount"]
            
        else:
            continue
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            client_reference_id=orderId,
            line_items=line_items,
            payment_intent_data={
                "application_fee_amount": round((((product_price * settings.STRIPE_PERCENT_FEE) + settings.STRIPE_AMOUNT_FEE))),
                "transfer_data": {"destination": settings.STRIPE_CONN_ID},
            },
            mode="payment",
            success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain_url + "cancel?session_id={CHECKOUT_SESSION_ID}",
        )
    except Exception as e:
        raise (e)
    return checkout_session.url


def singles(request):
    if request.method == "POST":
        form = Singles(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            gender = form.cleaned_data["gender"]
            email_address = form.cleaned_data["email_address"]
            phone_number = form.cleaned_data["phone_number"]
            skill_level = form.cleaned_data["skill_level"]
            paid_status = False
            matchname = request.POST.get("matchname")

            match = models.Singles(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                email_address=email_address,
                phone_number=phone_number,
                skill_level=skill_level,
                paid_status=paid_status,
            )
            match.save()
            order_id = str(match.id) + "S"
            match.order_id = order_id
            match.save()

            return redirect(create_checkout_session(matchname, order_id))
    else:
        form = Singles
        return render(request, "singles.html", {"form": form})


def doublesnopartner(request):
    if request.method == "POST":
        form = DoublesWithNoPartner(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            gender = form.cleaned_data["gender"]
            email_address = form.cleaned_data["email_address"]
            phone_number = form.cleaned_data["phone_number"]
            skill_level = form.cleaned_data["skill_level"]
            paid_status = False
            matchname = request.POST.get("matchname")

            match = models.DoublesWithNoPartner(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                email_address=email_address,
                phone_number=phone_number,
                skill_level=skill_level,
                paid_status=paid_status,
            )
            match.save()
            order_id = str(match.id) + "DNP"
            match.order_id = order_id
            match.save()

            return redirect(create_checkout_session(matchname, order_id))
    else:
        form = DoublesWithNoPartner
        return render(request, "solo.html", {"form": form})


def doubles(request):
    if request.method == "POST":
        form = Doubles(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            gender = form.cleaned_data["gender"]
            email_address = form.cleaned_data["email_address"]
            phone_number = form.cleaned_data["phone_number"]
            skill_level = form.cleaned_data["skill_level"]
            partner_first_name = form.cleaned_data["partner_first_name"]
            partner_last_name = form.cleaned_data["partner_last_name"]
            partner_gender = form.cleaned_data["partner_gender"]
            partner_email_address = form.cleaned_data["partner_email_address"]
            partner_phone_number = form.cleaned_data["partner_phone_number"]
            partner_skill_level = form.cleaned_data["partner_skill_level"]
            paid_status = False
            matchname = request.POST.get("matchname")

            match = models.Doubles(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                email_address=email_address,
                phone_number=phone_number,
                skill_level=skill_level,
                paid_status=paid_status,
                partner_first_name=partner_first_name,
                partner_last_name=partner_last_name,
                partner_gender=partner_gender,
                partner_email_address=partner_email_address,
                partner_phone_number=partner_phone_number,
                partner_skill_level=partner_skill_level,
            )
            match.save()
            order_id = str(match.id) + "DBL"
            match.order_id = order_id
            match.save()

            return redirect(create_checkout_session(matchname, order_id))
    else:
        form = Doubles
        return render(request, "doubles.html", {"form": form})


def mixeddoubles(request):
    if request.method == "POST":
        form = MixedDoubles(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            gender = form.cleaned_data["gender"]
            email_address = form.cleaned_data["email_address"]
            phone_number = form.cleaned_data["phone_number"]
            skill_level = form.cleaned_data["skill_level"]
            partner_first_name = form.cleaned_data["partner_first_name"]
            partner_last_name = form.cleaned_data["partner_last_name"]
            partner_gender = form.cleaned_data["partner_gender"]
            partner_email_address = form.cleaned_data["partner_email_address"]
            partner_phone_number = form.cleaned_data["partner_phone_number"]
            partner_skill_level = form.cleaned_data["partner_skill_level"]
            paid_status = False
            matchname = request.POST.get("matchname")

            match = models.Doubles(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                email_address=email_address,
                phone_number=phone_number,
                skill_level=skill_level,
                paid_status=paid_status,
                partner_first_name=partner_first_name,
                partner_last_name=partner_last_name,
                partner_gender=partner_gender,
                partner_email_address=partner_email_address,
                partner_phone_number=partner_phone_number,
                partner_skill_level=partner_skill_level,
            )
            match.save()
            order_id = str(match.id) + "MD"
            match.order_id = order_id
            match.save()

            return redirect(create_checkout_session(matchname, order_id))
    else:
        form = MixedDoubles
        return render(request, "mixeddoubles.html", {"form": form})


@csrf_exempt
def stripe_webhook(request):

    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), settings.STRIPE_WH_SECRET
        )
    except ValueError as e:
        print(e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print(e)
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        client_reference_id = session["client_reference_id"]

        if "S" in client_reference_id:
            match = models.Singles.objects.get(order_id=client_reference_id)
            match.paid_status = True
            match.save()

        elif "DBL" in client_reference_id:
            match = models.Doubles.objects.get(order_id=client_reference_id)
            match.paid_status = True
            match.save()

        elif "MD" in client_reference_id:
            match = models.MixedDoubles.objects.get(order_id=client_reference_id)
            match.paid_status = True
            match.save()

        elif "DNP" in client_reference_id:
            match = models.DoublesWithNoPartner.objects.get(
                order_id=client_reference_id
            )
            match.paid_status = True
            match.save()

    return HttpResponse(status=200)
