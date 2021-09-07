def FindAngle (hour, minute):
    degreePerMin = 360/60
    degreeOfMin = degreePerMin * minute
    #degree/x * x/hour = degree/hour
    degreePerHour = 360/12
    degreeOfHour = degreePerHour * (hour + minute/60)
    # 30 * (3+0/60) = 90
    #              0-90=90,                    360-90-0=270
    return min(abs(degreeOfMin-degreeOfHour), 360-abs(degreeOfHour-degreeOfMin))

print(FindAngle(12,45))