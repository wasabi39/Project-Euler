#start with numbers 1 to 19:
total_length = len("onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen")
#20 to 99:
total_length += 8 * len("onetwothreefourfivesixseveneightnine")
total_length += 10 * len("twentythirtyfortyfiftysixtyseventyeightyninety")
#100 to 999
total_length += 100 * len("onetwothreefourfivesixseveneightnine")
total_length += 900 * len("hundred")
total_length += 891 * len("and")
total_length += 9 * len("onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen")
total_length += 72 * len("onetwothreefourfivesixseveneightnine")
total_length += 90 * len("twentythirtyfortyfiftysixtyseventyeightyninety")
#1000
total_length += len("onethousand")
print(total_length)
         