from __future__ import division
import sys, timeit
from random import randint, uniform
import random
from functools import wraps
import matplotlib.pyplot as plt


list_rand_int = lambda Lim, Len, Sign=0: [randint(Sign*Lim,Lim) for x in range(0,Len)]

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4]) # toy for interpretation

def wrap_text(text, highlight=None):
    if highlight is None:
        return str(text)
    else:
        return '%s%s%s' %(highlight, text, color.END)

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def timer(function):

    @wraps(function)
    def func_timer(*args, **kwargs):
        t0 = timeit.default_timer()
        result = function(*args, **kwargs)
        t1 = timeit.default_timer()
        diff = t1 -t0
        print ("Total time running %s: %s seconds" %(wrap_text(function.func_name, color.DARKCYAN), wrap_text(diff, color.YELLOW)))
        return result, diff
    return func_timer

def exchange(List, a, b):
    temp = List[a]
    List[a] = List[b]
    List[b] = temp

def random_partition(List, p, r) :
    x = p + random.randrange(r - p + 1)
    exchange(List, x, r)
    for j in range(p, r):
        if List[j] <= List[r]:
            exchange(List, j, p)
            p +=1
    exchange(List, p, r)
    return p

@timer
def partition_selection(List, i, p=None, r=None):
    """
    This method applies the partition investigation to the list to find the location of the i parameter smallest index
    """
    return _partition_selection(List, p=0, r = len(List)-1, i=i)

def _partition_selection(List, p, r, i):
    if p == r:
        return List[p]
    q = random_partition(List, p, r)
    k = q - p + 1
    if i == k:
        return List[q]
    elif i < k:
        return _partition_selection(List, p, q - 1, i)
    else:
        return _partition_selection(List, q + 1, r, i - k)

@timer
def randomized_select(List, i):
    try:
        start = 0
        end = len(List)-1
        while start < end:
            q = random_partition(List, start, end)
            k = q - start + 1
            if i == k:
                return List[q]
            elif i < k:
                end = q - 1
            else:
                start = q + 1
                i = i - k
        return List[start]
    except Exception as e:
        return e

@timer
def sort_then_select(List, i):
    return _quicksort(List, 0, len(List)-1)[i-1]

def _quicksort(List, p, r):
    if p < r:
        q = random_partition(List, p, r)
        _quicksort(List, p, q - 1)
        _quicksort(List, q + 1, r)
    return List

print """Test 1: control input for debugging""" + '-' * 100
array = [18,5,100,3,1,19,6,0,7,4,2]
for i in range(1, len(array)+1):
    pt1 = randomized_select(array, i)
    print "%s:\t"% ordinal(i), pt1[0]
    plt.scatter(i, pt1[1], color='green')

for i in range(1, len(array)+1):
    pt2 = sort_then_select(array, i)
    print "%s:\t"% ordinal(i), pt2[0]
    plt.scatter(i, pt2[1], color='red')

for i in range(1, len(array)+1):
    pt3 = partition_selection(array, i)
    print "%s:\t"% ordinal(i), pt3[0]
    plt.scatter(i, pt3[1], color='blue')

plt.show()


print """Test 2: randomly generated test input for timing, size 100""" + '-' * 100
array = [-62, -32, 89, 72, -76, -11, 54, -32, -63, 12, 11, 60, 32, -27, 32, 17, -85, -49, -3, 27, -71, 52, -21, -49, 5, -12, 4, -67, 45, 54, -55, 84, 74, 78, -32, 23, 74, 73, 57, 81, -5, 98, 51, 18, 73, -90, 10, -71, 41, -93, -92, 36, -26, -94, -33, -75, 55, 55, 18, 29, -39, -15, -70, 85, -35, 20, 89, -93, -63, -46, 70, 60, -82, -86, 41, 40, 73, 38, 28, 35, -87, -72, 8, 7, -26, -97, 5, -44, 83, 66, -87, 82, 83, -65, 14, -87, 19, -78, 69, -4]
for i in range(1, len(array)+1):
    pt1 = randomized_select(array, i)
    print "%s:\t"% ordinal(i), pt1[0]
    plt.scatter(i, pt1[1], color='green')

