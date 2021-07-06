""" usage: txt_to_xml.py [-h] [-i INPUTDIR]

Convert txt labels to xml labels.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTDIR, --inputDir INPUTDIR
                        Path to the folder where the text (.txt) labels are stored. If not specified, the CWD will be used.
"""
import os
import glob
import argparse
import cv2


def iterate_dir(source):

    for txt_file in glob.glob(source + '/*.txt'):

        f = open(txt_file)
        f_str = f.read()
        f.close()

        lst = list(map(int, f_str.split()))
        n = lst[0]

        fx = open(txt_file.replace(".txt",".xml"), "x")

        fx.write("<annotation>\n")

        fx.write("  <filename>{}.jpeg</filename>\n".format(txt_file.replace(source,"").replace(".txt","").replace("/","").replace("\\","")))
        im = cv2.imread(txt_file.replace(".txt",".jpeg"))
        h,w,c = im.shape
        fx.write("  <size>\n")
        fx.write("      <width>{}</width>\n".format(w))
        fx.write("      <height>{}</height>\n".format(h))
        fx.write("      <depth>{}</depth>\n".format(c))
        fx.write("  </size>\n")

        fx.write("  <segmented>0</segmented>\n")

        for i in range(n):
            xmin = lst[(i*4)+1]
            ymin = lst[(i*4)+2]
            xmax = lst[(i*4)+3]
            ymax = lst[(i*4)+4]
            fx.write("  <object>\n")
            fx.write("      <name>Gun</name>\n")
            fx.write("      <bndbox>\n")
            fx.write("          <xmin>{}</xmin>\n".format(xmin))
            fx.write("          <ymin>{}</ymin>\n".format(ymin))
            fx.write("          <xmax>{}</xmax>\n".format(xmax))
            fx.write("          <ymax>{}</ymax>\n".format(ymax))
            fx.write("      </bndbox>\n")
            fx.write("  </object>\n")
        fx.write("</annotation>")
        fx.close()


def main():

    # Initiate argument parser
    parser = argparse.ArgumentParser(description="Convert txt labels to xml labels",
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '-i', '--inputDir',
        help='Path to the folder where the text (.txt) labels are stored. If not specified, the CWD will be used.',
        type=str,
        default=os.getcwd()
    )

    args = parser.parse_args()

    # Now we are ready to start the iteration
    iterate_dir(args.inputDir)


if __name__ == '__main__':
    main()