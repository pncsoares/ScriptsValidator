import os
import glob
import codecs

import ConfigurationUtils

# TODO: transform in configurations
core = "CORE"
calculators = "CALCULATORS"
flowcredit = "FLOWCREDIT"
collections = "COLLECTIONS"
risk = "RISK"
scoring = "SCORING"
externalServices = "EXTERNALSERVICES"

errors = False

# open files in order

print("Looking for sql files...")

try:
    if glob.glob('INT/*.sql'):
        # files exists
        for filepath in glob.glob(os.path.join('INT', '*.sql')):
            with codecs.open(filepath, "r") as sourceFile:
                with codecs.open(filepath, "w", 'utf-8') as targetFile:

                    fileContent = sourceFile.read()
                    fileName = os.path.basename(filepath)

                    print("\nOpening file " + fileName)

                    # verify USE based on file name

                    if core in fileName:
                        module = core

                    elif calculators in fileName:
                        module = calculators

                    elif flowcredit in fileName:
                        module = flowcredit

                    elif collections in fileName:
                        module = collections

                    elif risk in fileName:
                        module = risk

                    elif scoring in fileName:
                        module = scoring

                    elif externalServices in fileName:
                        module = externalServices

                    hints = fileContent.count(' '.join(['USE', module]))

                    if hints == 0:
                        print("USE " + module + " added!")
                    elif hints > 1:
                        print("Multiple uses found.")
                    else:
                        print("USE found.")

                    # convert file encoding to UTF-8

                    fileContent.encode('utf-8')

                    # change USE to target database name

                    # save file

                    targetFile.write(fileContent)
                    print("File saved!")

                    # move files to QUA folder

                    # TODO move files
    else:
        # files not exists
        print("No files found.")

except Exception as ex:
    # error
    print("\nAn error has ocurred:")
    print(ex)
    errors = True

finally:
    if not errors:
        print("\nAll done!\n")
