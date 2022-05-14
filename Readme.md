# How run TCs
* To run tests with allure report: 
  > pytest --alluredir=report_allure
* To run pytest with HTML report: 
  > pytest --html=reports/report.html --self-contained-html
_________________________________________________________
#Souse labs configuration:

* Add SAUCE_USERNAME to your env variables
* Add SAUCE_ACCESS_KEY to your env variables
* Provide system info in run_settings.ini
_________________________________________________________
#How to generate documentation

* install doxygen and add it to your path
* you can change doxygen_config file
* run in terminal doxygen:
     > doxygen doxygen_config