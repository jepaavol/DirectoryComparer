import os 

class DirectoryComparer(object):
    
    def __init__(self, options):
        self.source = options.source_dir
        self.target = options.target_dir
        self.output = options.outout



def main():
    import argparse

    # setup command line parsing
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                     description='Organizes files into folders by date using EXIF data')
    parser.add_argument('-s', '--source-dir', type=str, help='source directory')
    parser.add_argument('-t', '--target-dir', type=str, help='target directory')
    parser.add_argument('-o', '--output', type=str, help='Output HTML file', default='output.html')

    # parse command line arguments
    options = parser.parse_args()
    
    dc = DirectoryComparer(options)
    
    
if __name__ == '__main__':
    main()