from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def not_string(response, str):
  if len(str) >= 3 and str[:3] == "not":
    return HttpResponse(str)
  else:
    return HttpResponse("not " + str)

def make_abba(response, a, b):
  return HttpResponse(a + b + b + a)


def close_far(response, a, b, c):
    a_b_diff = abs(a - b)
    a_c_diff = abs(a - c)
    b_c_diff = abs(b - c)
    if (a_b_diff <= 1 and a_c_diff >= 2 and b_c_diff >= 2) != (a_c_diff <= 1 and a_b_diff >= 2 and b_c_diff >= 2):
        return HttpResponse(True)
    return HttpResponse(False)