for i in range(1, len(array)+1):
    pt2 = sort_then_select(array, i)
    print "%s:\t"% ordinal(i), pt2[0]
    plt.scatter(i, pt2[1], color='red')

for i in range(1, len(array)+1):
    pt3 = partition_selection(array, i)
    print "%s:\t"% ordinal(i), pt3[0]
    plt.scatter(i, pt3[1], color='blue')

plt.show()

print """Test 3: randomly generated test input for timing, size 1000""" + '-' * 100
array = [-35, 5, 46, 34, -1, -97, -73, -30, 33, -35, 97, -94, 22, 91, 62, -45, -45, 26, -5, -79, -24, -92, -28, 76, 40, 75, -5, -5, 11, -9, -70, -9, -65, 65, 59, 0, -61, -87, 34, 80, -43, -4, -99, 87, 66, 90, -83, -31, -92, 92, -80, -85, 34, -21, -15, 34, -76, -25, -61, -48, 90, 43, -31, 52, 21, 4, 48, 13, 88, -8, 75, -87, -32, -27, -28, -33, -92, -8, 63, 30, -66, 21, 94, -17, -45, -19, 19, -84, -84, -60, 86, 98, -64, -39, 3, 46, 60, -6, -75, 16, -84, 29, 48, 75, -13, 44, 98, 52, 93, 97, -74, -15, -67, -2, -17, 79, 71, 100, 49, 46, 63, 5, 30, -75, 19, -7, 25, 95, 96, 57, -88, -72, 69, 82, -12, 23, -78, -73, 55, -2, 8, -15, 49, 17, 2, 68, 98, 81, 91, 94, -98, -30, 79, -73, 78, -49, 65, 83, -46, -62, 28, -86, 46, -60, 61, 16, -83, -8, 83, 84, 70, 57, -44, -54, -7, -68, 9, 23, 41, 42, -73, -32, -83, -26, -37, 71, 93, 38, -16, 21, 10, -39, 46, -58, -81, 23, 51, -4, 72, -33, 58, -29, -81, 82, 47, -47, 70, -85, 68, -41, -74, -82, -85, 98, -90, 46, 64, 82, 24, -81, -94, -74, 76, -19, -59, 6, 96, -20, 90, -51, 10, -15, -73, -17, -58, 44, 48, -19, 91, 25, -4, 39, 35, -71, -20, -26, -1, 75, 86, 56, -55, -37, -46, 3, 100, -56, 82, -82, 24, 52, -47, -51, 94, -70, 71, -25, 36, 73, -30, -42, 8, -99, 34, -56, -20, 71, -1, -76, -70, 68, -85, 3, -22, 10, -60, 46, 64, -35, -37, -14, -39, 5, 82, -96, 68, -95, -68, 24, 92, -81, -62, -36, 36, 49, 42, -2, 95, 47, -94, -46, 49, -63, 39, 2, -68, -15, 42, -60, 42, 55, 59, 84, 53, -52, 99, -65, 16, 55, 23, 42, 99, 45, 53, 92, -79, -28, 17, 4, 31, -42, 67, 75, 53, -80, 19, -14, 91, -45, -21, 96, -18, -92, 13, 14, 73, -69, 11, -61, -13, 43, -32, 90, 38, 70, 76, -20, -54, -82, 42, 79, 76, -79, -47, -31, 32, 27, -75, 25, 38, -90, 81, -67, -76, 32, -41, 90, -29, 71, -97, -7, 69, 42, -91, -70, 48, 34, -16, 46, -78, -91, 2, 75, 32, -27, 0, -16, -68, 5, 71, 38, 89, 62, -1, -7, 79, -83, 10, -18, -47, -11, 26, 81, -93, 31, 57, -85, -65, -90, -51, -18, -58, 2, 18, 30, -32, -95, 61, -34, -70, -31, -81, -82, -54, 19, 94, 83, 61, 60, 4, -59, -7, -58, -47, -40, 17, -7, 62, -47, -18, -69, -2, 22, 16, 66, -21, -60, 89, -100, 54, 78, -11, 0, 50, -69, 64, -18, -35, 62, -87, -72, 26, 8, -93, -94, -81, 97, 91, -65, -57, -8, -81, 14, 20, -100, -68, -59, 32, 62, -68, 3, -99, -49, -70, -11, 58, 100, -67, 2, 46, 67, -93, -56, 75, 74, -80, 55, 37, 77, -23, 7, -48, 43, 21, -53, 39, 74, 54, -68, -19, -30, 53, -4, -6, -80, 66, 21, 88, -18, 93, -25, 39, -30, -52, -74, 25, 54, 3, 92, -98, 86, -36, -90, 46, 82, -97, 22, 43, -17, 92, 35, -67, -4, 95, 95, -90, 22, 89, 34, 60, 35, 52, 23, -52, -80, 33, 97, 20, 92, -94, -77, -69, -46, -94, -74, -89, 14, -44, -81, -85, -17, -4, -63, 43, -65, 68, -27, 75, 13, 82, 37, -20, 34, 56, 57, -8, 69, -38, 78, 80, -97, 23, -26, 13, -92, -90, -41, 2, 71, -83, -29, -37, -4, -10, -76, 98, -25, -35, -64, 71, 64, -5, -32, -35, -18, -48, 50, -8, -46, 0, 12, -95, -6, -35, -85, 93, -61, -26, 11, -92, -25, 32, 81, 8, 81, -66, -34, 15, -27, 37, 1, 4, -52, -81, 99, 71, -56, 38, 4, -51, -70, 2, -54, 33, 60, -72, 33, 88, 29, -6, 46, -1, 94, 56, 88, 97, -82, -64, -74, -40, 29, 6, -56, -35, -49, -95, -43, -34, -50, -94, 5, 51, -11, 50, -64, 88, -74, 71, 19, 1, -71, 43, -74, -59, 5, 12, 28, -51, -92, -17, -56, 26, -1, -41, 72, -23, 89, -17, 48, -65, -63, -74, -8, -88, -83, -43, 15, -71, 96, -50, 8, -39, 31, -17, 39, -43, 55, 65, -34, 9, -19, 53, -40, -5, 56, 85, -19, 70, 27, -84, -38, -6, 33, -19, 83, -48, -68, 95, 88, 10, 54, -34, -2, -80, 93, -45, 41, 34, 85, 68, -38, 48, 40, 95, -100, -98, 18, -39, 47, -30, -22, 13, -67, 53, -5, 51, -50, -85, -45, -31, -6, 10, -26, -13, -66, -92, 66, 40, 12, -47, -33, -25, -25, 17, -40, -77, -51, 69, -51, 8, -51, 28, 84, 79, 72, 33, 62, -36, -86, 82, -3, -25, 56, -7, 58, 38, 69, -97, 52, 84, -47, -77, 19, -74, -55, 85, 20, 30, 2, -93, 17, 20, -41, -9, -91, -76, 78, 29, -26, -99, -7, -88, 17, -29, 52, -71, 71, -93, 69, -31, 92, -63, 92, -96, 98, -44, -10, 71, 34, -53, -65, -70, 97, 92, 18, 19, -77, -79, -62, 74, -70, 43, -12, -47, 92, 24, 15, 67, -64, -20, -55, -67, 60, 56, 37, 13, 88, 69, 86, 12, -13, -71, 81, 42, -46, -36, -67, -71, 55, -69, -49, 14, -87, -17, -65, 83, 83, 31, -47, 5, 88, -3, -93, -85, -71, 85, -66, -32, 12, 92, -26, 34, 71, 3, -68, 29, -56, 18, 36, -2, 97, 38, -91, -97, 74, -100, -48, -90, -85, 6, -49, -5, -16, 6, -86, -6, 92, -7, -91, -38, 74, -37, 21, 2, -62, 41, 80, 74, 70, 52, -31, 53, 54, 78, -37, -52, 93, -4, -69, -13, 15, 49, -24, -91, 83, -82, -14, -26, 20, 63, -37]
for i in range(1, len(array)+1):
    pt1 = randomized_select(array, i)
    print "%s:\t"% ordinal(i), pt1[0]
    plt.scatter(i, pt1[1], color='green')

