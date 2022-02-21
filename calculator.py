class ConversionRate:
    def ConversionRate(carCount,ARMWashes,plansSold, *bee):
        carCount = int(carCount)
        ARMWashes = int(ARMWashes)
        plansSold = int(plansSold)
        rate = (plansSold/(carCount-ARMWashes))
    
        if bee: 
            print("The Conversion Rate is {:.2%}".format(rate))
    
        return (rate * 100)

