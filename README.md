Your TODO list:

-- Make the button in main.js make an http request to "/birthdays"

-- When birthday data comes back from the server, console log it

-- In your django app, create the following
1) a Birthday model with
# Date:
# Name:
# Greeting:
2) a birthdays url configuration
3) a birthdays view
-- makemigrations and migrate to create a birthdays table in your db
-- In birthdays view function, you will need to send back JSON, not rendered HTML
Do this by
1) using `from django.http import JsonResponse`
2) turning the returned data into a list like so: `bday_list = list(your returned data)`
3) making your function `return JsonResponse(bday_list, safe=False)`

-- Once you have the console.log working, move on to looping over the data and appending it to the DOM in an unordered list.

--Getting the full circle of request/response working will give you a small, clean example of serving HTML/JS/JSON from your backend, and appending HTML to the DOM the server-rendered way (index.html) and the browser-rendered way (the birthday data)