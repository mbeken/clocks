def wallclock(hour, min):

	# printing position of my clock's hour hand
	h = (hour * 360) // 12 + (min * 360) // (12 * 60)

	# printing position of my clock's minute hand
	m = (min * 360) // (60)

	# here you go to find the angle difference
	angle = abs(h - m)
  
	return angle

print(findAngle(3,00))
