#One function that takes length and width and returns both the area and perimeter. (5, 3) gives 15, 16.
def perimeter_and_area():
    lenth=int(input("Enter length of rectangle"))
    width=int(input("Enter width of rectangle"))
    print("The area of rectangle is:",(lenth*width),"m²")
    
    print("The perimetre of rectangle:",2*(lenth+width) )


perimeter_and_area()