# Ex.04 Design a Website for Server Side Processing
## Date: 11-12-2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:

```
mileage.html

<html>
<head>
    <title>Mileage Calculator</title>
    <style>
        body {
            background: linear-gradient(aliceblue, lightpink, rgb(224, 90, 224));
            padding: 0px;
            background-size: cover;
            background-repeat: no-repeat;
            background-position-x: center;
            background-attachment: fixed;
        }
        .container {
            width: 350px;
            position: relative;
            top: 120px;
            margin: auto;
            background: #e7a1cb;
            padding: 25px;
            border-radius: 10px;
            border: 2px solid #000;
        }
        h2 {
            text-align: center;
            margin-bottom: 20px;
        }
        input {
            width: 100%;
            padding: 8px;
            margin-top: 10px;
            border-radius: 5px;
            border: 1px solid #333;
        }
        button {
            width: 100%;
            padding: 10px;
            margin-top: 15px;
            background: black;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .result {
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Mileage Calculator</h2>

    <form method="get">
        <label>Distance Travelled (km):</label>
        <input type="number" name="distance" required>

        <label>Fuel Used (litres):</label>
        <input type="number" name="fuel" required>

        <button type="submit">Calculate</button>
    </form>

    <div class="result">
        Mileage: {{ mileage }} km/litre
    </div>


<footer style ="text-align: center;"> MADHU SHRUTHI.A.R (25008368) </footer>
</div>
</body>
</html>

```

```
views.py

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
```

```
urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('mileage/', views.mileage_calculator, name='mileage'),
]
```


## OUTPUT - SERVER SIDE:
![Server Output](output.png)

## OUTPUT - WEBPAGE:
![Webpage Output](sideserver.png)



## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
