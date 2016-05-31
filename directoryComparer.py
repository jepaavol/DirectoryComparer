import os
import hashlib

BLOCK_SIZE = 65536


class DirectoryComparer(object):
    
    def __init__(self, options):
        self.source = options.source_dir
        self.target = options.target_dir
        self.output = options.outout

    def process_directory(self, directory):
        """
        Function to walk through folder structure and calculate checksums.
        """
        
        resultDict = {}
        
        for root, dirs, files in os.walk(directory):
            for f in files:
                #Calculating hash over the file
                md5 = self.__get_md5(open(os.path.join(root, f), 'rb'))
                if md5 not in resultDict:
                    resultDict[md5]=[]
                resultDict[md5].append(os.path.join(root, f))
                
        return resultDict

    def __get_md5(self, fp):
        """
        Internal function to get MD5 of the file
        """
        
        hasher = hashlib.md5()
        
        buf = fp.read(BLOCK_SIZE)
        while len(buf) > 0: 
            hasher.update(buf)
            buf = fp.read(BLOCK_SIZE)
        
        return hasher.digest()

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
    dict1 = dc.process_directory(options.source_dir)
    dict2 = dc.process_directory(options.target_dir)
    
    
if __name__ == '__main__':
    main()