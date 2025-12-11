from django.shortcuts import render

def mileage_calculator(request):
    mileage = None

    if "distance" in request.GET and "fuel" in request.GET:
        try:
            distance = float(request.GET.get("distance"))
            fuel = float(request.GET.get("fuel"))
            mileage = distance / fuel

            print("distance =", distance)
            print("fuel =", fuel)
            print("mileage =", mileage)

        except:
            mileage = None

    return render(request, "mathapp/mileage.html", {"mileage": mileage})
