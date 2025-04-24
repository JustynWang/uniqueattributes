import arcpy
import timeit

def unique_values(table, field):  ##uses list comprehension
    with arcpy.da.SearchCursor(table, [field]) as cursor:
        return sorted({row[0] for row in cursor})

try:
    arcpy.env.workspace = "C:\Users\jlwan\Downloads\mtbs_perimeter_data"

    start = timeit.default_timer()
    vals = unique_values("mtbs_perims_DD.shp","Fire_Type")

    stop = timeit.default_timer()
    total_time = stop - start
    print(total_time)
    print(vals)

except Exception as e:
    print("Error: " + e.args[0])