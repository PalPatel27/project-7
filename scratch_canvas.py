s1 = int(input('enter the first side of triangle'))
s2 = int(input('enter the second side of triangle'))
s3 = int(input('enter the third side of triangle'))
if s1==s2 and s2==s3:
    print ("equilateral triangle")
elif (s1==s2 and s2 !=s3) or (s2==s3 and s2!=s1) or (s1==s3 and s1 !=s2):
    print ("isosceles triangle")
elif (s1 !=s2 and s1 !=s3 or s2 !=s3):
    print ("scalen triangle")

   