""" usage: txt_to_xml.py [-h] [-i INPUTDIR] [-o OUTPUTDIR]

Convert txt labels to xml labels.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTDIR, --inputDir INPUTDIR
                        Path to the folder where the text labels are stored. If not specified, the CWD will be used.
  -o OUTPUTDIR, --outputDir OUTPUTDIR
                        Path to the output folder where the xml labels should be created. Defaults to the same directory as inputDir.
"""
import os
import glob
import argparse
from re import S


def iterate_dir(source, dest):

    for txt_file in glob.glob(source + '/*.txt'):

        f = open(txt_file)
        f_str = f.read()
        f.close()

        lst = list(map(int, f_str.split()))
        n = lst[0]

        fx = open(txt_file.replace(".txt",".xml"), "x")
        fx.write("<annotation> \n")
        fx.write("  <filename>{}.jpeg</filename> \n".format(txt_file.replace(source,"").replace(".txt","").replace("/","").replace("\\","")))
        for i in range(n):
            xmin = lst[(i*4)+1]
            ymin = lst[(i*4)+2]
            xmax = lst[(i*4)+3]
            ymax = lst[(i*4)+4]
            fx.write("  <object> \n")
            fx.write("      <name>Gun</name> \n")
            fx.write("      <bndbox> \n")
            fx.write("          <xmin>{}</xmin> \n".format(xmin))
            fx.write("          <ymin>{}</ymin> \n".format(ymin))
            fx.write("          <xmax>{}</xmax> \n".format(xmax))
            fx.write("          <ymax>{}</ymax> \n".format(ymax))
            fx.write("      </bndbox> \n")
            fx.write("  </object> \n")
        fx.write("</annotation>")
        fx.close()


def main():

    # Initiate argument parser
    parser = argparse.ArgumentParser(description="Convert txt labels to xml labels",
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '-i', '--inputDir',
        help='Path to the folder where the text labels are stored. If not specified, the CWD will be used.',
        type=str,
        default=os.getcwd()
    )
    parser.add_argument(
        '-o', '--outputDir',
        help='Path to the output folder where the xml labels should be created. '
             'Defaults to the same directory as inputDir.',
        type=str,
        default=None
    )
    args = parser.parse_args()

    if args.outputDir is None:
        args.outputDir = args.inputDir

    # Now we are ready to start the iteration
    iterate_dir(args.inputDir, args.outputDir)


if __name__ == '__main__':
    main()