#py.py

'''
    from PIL import Image
    def crop(image_path, coords, saved_location):
        """
        @param image_path: The path to the image to edit
        @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
        @param saved_location: Path to save the cropped image
        """
        image_obj = Image.open(image_path)
        cropped_image = image_obj.crop(coords)
        cropped_image.save(saved_location)
        cropped_image.show()
    if __name__ == '__main__':
        image = 'grasshopper.jpg'
        crop(image, (161, 166, 706, 1050), 'cropped.jpg')
'''
#(x1, y1, x2, y2)
'''
from PIL import Image
image = Image.open('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_002.png')

#cropped = image.crop((0, 0, 1418, 1418))
cropped = image.crop((1418, 1418, 1418, 2835))
cropped.save('E:\\___IIP___home\\_002b.png')
'''
#from PIL import Image

'''
image_to_crop = Image.open('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_002.png')
xcenter = image_to_crop.width/2
ycenter = image_to_crop.height

x1 = xcenter
y1 = ycenter

x2 = 2835
y2 = 1418

image_cropped = image_to_crop.crop((x1, y1, x2, y2))
#image_cropped.show()
image_cropped.save('E:\\___IIP___home\\_002b.png')
'''
import image_slicer
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_004.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_005.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_006.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_007.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_008.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_009.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_010.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_011.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_012.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_013.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_014.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_015.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_016.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_017.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_018.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_019.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_020.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_021.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_022.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_023.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_024.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_025.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_026.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_027.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_028.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_029.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_030.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_031.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_032.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_033.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_034.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_035.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_036.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_037.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_038.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_039.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_040.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_041.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_042.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_043.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_044.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_045.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_046.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_047.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_048.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_049.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_050.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_051.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_052.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_053.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_054.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_055.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_056.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_057.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_058.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_059.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_060.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_061.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_062.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_063.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_064.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_065.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_066.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_067.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_068.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_069.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_070.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_071.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_072.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_073.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_074.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_075.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_076.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_077.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_078.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_079.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_080.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_081.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_082.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_083.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_084.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_085.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_086.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_087.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_088.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_089.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_090.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_091.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_092.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_093.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_094.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_095.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_096.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_097.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_098.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_099.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_100.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_101.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_102.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_103.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_104.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_105.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_106.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_107.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_108.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_109.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_110.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_111.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_112.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_113.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_114.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_115.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_116.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_117.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_118.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_119.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_120.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_121.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_122.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_123.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_124.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_125.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_126.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_127.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_128.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_129.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_130.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_131.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_132.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_133.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_134.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_135.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_136.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_137.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_138.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_139.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_140.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_141.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_142.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_143.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_144.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_145.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_146.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_147.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_148.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_149.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_150.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_151.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_152.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_153.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_154.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_155.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_156.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_157.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_158.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_159.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_160.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_161.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_162.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_163.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_164.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_165.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_166.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_167.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_168.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_169.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_170.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_171.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_172.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_173.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_174.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_175.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_176.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_177.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_178.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_179.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_180.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_181.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_182.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_183.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_184.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_185.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_186.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_187.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_188.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_189.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_190.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_191.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_192.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_193.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_194.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_195.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_196.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_197.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_198.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_199.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_200.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_201.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_202.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_203.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_204.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_205.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_206.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_207.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_208.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_209.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_210.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_211.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_212.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_213.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_214.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_215.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_216.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_217.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_218.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_219.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_220.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_221.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_222.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_223.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_224.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_225.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_226.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_227.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_228.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_229.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_230.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_231.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_232.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_233.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_234.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_235.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_236.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_237.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_238.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_239.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_240.png', 2)

image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_241.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_242.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_243.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_244.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_245.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_246.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_247.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_248.png', 2)
image_slicer.slice('E:\\___IIP___home\\_strony_a\\Symbole i insygnia 2020_główny_Strona_249.png', 2)






