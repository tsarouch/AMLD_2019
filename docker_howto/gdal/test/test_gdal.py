from osgeo import gdal
import os

def get_img_array(img):
    from osgeo import gdal
    # used the first band of the image
    ds = gdal.Open(img)
    band = ds.GetRasterBand(1)
    return band.ReadAsArray()

print(get_img_array(os.getcwd()+"/test.tif"))
print("GDAL works fine!")