import arcpy
import arcpy.sa as sa
from glob import glob

print("ObjectID,Raster,NCols,NRows,NBands,PixelType,XMin,YMin,XMax,YMax,SRS")

k = 0
for f in glob(r"e:\raster-types\Data\Tiles\*.tif"):
    r = sa.Raster(f)
    e = r.extent
    k = k + 1
    print(",".join((str(k), str(f), str(r.width), str(r.height), str(r.bandCount), str(r.pixelType), str(e.XMin), str(e.YMin), str(e.XMax), str(e.YMax), str(r.spatialReference.factoryCode))))