for i in range(1, len(array)+1):
    pt2 = sort_then_select(array, i)
    print "%s:\t"% ordinal(i), pt2[0]
    plt.scatter(i, pt2[1], color='red')

for i in range(1, len(array)+1):
    pt3 = partition_selection(array, i)
    print "%s:\t"% ordinal(i), pt3[0]
    plt.scatter(i, pt3[1], color='blue')

plt.show()

print """Test 4: randomly generated test input for timing, size 1000""" + '-' * 100
array = [-279, 439, -340, -22, 255, 290, -418, 173, 321, -319, 182, -111, 50, 485, -370, -369, 190, 31, 172, 493, -144, 237, 273, 349, 361, 119, 194, -303, -107, -455, -395, -64, -183, -348, 31, 223, -409, 170, -462, -149, -466, 415, 494, -275, 42, -379, -401, -91, -298, 4, 310, -489, -8, 397, 276, -70, 194, 114, -413, -360, -164, 385, 244, 80, -437, 489, 434, -363, -250, 173, -448, -453, 225, -241, 474, -289, -455, 294, 175, 360, 42, -79, 22, -328, -384, -340, 214, 375, 399, -104, -159, -200, 333, 373, 278, -106, 411, 189, -288, -80, 330, -487, 231, 231, -457, -73, 185, -86, -498, -73, -201, 252, -227, 303, -23, 365, -481, -456, 332, 486, -210, -25, -465, -85, -15, -212, 483, -383, -316, -28, 446, 479, 258, -258, -14, 37, 31, 196, 364, 370, 481, 287, -485, -94, 73, -150, 430, -129, 349, -236, -197, 77, -322, 86, 210, -3, -205, -304, 173, 104, -371, -146, 309, -199, -343, -499, -84, 13, -265, -201, -279, -424, 284, 217, 162, 380, 498, 140, 289, 275, 479, -52, -100, -233, 308, 387, -401, -156, 183, 293, 364, -102, -411, 16, 432, 57, 1, 431, 102, -406, -397, -263, -495, 16, -109, -217, -418, 247, -159, 130, -161, -136, 449, -285, -27, -12, -476, 273, 411, -312, 205, 362, 491, -374, 484, 157, -394, 62, 106, -131, 274, -360, 441, -234, 404, 31, 166, 291, 461, 415, -338, -202, -138, 396, -38, 60, -356, -44, -445, 49, 75, 322, -57, -217, 32, -88, 366, -126, -84, 83, 247, 372, 4, 164, -217, -373, -500, 498, 221, 415, -498, -362, -497, -213, 85, -414, 409, -406, -253, -132, 439, 385, -235, -103, 5, -149, 219, 43, -475, -62, -387, 233, 443, -188, 329, 235, -407, -183, 122, -147, 378, 223, 73, -500, 263, -124, 324, 426, 375, 19, -239, 67, 233, -466, -373, -162, 438, -363, 86, -392, 460, -320, 69, 282, 370, 500, -176, 140, 195, 27, 469, 148, -341, 478, 110, -195, -80, -171, 450, -410, -392, 99, 7, 352, 470, 208, -10, 462, -169, -376, 152, 411, 148, -16, -322, -177, -460, -236, 211, 482, 188, 300, 319, 61, 268, 99, 462, 379, -56, -13, -363, 33, 100, -6, 255, 209, -268, -452, -2, 396, -79, 160, -26, 161, 261, -254, -78, -464, 285, 393, -404, 461, 183, 297, -346, 458, 35, -209, -114, 178, 23, -289, -285, -438, 182, -372, -194, -400, -179, -378, 122, 330, -347, 36, -205, 428, 289, -290, 186, 239, -298, -109, 449, 497, -263, -497, -327, 286, -313, -405, 254, -410, -29, 118, 117, -290, 242, -188, 168, 19, 146, 17, 236, 7, -461, -203, 300, 392, -69, 78, -120, -234, 252, -70, 321, 435, -350, -134, -226, 100, 141, -4, -436, 469, 497, -346, -392, -227, 122, -454, 325, 162, -403, 420, 302, 161, -204, -21, 420, 157, 264, -18, -290, 368, -469, 14, 232, 208, 15, 313, -384, 84, 349, -54, -462, -160, 0, 48, 0, -394, -90, 64, 19, 483, 253, -178, 428, -159, -416, -287, 411, -464, -87, 371, -90, 390, -285, -277, -391, 34, 42, -492, 110, -112, -458, -200, -174, -190, 72, 155, -361, -252, 238, 171, -373, -365, -360, -222, 72, -164, -497, 231, 300, -456, -482, -449, -479, 49, -188, -437, 485, 11, -222, 217, 423, -266, -344, 421, 392, -238, -91, -265, 46, 341, -157, 419, 306, -316, -364, 354, -161, -373, 179, 147, 125, -87, -56, 67, 148, 448, -283, -349, -231, -402, -160, 440, 284, 35, -239, -182, -486, -43, -224, 491, -180, 462, -3, -167, -237, -88, 85, -3, -86, -480, 253, -132, -413, -446, 130, 484, -138, -82, 163, -279, -364, -141, 121, 62, 39, -398, -348, 88, 25, -491, 57, -57, 35, -245, -415, -368, -217, -157, 399, -208, 379, -281, -162, -462, 336, 452, 84, -52, -281, 470, 360, -361, -459, -495, -140, 393, -220, -201, 345, -371, -41, 388, -135, -290, -438, 192, -461, -430, -317, 377, 32, 215, -178, 227, 487, 243, -16, -357, -162, -475, -19, 221, -383, -79, 464, 155, 148, -112, 109, 356, 346, 458, -102, 454, -404, 375, 363, -289, -291, 283, 88, 370, 217, 427, -154, 363, 40, -328, -153, 355, -428, -196, 486, -101, 346, -58, -192, 259, -238, 86, -292, -40, 500, -467, 78, -247, 492, -460, -391, 347, 347, 281, 71, -482, -53, -453, 92, -18, 244, 322, 175, -365, 274, -229, 383, 367, 320, -221, 495, 336, -355, -61, -98, 439, 329, -315, 70, 397, 293, 67, -44, -54, 305, 200, -464, 324, -102, -407, 211, -401, -36, 356, 152, 343, -110, -14, -51, -86, -100, 424, -153, 464, 484, 435, 184, 247, -331, 242, 468, 142, 390, -8, -285, 496, -416, 462, 160, 13, -384, 10, 175, -177, 453, 133, -354, 89, -462, 33, -491, -279, 319, -133, -10, 267, 14, 29, 223, -48, 70, 361, -47, 374, 456, -352, 95, -12, -444, 27, -63, 21, 240, 368, 419, 264, 137, -411, 173, 268, 234, 303, 346, 230, 71, 75, -423, 246, 93, -117, -460, 101, 224, 339, 192, -410, -76, -155, 418, -393, 352, -246, 344, -455, -180, 148, -45, 190, -209, 284, 150, -346, -59, 96, -39, 375, 123, -232, -104, 192, -139, 76, -136, 281, 416, 395, 25, -368, 402, -22, -490, 382, 74, -471, -3, 120, -63, -84, -288, 188, -455, 486, 274, 240, 387, -159, 27, -175, 151, 253, 182, -195, -118, -300, 112, 42, -482, -367, -305, -57, 283, -344, 424, 148, 146, 152, -468, -90, -28, -401, 265, -379, 28, -147, 470, -143, -225, -157, -99, 188, 473, 224, 102, 299, 113, 145, 479, -218, -397, 110, 212, 321, 150, 278, 405, -275, 348, 52, 96, 321, 71, -149, 223, -87, -379, 4, 42, 272, 19, -258, -99, 199, -258, 209, 250, 72, -321, -476, 150, -335, 132, -177, -25, -207, 15, -333, 404, 363, -51, 493, 0, 107, 307, 5, 284, 275, 299, 65, 385, 288, -196, -196, 458, -136, -113, -251, -40, 163]
for i in range(1, len(array)+1):
    pt1 = randomized_select(array, i)
    print "%s:\t"% ordinal(i), pt1[0]
    plt.scatter(i, pt1[1], color='green')

for i in range(1, len(array)+1):
    pt2 = sort_then_select(array, i)
    print "%s:\t"% ordinal(i), pt2[0]
    plt.scatter(i, pt2[1], color='red')

for i in range(1, len(array)+1):
    pt3 = partition_selection(array, i)
    print "%s:\t"% ordinal(i), pt3[0]
    plt.scatter(i, pt3[1], color='blue')

plt.show()


