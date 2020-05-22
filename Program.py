import os
import glob
import codecs

import ConfigurationUtils

# TODO: transform in configurations
core = "ITSCREDITV17_CEMG_CORE"
calculators = "ITSCREDITV17_CEMG_CALCULATORS"
flowcredit = "ITSCREDIT_CEMG_FLOWCREDIT"
collections = "ITSCREDITV17_CEMG_COLLECTIONS"
risk = "ITSCREDITV17_CEMG_RISK"
scoring = "ITSCREDITV17_CEMG_SCORING"
externalServices = "ITSCREDITV17_CEMG_EXTERNALSERVICES"

errors = False
module = ""

# open files in order

print("Looking for sql files...")

try:
    if glob.glob('INT/*.sql'):
        # files exists
        for filepath in glob.glob(os.path.join('INT', '*.sql')):

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

            useDb = 'use ' + module

            with codecs.open(filepath, "rt") as file:
                
                fileContent = file.read()

                hints = fileContent.count(useDb.upper())

                if hints == 0:
                    print(useDb + " added!")
                elif hints > 1:
                    print("Multiple uses found.")
                else:
                    print("USE found.")

                fileContent = fileContent.replace(module, "Simuladores" + module).capitalize()

                # convert file encoding to UTF-8
                
                fileContent.encode('utf-8')

                # save file

                file.close()
                print("File saved!")

                # move files to QUA folder

                # TODO move files

            #with codecs.open(filepath, "w", 'utf-8') as targetFile:

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
