#this program starts the application -- must be included into all programs created using this library

import sys, os
sys.path.append("infinateWorld_data/")          #add the data folder to the library directory
try:
   import main
except Exception as err:
      exc_type, exc_obj, exc_tb = sys.exc_info()  # this is to get error line number and description.
      file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]  # to get File Name.
      error_string=("ERROR : Error Msg:{}, File Name : {}, Line no : {}\n".format(err,file_name,exc_tb.tb_lineno))
      file_log = open("infinateWorld_report/error_log.log", "w")
      file_log.write(error_string)
      file_log.close()
